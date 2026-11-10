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

W, H = 1200, 300

THEMES = {
    "dark": {
        "bg_from": "#0b1220", "bg_to": "#0f172a", "border": "#1e293b",
        "glow_right": "#7c3aed", "glow_right_op": "0.30",
        "glow_left": "#2563eb", "glow_left_op": "0.18",
        "accent_from": "#38bdf8", "accent_to": "#a78bfa",
        "eyebrow": "#7dd3fc", "name": "#f8fafc", "sub": "#94a3b8", "label": "#64748b",
        "ring": "#334155", "edge": "#7dd3fc", "face_a": "#38bdf8", "face_b": "#a78bfa",
    },
    "light": {
        "bg_from": "#ffffff", "bg_to": "#f5f7fb", "border": "#d0d7de",
        "glow_right": "#8b5cf6", "glow_right_op": "0.14",
        "glow_left": "#3b82f6", "glow_left_op": "0.10",
        "accent_from": "#2563eb", "accent_to": "#7c3aed",
        "eyebrow": "#2563eb", "name": "#0f172a", "sub": "#475569", "label": "#64748b",
        "ring": "#cbd5e1", "edge": "#1d4ed8", "face_a": "#3b82f6", "face_b": "#8b5cf6",
    },
}

# Centre of the motif on the right-hand side.
CX, CY = 1010, 150
LEFT = 64


def focus_lines() -> tuple[str, str]:
    """Return the <text> elements and the per-line delay rules for the focus ticker."""
    texts = "\n".join(
        f'  <text class="focus f{i}" x="{LEFT}" y="266">{label.replace("&", "&amp;")}</text>'
        for i, label in enumerate(FOCUS)
    )
    delays = "\n".join(
        f"    .f{i} {{ animation-delay: {i * SECONDS_PER_FOCUS}s; }}" for i in range(len(FOCUS))
    )
    return texts, delays


def cube(t: dict, s: float = 54) -> str:
    """An isometric cube centred on (CX, CY); s is the edge length."""
    hx, hy = s * 0.866, s * 0.5  # cos30, sin30
    top = (CX, CY - s)
    left = (CX - hx, CY - hy)
    right = (CX + hx, CY - hy)
    mid = (CX, CY)
    bl = (CX - hx, CY + hy)
    br = (CX + hx, CY + hy)
    bottom = (CX, CY + s)
    p = lambda *pts: " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)  # noqa: E731
    return f"""  <g class="cube">
    <polygon points="{p(top, right, mid, left)}" fill="{t['face_a']}" fill-opacity="0.18"/>
    <polygon points="{p(left, mid, bottom, bl)}" fill="{t['face_b']}" fill-opacity="0.24"/>
    <polygon points="{p(mid, right, br, bottom)}" fill="{t['face_a']}" fill-opacity="0.10"/>
    <g fill="none" stroke="{t['edge']}" stroke-width="1.5" stroke-linejoin="round" stroke-opacity="0.85">
      <polygon points="{p(top, right, br, bottom, bl, left)}"/>
      <polyline points="{p(left, mid, right)}"/>
      <line x1="{mid[0]:.1f}" y1="{mid[1]:.1f}" x2="{bottom[0]:.1f}" y2="{bottom[1]:.1f}"/>
    </g>
    <g fill="{t['edge']}">
      <circle class="twinkle"    cx="{CX - 16}" cy="{CY - 30}" r="2"/>
      <circle class="twinkle t1" cx="{CX + 20}" cy="{CY - 38}" r="1.8"/>
      <circle class="twinkle t2" cx="{CX - 30}" cy="{CY + 14}" r="2"/>
      <circle class="twinkle t3" cx="{CX - 18}" cy="{CY + 34}" r="1.6"/>
      <circle class="twinkle t4" cx="{CX + 26}" cy="{CY + 8}" r="2"/>
      <circle class="twinkle t5" cx="{CX + 34}" cy="{CY + 32}" r="1.6"/>
    </g>
  </g>"""


