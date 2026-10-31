"""Render the animated profile header as a dark and a light SVG.

Run from the repository root:  python scripts/build_header.py
Edit NAME, SUBTITLE or FOCUS below, re-run, and commit both files in assets/.
The SVGs use only CSS and SMIL animation (no scripts, no web fonts), which is
what GitHub allows inside README images.
"""

from pathlib import Path

NAME = "Md Selim Sarowar"
EYEBROW = "PHYSICAL SUPER INTELLIGENCE  ·  EMBODIED AI"
SUBTITLE = "M.Sc. Researcher  ·  Advanced Visual Intelligence Lab, Yeungnam University"
FOCUS = [
    "World Models & Latent Planning",
    "Vision-Language-Action Models",
    "Agentic Robotics for Manipulation",
    "3D Spatial Intelligence & 6D Pose",
    "Physical Super Intelligence",
]
SECONDS_PER_FOCUS = 3

THEMES = {
    "dark": {
        "bg_from": "#0b1220", "bg_to": "#111827", "border": "#1f2937",
        "glow_right": "#7c3aed", "glow_right_op": "0.35",
        "glow_left": "#0ea5e9", "glow_left_op": "0.22",
        "accent_from": "#22d3ee", "accent_to": "#a78bfa",
        "grid": "#94a3b8", "grid_op": "0.10",
        "eyebrow": "#22d3ee", "name": "#f8fafc", "sub": "#94a3b8", "label": "#64748b",
        "ring": "#334155", "edge": "#67e8f9", "node": "#e2e8f0",
    },
    "light": {
        "bg_from": "#ffffff", "bg_to": "#f6f8fa", "border": "#d0d7de",
        "glow_right": "#8b5cf6", "glow_right_op": "0.16",
        "glow_left": "#0ea5e9", "glow_left_op": "0.12",
        "accent_from": "#0284c7", "accent_to": "#7c3aed",
        "grid": "#64748b", "grid_op": "0.12",
        "eyebrow": "#0284c7", "name": "#0f172a", "sub": "#475569", "label": "#64748b",
        "ring": "#cbd5e1", "edge": "#0369a1", "node": "#334155",
    },
}

# Centre of the 3D motif on the right-hand side.
CX, CY = 985, 160


def focus_lines() -> tuple[str, str]:
    """Return the <text> elements and the per-line delay rules for the focus ticker."""
    texts = "\n".join(
        f'  <text class="focus f{i}" x="60" y="284">{label.replace("&", "&amp;")}</text>'
        for i, label in enumerate(FOCUS)
    )
    delays = "\n".join(
        f"    .f{i} {{ animation-delay: {i * SECONDS_PER_FOCUS}s; }}" for i in range(len(FOCUS))
    )
    return texts, delays


