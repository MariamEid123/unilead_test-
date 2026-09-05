export default function HeroIllustration() {
  return (
    <svg
      viewBox="0 0 480 440"
      className="hero-illustration"
      role="img"
      aria-label="Illustration of a learning dashboard with progress and AI coaching"
    >
      <defs>
        <linearGradient id="hi-blob" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="var(--color-primary-light)" />
          <stop offset="100%" stopColor="var(--color-bg)" />
        </linearGradient>
        <linearGradient id="hi-ring" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0%" stopColor="var(--color-primary)" />
          <stop offset="100%" stopColor="var(--color-primary-dark)" />
        </linearGradient>
      </defs>

      {/* backdrop blob */}
      <path
        d="M240 20c92 0 180 52 200 140 18 82-30 160-118 196-84 34-186 18-232-56C42 232 30 140 84 78 126 30 178 20 240 20Z"
        fill="url(#hi-blob)"
      />

      {/* main card: lesson / competency progress */}
      <g transform="translate(58 96)">
        <rect width="256" height="176" rx="20" fill="var(--color-surface)" />
        <rect width="256" height="176" rx="20" fill="none" stroke="var(--color-border)" strokeWidth="1.5" />
        <rect x="24" y="28" width="120" height="12" rx="6" fill="var(--color-text)" opacity="0.85" />
        <rect x="24" y="48" width="80" height="9" rx="4.5" fill="var(--color-text-faint)" />

        <rect x="24" y="84" width="208" height="8" rx="4" fill="var(--color-neutral-light)" />
        <rect x="24" y="84" width="146" height="8" rx="4" fill="url(#hi-ring)" />

        <g transform="translate(24 110)">
          <circle cx="10" cy="10" r="10" fill="var(--color-success-light)" />
          <path d="M6 10l3 3 5-6" stroke="var(--color-success)" strokeWidth="1.8" fill="none" strokeLinecap="round" strokeLinejoin="round" />
          <rect x="28" y="5" width="110" height="10" rx="5" fill="var(--color-neutral-light)" />
        </g>
        <g transform="translate(24 132)">
          <circle cx="10" cy="10" r="10" fill="var(--color-warning-light)" />
          <circle cx="10" cy="10" r="4" fill="var(--color-warning)" />
          <rect x="28" y="5" width="90" height="10" rx="5" fill="var(--color-neutral-light)" />
        </g>
      </g>

      {/* floating AI coach bubble */}
      <g transform="translate(300 42)">
        <rect width="150" height="86" rx="18" fill="var(--color-accent)" />
        <rect x="18" y="20" width="90" height="9" rx="4.5" fill="var(--color-surface)" opacity="0.92" />
        <rect x="18" y="38" width="114" height="9" rx="4.5" fill="var(--color-surface)" opacity="0.6" />
        <rect x="18" y="56" width="66" height="9" rx="4.5" fill="var(--color-surface)" opacity="0.6" />
        <path d="M28 86l-14 20 26-12z" fill="var(--color-accent)" />
      </g>

      {/* competency badge */}
      <g transform="translate(300 268)">
        <circle cx="46" cy="46" r="46" fill="var(--color-surface)" stroke="var(--color-border)" strokeWidth="1.5" />
        <circle cx="46" cy="46" r="34" fill="none" stroke="var(--color-neutral-light)" strokeWidth="8" />
        <circle
          cx="46"
          cy="46"
          r="34"
          fill="none"
          stroke="url(#hi-ring)"
          strokeWidth="8"
          strokeDasharray="176 214"
          strokeLinecap="round"
          transform="rotate(-90 46 46)"
        />
        <path d="M34 46l8 8 16-18" stroke="var(--color-primary)" strokeWidth="3.4" fill="none" strokeLinecap="round" strokeLinejoin="round" />
      </g>

      {/* small orange accent chip */}
      <g transform="translate(40 320)">
        <rect width="118" height="60" rx="16" fill="var(--color-surface)" stroke="var(--color-border)" strokeWidth="1.5" />
        <circle cx="30" cy="30" r="14" fill="var(--color-accent-light)" />
        <path d="M24 30l4 4 8-9" stroke="var(--color-accent)" strokeWidth="2.2" fill="none" strokeLinecap="round" strokeLinejoin="round" />
        <rect x="54" y="20" width="48" height="8" rx="4" fill="var(--color-text)" opacity="0.75" />
        <rect x="54" y="34" width="34" height="7" rx="3.5" fill="var(--color-text-faint)" />
      </g>
    </svg>
  );
}