def render(t: dict) -> str:
    cycle = SECONDS_PER_FOCUS * len(FOCUS)
    # Each line owns 1/len(FOCUS) of the cycle: fade in, hold, fade out.
    share = 100 / len(FOCUS)
    texts, delays = focus_lines()
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
  <title id="title">{NAME}</title>
  <desc id="desc">M.Sc. researcher in 3D computer vision, vision-language-action models, world models and agentic robotics at the Advanced Visual Intelligence Lab, Yeungnam University.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t['bg_from']}"/>
      <stop offset="1" stop-color="{t['bg_to']}"/>
    </linearGradient>
    <radialGradient id="glowR" cx="0.86" cy="0.45" r="0.40">
      <stop offset="0" stop-color="{t['glow_right']}" stop-opacity="{t['glow_right_op']}"/>
      <stop offset="1" stop-color="{t['glow_right']}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowL" cx="0.0" cy="1.0" r="0.5">
      <stop offset="0" stop-color="{t['glow_left']}" stop-opacity="{t['glow_left_op']}"/>
      <stop offset="1" stop-color="{t['glow_left']}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['accent_from']}"/>
      <stop offset="1" stop-color="{t['accent_to']}"/>
    </linearGradient>
    <filter id="glow" x="-200%" y="-200%" width="500%" height="500%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="card"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>
  <style>
    text {{ font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif; }}
    .eyebrow {{ font-size: 13px; font-weight: 600; letter-spacing: 3.5px; fill: {t['eyebrow']}; }}
    .name {{ font-size: 58px; font-weight: 800; letter-spacing: -1.2px; fill: {t['name']}; }}
    .sub {{ font-size: 19px; fill: {t['sub']}; }}
    .label {{ font-size: 12px; font-weight: 600; letter-spacing: 3px; fill: {t['label']}; }}
    .focus {{ font-size: 28px; font-weight: 700; letter-spacing: -0.3px; fill: url(#accent); opacity: 0; animation: cycle {cycle}s ease-in-out infinite; }}
    /* Where animation never runs, the first focus line still shows. */
    .f0 {{ opacity: 1; }}
{delays}
    .ring {{ transform-origin: {CX}px {CY}px; animation: spin 60s linear infinite; }}
    .cube {{ animation: float 7s ease-in-out infinite; }}
    .twinkle {{ animation: twinkle 2.8s ease-in-out infinite; }}
    .t1 {{ animation-delay: 0.4s; }} .t2 {{ animation-delay: 0.8s; }} .t3 {{ animation-delay: 1.2s; }}
    .t4 {{ animation-delay: 1.6s; }} .t5 {{ animation-delay: 2s; }}
    @keyframes cycle {{
      0% {{ opacity: 0; transform: translateY(8px); }}
      {share * 0.15:.2f}% {{ opacity: 1; transform: translateY(0); }}
      {share * 0.85:.2f}% {{ opacity: 1; transform: translateY(0); }}
      {share:.2f}% {{ opacity: 0; transform: translateY(-8px); }}
      100% {{ opacity: 0; }}
    }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    @keyframes float {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-6px); }} }}
    @keyframes twinkle {{ 0%, 100% {{ opacity: 0.2; }} 50% {{ opacity: 1; }} }}
    @media (prefers-reduced-motion: reduce) {{
      * {{ animation: none !important; }}
    }}
  </style>

  <g clip-path="url(#card)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>
    <rect width="{W}" height="{H}" fill="url(#glowL)"/>
    <rect width="{W}" height="{H}" fill="url(#glowR)"/>
    <rect width="{W}" height="3" fill="url(#accent)"/>
  </g>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="{t['border']}"/>

  <text class="eyebrow" x="{LEFT}" y="76">{EYEBROW}</text>
  <text class="name" x="{LEFT - 3}" y="136">{NAME}</text>
  <text class="sub" x="{LEFT}" y="172">{SUBTITLE}</text>
  <rect x="{LEFT}" y="198" width="44" height="2" rx="1" fill="url(#accent)"/>
  <text class="label" x="{LEFT}" y="230">CURRENT FOCUS</text>
{texts}

  <!-- Right: a cube (perception) inside two orbits (prediction) and a slow dashed ring. -->
  <circle class="ring" cx="{CX}" cy="{CY}" r="124" fill="none" stroke="{t['ring']}" stroke-width="1.2" stroke-dasharray="2 10"/>

  <g transform="rotate(-20 {CX} {CY})">
    <ellipse cx="{CX}" cy="{CY}" rx="146" ry="44" fill="none" stroke="url(#accent)" stroke-opacity="0.55" stroke-width="1.3"/>
    <circle r="4.5" fill="{t['accent_from']}" filter="url(#glow)">
      <animateMotion dur="10s" repeatCount="indefinite" path="M{CX - 146},{CY} a146,44 0 1,0 292,0 a146,44 0 1,0 -292,0"/>
    </circle>
  </g>
  <g transform="rotate(28 {CX} {CY})">
    <ellipse cx="{CX}" cy="{CY}" rx="132" ry="36" fill="none" stroke="url(#accent)" stroke-opacity="0.40" stroke-width="1.1"/>
    <circle r="4" fill="{t['accent_to']}" filter="url(#glow)">
      <animateMotion dur="14s" repeatCount="indefinite" path="M{CX - 132},{CY} a132,36 0 1,1 264,0 a132,36 0 1,1 -264,0"/>
    </circle>
  </g>

{cube(t)}
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