def render(t: dict) -> str:
    cycle = SECONDS_PER_FOCUS * len(FOCUS)
    # Each line owns 1/len(FOCUS) of the cycle: fade in, hold, fade out.
    share = 100 / len(FOCUS)
    texts, delays = focus_lines()
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320" role="img" aria-labelledby="title desc">
  <title id="title">{NAME}</title>
  <desc id="desc">M.Sc. researcher in 3D computer vision, vision-language-action models, world models and agentic robotics at the Advanced Visual Intelligence Lab, Yeungnam University.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t['bg_from']}"/>
      <stop offset="1" stop-color="{t['bg_to']}"/>
    </linearGradient>
    <radialGradient id="glowR" cx="0.82" cy="0.5" r="0.42">
      <stop offset="0" stop-color="{t['glow_right']}" stop-opacity="{t['glow_right_op']}"/>
      <stop offset="1" stop-color="{t['glow_right']}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowL" cx="0.02" cy="0" r="0.55">
      <stop offset="0" stop-color="{t['glow_left']}" stop-opacity="{t['glow_left_op']}"/>
      <stop offset="1" stop-color="{t['glow_left']}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['accent_from']}"/>
      <stop offset="1" stop-color="{t['accent_to']}"/>
    </linearGradient>
    <pattern id="grid" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1.5" cy="1.5" r="1.1" fill="{t['grid']}" fill-opacity="{t['grid_op']}"/>
    </pattern>
    <filter id="glow" x="-200%" y="-200%" width="500%" height="500%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="card"><rect width="1200" height="320" rx="20"/></clipPath>
  </defs>
  <style>
    text {{ font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif; }}
    .eyebrow {{ font-size: 14px; font-weight: 600; letter-spacing: 3.5px; fill: {t['eyebrow']}; }}
    .name {{ font-size: 60px; font-weight: 800; letter-spacing: -1px; fill: {t['name']}; }}
    .sub {{ font-size: 20px; fill: {t['sub']}; }}
    .label {{ font-size: 13px; font-weight: 600; letter-spacing: 3px; fill: {t['label']}; }}
    .focus {{ font-size: 30px; font-weight: 700; fill: url(#accent); opacity: 0; animation: cycle {cycle}s ease-in-out infinite; }}
    /* Where animation never runs, the first focus line still shows. */
    .f0 {{ opacity: 1; }}
{delays}
    .ring {{ transform-origin: {CX}px {CY}px; animation: spin 48s linear infinite; }}
    .cube {{ animation: float 6s ease-in-out infinite; }}
    .twinkle {{ animation: twinkle 2.4s ease-in-out infinite; }}
    .t1 {{ animation-delay: 0.4s; }} .t2 {{ animation-delay: 0.8s; }} .t3 {{ animation-delay: 1.2s; }}
    .t4 {{ animation-delay: 1.6s; }} .t5 {{ animation-delay: 2s; }}
    .pulse {{ animation: twinkle 3.2s ease-in-out infinite; }}
    @keyframes cycle {{
      0% {{ opacity: 0; transform: translateY(10px); }}
      {share * 0.15:.2f}% {{ opacity: 1; transform: translateY(0); }}
      {share * 0.85:.2f}% {{ opacity: 1; transform: translateY(0); }}
      {share:.2f}% {{ opacity: 0; transform: translateY(-10px); }}
      100% {{ opacity: 0; }}
    }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    @keyframes float {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-7px); }} }}
    @keyframes twinkle {{ 0%, 100% {{ opacity: 0.25; }} 50% {{ opacity: 1; }} }}
    @media (prefers-reduced-motion: reduce) {{
      * {{ animation: none !important; }}
    }}
  </style>

  <g clip-path="url(#card)">
    <rect width="1200" height="320" fill="url(#bg)"/>
    <rect width="1200" height="320" fill="url(#grid)"/>
    <rect width="1200" height="320" fill="url(#glowL)"/>
    <rect width="1200" height="320" fill="url(#glowR)"/>
    <rect width="1200" height="4" fill="url(#accent)"/>
  </g>
  <rect x="0.5" y="0.5" width="1199" height="319" rx="20" fill="none" stroke="{t['border']}"/>

  <text class="eyebrow" x="60" y="82">{EYEBROW}</text>
  <text class="name" x="58" y="148">{NAME}</text>
  <text class="sub" x="60" y="188">{SUBTITLE}</text>
  <rect x="60" y="216" width="56" height="3" rx="1.5" fill="url(#accent)"/>
  <text class="label" x="60" y="248">CURRENT FOCUS</text>
{texts}

  <!-- Right: a 3D cube (perception) on orbits (prediction), linked like a graph (reasoning). -->
  <g stroke="{t['ring']}" stroke-width="1" opacity="0.9">
    <line x1="868" y1="58" x2="931" y2="129"/>
    <line x1="1118" y1="64" x2="1039" y2="129"/>
    <line x1="1132" y1="258" x2="1039" y2="191"/>
    <line x1="856" y1="262" x2="931" y2="191"/>
  </g>
  <g fill="{t['node']}">
    <circle class="pulse" cx="868" cy="58" r="4"/>
    <circle class="pulse t2" cx="1118" cy="64" r="4"/>
    <circle class="pulse t4" cx="1132" cy="258" r="4"/>
    <circle class="pulse t3" cx="856" cy="262" r="4"/>
  </g>

  <circle class="ring" cx="{CX}" cy="{CY}" r="132" fill="none" stroke="{t['ring']}" stroke-width="1.5" stroke-dasharray="2 9"/>

  <g transform="rotate(-18 {CX} {CY})">
    <ellipse cx="{CX}" cy="{CY}" rx="150" ry="46" fill="none" stroke="url(#accent)" stroke-opacity="0.6" stroke-width="1.4"/>
    <circle r="5" fill="{t['accent_from']}" filter="url(#glow)">
      <animateMotion dur="9s" repeatCount="indefinite" path="M{CX - 150},{CY} a150,46 0 1,0 300,0 a150,46 0 1,0 -300,0"/>
    </circle>
  </g>
  <g transform="rotate(26 {CX} {CY})">
    <ellipse cx="{CX}" cy="{CY}" rx="138" ry="38" fill="none" stroke="url(#accent)" stroke-opacity="0.45" stroke-width="1.2"/>
    <circle r="4.5" fill="{t['accent_to']}" filter="url(#glow)">
      <animateMotion dur="12s" repeatCount="indefinite" path="M{CX - 138},{CY} a138,38 0 1,1 276,0 a138,38 0 1,1 -276,0"/>
    </circle>
  </g>

  <g class="cube">
    <path d="M985,98 L1039,129 L985,160 L931,129 Z" fill="{t['accent_from']}" fill-opacity="0.20"/>
    <path d="M931,129 L985,160 L985,222 L931,191 Z" fill="{t['accent_to']}" fill-opacity="0.26"/>
    <path d="M985,160 L1039,129 L1039,191 L985,222 Z" fill="#0ea5e9" fill-opacity="0.16"/>
    <g fill="none" stroke="{t['edge']}" stroke-width="1.6" stroke-linejoin="round" stroke-opacity="0.9">
      <path d="M985,98 L1039,129 L1039,191 L985,222 L931,191 L931,129 Z"/>
      <path d="M931,129 L985,160 L1039,129 M985,160 L985,222"/>
    </g>
    <g fill="{t['edge']}">
      <circle class="twinkle" cx="968" cy="131" r="2.2"/>
      <circle class="twinkle t1" cx="1004" cy="122" r="2"/>
      <circle class="twinkle t2" cx="952" cy="176" r="2.2"/>
      <circle class="twinkle t3" cx="962" cy="196" r="1.8"/>
      <circle class="twinkle t4" cx="1012" cy="168" r="2.2"/>
      <circle class="twinkle t5" cx="1022" cy="192" r="1.8"/>
    </g>
  </g>
</svg>
"""


def main() -> None:
    out_dir = Path(__file__).resolve().parent.parent / "assets"
    out_dir.mkdir(exist_ok=True)
    for name, theme in THEMES.items():
        path = out_dir / f"header-{name}.svg"
        path.write_text(render(theme), encoding="utf-8")
        print(f"wrote {path.relative_to(out_dir.parent)}")


if __name__ == "__main__":
    main()
