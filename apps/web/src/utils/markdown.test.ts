import { describe, expect, it } from 'vitest';
import { renderMarkdown } from './markdown';

describe('renderMarkdown', () => {
  it('renders headings with escaped content', () => {
    const html = renderMarkdown('# Title\n## Sub <b>title</b>');
    expect(html).toContain('<h2>Title</h2>');
    expect(html).toContain('<h3>Sub &lt;b&gt;title&lt;/b&gt;</h3>');
  });

  it('renders unordered and ordered lists', () => {
    const html = renderMarkdown('- one\n- two\n\n1. a\n2. b');
    expect(html).toContain('<ul><li>one</li><li>two</li></ul>');
    expect(html).toContain('<ol><li>a</li><li>b</li></ol>');
  });

  it('renders a pipe table skipping the separator row', () => {
    const html = renderMarkdown('| A | B |\n|---|---|\n| 1 | 2 |');
    expect(html).toContain('<th>A</th>');
    expect(html).toContain('<td>1</td>');
    expect(html).not.toContain('---');
  });

  it('renders paragraphs and inline emphasis', () => {
    const html = renderMarkdown('Hello **bold** and *italic* and `code`.');
    expect(html).toContain('<p>Hello <strong>bold</strong> and <em>italic</em> and <code>code</code>.</p>');
  });

  it('escapes dangerous HTML in content', () => {
    const html = renderMarkdown('<script>alert(1)</script>');
    expect(html).not.toContain('<script>');
  });
});