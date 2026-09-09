function escapeHtml(text: string): string {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function renderInline(text: string): string {
  const escaped = escapeHtml(text);
  return escaped
    .replace(/`([^`]+)`/g, (_, code: string) => `<code>${code}</code>`)
    .replace(/\*\*([^*\n]+)\*\*/g, (_, bold: string) => `<strong>${bold}</strong>`)
    .replace(/(^|\s)\*([^*\n]+)\*(?=\s|$)/g, (_, lead: string, italic: string) => `${lead}<em>${italic}</em>`);
}

interface TableBlock {
  rows: string[][];
}

function isTableLine(line: string): boolean {
  return line.trim().startsWith('|');
}

function isTableSeparator(line: string): boolean {
  return /^\s*\|?[\s:|-]+\|?\s*$/.test(line) && line.includes('-');
}

function isListLine(line: string): { ordered: boolean } | null {
  if (/^\s*[-*+]\s+/.test(line)) return { ordered: false };
  if (/^\s*\d+\.\s+/.test(line)) return { ordered: true };
  return null;
}

function isHeading(line: string): number | null {
  const match = /^(#{1,6})\s+(.*)$/.exec(line);
  return match ? match[1]!.length : null;
}

export function renderMarkdown(markdown: string): string {
  const lines = markdown.replace(/\r\n/g, '\n').split('\n');
  const blocks: string[] = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i]!;
    const trimmed = line.trim();

    if (trimmed === '' || trimmed === '---' || trimmed === '***' || trimmed === '___') {
      i += 1;
      continue;
    }

    const headingDepth = isHeading(line);
    if (headingDepth !== null) {
      const content = line.replace(/^#{1,6}\s+/, '');
      const headingLevel = Math.min(Math.max(headingDepth + 1, 2), 6);
      blocks.push(`<h${headingLevel}>${renderInline(content)}</h${headingLevel}>`);
      i += 1;
      continue;
    }

    const list = isListLine(line);
    if (list) {
      const items: string[] = [];
      while (i < lines.length) {
        const item = lines[i]!;
        const itemList = isListLine(item);
        if (!itemList) break;
        items.push(renderInline(item.replace(/^\s*(?:[-*+]|\d+\.)\s+/, '')));
        i += 1;
      }
      const tag = list.ordered ? 'ol' : 'ul';
      blocks.push(`<${tag}>${items.map((item) => `<li>${item}</li>`).join('')}</${tag}>`);
      continue;
    }

    if (isTableLine(line)) {
      const table: TableBlock = { rows: [] };
      while (i < lines.length && isTableLine(lines[i]!)) {
        const rowLine = lines[i]!.trim();
        if (!isTableSeparator(rowLine)) {
          const cells = rowLine
            .replace(/^\|/, '')
            .replace(/\|$/, '')
            .split('|')
            .map((cell) => renderInline(cell.trim()));
          table.rows.push(cells);
        }
        i += 1;
      }
      if (table.rows.length > 0) {
        const [header, ...body] = table.rows;
        blocks.push(
          '<div class="md-table"><table>' +
            `<thead><tr>${(header ?? []).map((cell) => `<th>${cell}</th>`).join('')}</tr></thead>` +
            (body.length > 0
              ? `<tbody>${body.map((row) => `<tr>${row.map((cell) => `<td>${cell}</td>`).join('')}</tr>`).join('')}</tbody>`
              : '') +
            '</table></div>'
        );
      }
      continue;
    }

    const paragraph: string[] = [];
    while (i < lines.length) {
      const current = lines[i]!.trim();
      if (current === '') break;
      if (isHeading(lines[i]!) !== null || isListLine(lines[i]!) || isTableLine(lines[i]!)) break;
      paragraph.push(renderInline(current));
      i += 1;
    }
    if (paragraph.length > 0) {
      blocks.push(`<p>${paragraph.join(' ')}</p>`);
    }
  }

  return blocks.join('\n');
}