import streamlit as st
import base64
from pathlib import Path

# ─── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Orion's Eye",
    page_icon="🔭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Load logo ─────────────────────────────────────────────────────────────────
def img_to_b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_text_b64 = img_to_b64("logo_text.jfif")
logo_icon_b64 = img_to_b64("logo_icon.jfif")

# ─── CSS ───────────────────────────────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;900&family=Exo+2:wght@300;400;500;600&display=swap');

/* ── Reset & base ── */
*, *::before, *::after {{ box-sizing: border-box; }}

.stApp {{
    background: #07071a;
    color: #e8e8ff;
    font-family: 'Exo 2', sans-serif;
}}

/* Animated star background */
.stApp::before {{
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse at 20% 50%, rgba(107,33,168,0.15) 0%, transparent 60%),
        radial-gradient(ellipse at 80% 20%, rgba(14,116,144,0.12) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 80%, rgba(27,27,75,0.3) 0%, transparent 60%),
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='800'%3E%3Crect fill='%2307071a'/%3E%3Ccircle cx='100' cy='100' r='1' fill='white' opacity='.8'/%3E%3Ccircle cx='300' cy='50' r='0.7' fill='white' opacity='.6'/%3E%3Ccircle cx='500' cy='150' r='1.2' fill='white' opacity='.9'/%3E%3Ccircle cx='700' cy='80' r='0.5' fill='white' opacity='.5'/%3E%3Ccircle cx='150' cy='300' r='0.8' fill='white' opacity='.7'/%3E%3Ccircle cx='450' cy='250' r='1' fill='%23a78bfa' opacity='.7'/%3E%3Ccircle cx='650' cy='350' r='0.6' fill='white' opacity='.6'/%3E%3Ccircle cx='50' cy='500' r='1.1' fill='white' opacity='.8'/%3E%3Ccircle cx='250' cy='450' r='0.7' fill='%2367e8f9' opacity='.6'/%3E%3Ccircle cx='750' cy='600' r='1' fill='white' opacity='.7'/%3E%3Ccircle cx='350' cy='650' r='0.8' fill='white' opacity='.5'/%3E%3Ccircle cx='600' cy='700' r='1.3' fill='%23a78bfa' opacity='.6'/%3E%3Ccircle cx='200' cy='750' r='0.6' fill='white' opacity='.8'/%3E%3Ccircle cx='400' cy='400' r='0.9' fill='white' opacity='.6'/%3E%3Ccircle cx='550' cy='500' r='0.7' fill='%2367e8f9' opacity='.5'/%3E%3Ccircle cx='720' cy='450' r='1' fill='white' opacity='.7'/%3E%3Ccircle cx='80' cy='650' r='0.8' fill='white' opacity='.6'/%3E%3Ccircle cx='480' cy='780' r='1.1' fill='white' opacity='.7'/%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
}}

/* ── Hide default streamlit elements ── */
#MainMenu, footer, header {{ display: none !important; }}
.block-container {{ padding: 0 !important; max-width: 100% !important; }}
section[data-testid="stSidebar"] {{ display: none; }}

/* ── Navbar ── */
.navbar {{
    position: sticky;
    top: 0;
    z-index: 999;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 48px;
    background: rgba(7,7,26,0.85);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(107,33,168,0.3);
    box-shadow: 0 4px 32px rgba(0,0,0,0.4);
}}
.nav-logo img {{ height: 52px; }}
.nav-links {{
    display: flex;
    gap: 32px;
    list-style: none;
    margin: 0; padding: 0;
}}
.nav-links a {{
    color: #c4b5fd;
    text-decoration: none;
    font-family: 'Exo 2', sans-serif;
    font-weight: 500;
    font-size: 0.92rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    transition: color 0.2s;
}}
.nav-links a:hover {{ color: #67e8f9; }}

/* ── Hero ── */
.hero {{
    position: relative;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
    padding: 80px 24px;
    overflow: hidden;
}}
.hero::before {{
    content: '';
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse at center top, rgba(107,33,168,0.25) 0%, transparent 55%),
        radial-gradient(ellipse at center bottom, rgba(14,116,144,0.15) 0%, transparent 55%);
}}
.hero-logo {{ width: min(420px, 80vw); margin-bottom: 32px; position: relative; z-index:1; }}
.hero-tagline {{
    font-family: 'Orbitron', monospace;
    font-size: clamp(0.9rem, 2.5vw, 1.25rem);
    color: #67e8f9;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    margin-bottom: 24px;
    position: relative; z-index:1;
}}
.hero-title {{
    font-family: 'Orbitron', monospace;
    font-size: clamp(2.2rem, 6vw, 4.5rem);
    font-weight: 900;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 24px;
    position: relative; z-index:1;
    text-shadow: 0 0 40px rgba(167,139,250,0.4);
}}
.hero-sub {{
    font-size: clamp(1rem, 2vw, 1.2rem);
    color: #a78bfa;
    max-width: 680px;
    line-height: 1.7;
    margin-bottom: 48px;
    position: relative; z-index:1;
}}
.btn-primary {{
    display: inline-block;
    padding: 14px 40px;
    background: linear-gradient(135deg, #6b21a8, #0e7490);
    color: white;
    font-family: 'Orbitron', monospace;
    font-size: 0.9rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    text-decoration: none;
    box-shadow: 0 0 30px rgba(107,33,168,0.4);
    transition: all 0.3s;
    position: relative; z-index:1;
}}
.btn-primary:hover {{
    box-shadow: 0 0 50px rgba(107,33,168,0.7);
    transform: translateY(-2px);
}}

/* ── Section base ── */
.section {{
    padding: 100px 48px;
    position: relative;
}}
.section-alt {{ background: rgba(255,255,255,0.02); }}

.section-title {{
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.6rem, 4vw, 2.8rem);
    font-weight: 700;
    color: #ffffff;
    text-align: center;
    margin-bottom: 12px;
    letter-spacing: 0.05em;
}}
.section-title span {{ color: #67e8f9; }}
.section-divider {{
    width: 80px; height: 3px;
    background: linear-gradient(90deg, #6b21a8, #67e8f9);
    margin: 0 auto 60px;
    border-radius: 2px;
}}

/* ── About cards ── */
.about-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 28px;
    max-width: 1200px;
    margin: 0 auto;
}}
.about-card {{
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(107,33,168,0.3);
    border-radius: 20px;
    padding: 36px 28px;
    backdrop-filter: blur(12px);
    transition: transform 0.3s, border-color 0.3s;
}}
.about-card:hover {{
    transform: translateY(-6px);
    border-color: rgba(103,232,249,0.5);
}}
.about-card-icon {{
    font-size: 2.5rem;
    margin-bottom: 18px;
}}
.about-card h3 {{
    font-family: 'Orbitron', monospace;
    font-size: 1rem;
    color: #67e8f9;
    margin-bottom: 12px;
    letter-spacing: 0.05em;
}}
.about-card p {{
    color: #c4b5fd;
    font-size: 0.95rem;
    line-height: 1.7;
}}

/* ── Historia timeline ── */
.timeline {{
    max-width: 800px;
    margin: 0 auto;
    position: relative;
}}
.timeline::before {{
    content: '';
    position: absolute;
    left: 24px;
    top: 0; bottom: 0;
    width: 2px;
    background: linear-gradient(180deg, #6b21a8, #67e8f9, #6b21a8);
}}
.timeline-item {{
    display: flex;
    gap: 32px;
    margin-bottom: 48px;
    padding-left: 16px;
}}
.timeline-dot {{
    width: 20px; height: 20px;
    background: linear-gradient(135deg, #6b21a8, #67e8f9);
    border-radius: 50%;
    flex-shrink: 0;
    margin-top: 4px;
    box-shadow: 0 0 16px rgba(107,33,168,0.6);
    position: relative;
    z-index: 1;
    margin-left: -8px;
}}
.timeline-content {{
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(107,33,168,0.25);
    border-radius: 16px;
    padding: 24px 28px;
    flex: 1;
}}
.timeline-content .date {{
    font-family: 'Orbitron', monospace;
    font-size: 0.75rem;
    color: #67e8f9;
    letter-spacing: 0.1em;
    margin-bottom: 8px;
    text-transform: uppercase;
}}
.timeline-content h3 {{
    color: #ffffff;
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 8px;
}}
.timeline-content p {{
    color: #c4b5fd;
    font-size: 0.9rem;
    line-height: 1.6;
    margin: 0;
}}

/* ── Jaguar Space section ── */
.jaguar-box {{
    max-width: 900px;
    margin: 0 auto;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(14,116,144,0.4);
    border-radius: 24px;
    padding: 56px;
    text-align: center;
    backdrop-filter: blur(12px);
    box-shadow: 0 0 60px rgba(14,116,144,0.1);
}}
.jaguar-box .jaguar-icon {{ font-size: 4rem; margin-bottom: 20px; }}
.jaguar-box h2 {{
    font-family: 'Orbitron', monospace;
    font-size: 1.5rem;
    color: #67e8f9;
    margin-bottom: 24px;
}}
.jaguar-box p {{
    color: #c4b5fd;
    font-size: 1.05rem;
    line-height: 1.8;
    margin-bottom: 16px;
}}
.jaguar-badge {{
    display: inline-block;
    margin-top: 24px;
    padding: 10px 28px;
    background: linear-gradient(135deg, rgba(14,116,144,0.3), rgba(107,33,168,0.3));
    border: 1px solid rgba(103,232,249,0.4);
    border-radius: 50px;
    color: #67e8f9;
    font-family: 'Orbitron', monospace;
    font-size: 0.8rem;
    letter-spacing: 0.1em;
}}

/* ── Noticias ── */
.news-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 28px;
    max-width: 1200px;
    margin: 0 auto;
}}
.news-card {{
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(107,33,168,0.25);
    border-radius: 20px;
    overflow: hidden;
    transition: transform 0.3s, border-color 0.3s;
}}
.news-card:hover {{
    transform: translateY(-6px);
    border-color: rgba(103,232,249,0.4);
}}
.news-card-header {{
    padding: 28px 28px 0;
}}
.news-badge {{
    display: inline-block;
    padding: 4px 14px;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 14px;
}}
.badge-win {{ background: rgba(16,185,129,0.2); color: #34d399; border: 1px solid rgba(52,211,153,0.3); }}
.badge-dev {{ background: rgba(107,33,168,0.2); color: #a78bfa; border: 1px solid rgba(167,139,250,0.3); }}
.badge-event {{ background: rgba(14,116,144,0.2); color: #67e8f9; border: 1px solid rgba(103,232,249,0.3); }}
.news-card h3 {{ color: #fff; font-size: 1.05rem; font-weight: 600; margin-bottom: 12px; }}
.news-card p {{ color: #9ca3c8; font-size: 0.88rem; line-height: 1.6; padding: 0 28px 28px; margin: 0; }}
.news-date {{
    font-size: 0.75rem;
    color: #67e8f9;
    font-family: 'Orbitron', monospace;
    letter-spacing: 0.05em;
    margin-bottom: 10px;
}}

/* ── Team section ── */
.team-intro {{
    text-align: center;
    color: #c4b5fd;
    font-size: 1.05rem;
    max-width: 700px;
    margin: 0 auto 60px;
    line-height: 1.7;
}}
.team-pi {{
    max-width: 400px;
    margin: 0 auto 56px;
}}
.team-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 24px;
    max-width: 1200px;
    margin: 0 auto;
}}
.member-card {{
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(107,33,168,0.25);
    border-radius: 20px;
    padding: 28px 20px 24px;
    text-align: center;
    transition: transform 0.3s, border-color 0.3s, box-shadow 0.3s;
}}
.member-card.pi-card {{
    border-color: rgba(103,232,249,0.4);
    box-shadow: 0 0 40px rgba(14,116,144,0.15);
    background: rgba(14,116,144,0.08);
}}
.member-card:hover {{
    transform: translateY(-6px);
    border-color: rgba(103,232,249,0.5);
    box-shadow: 0 8px 40px rgba(107,33,168,0.25);
}}
.member-avatar {{
    width: 100px; height: 100px;
    border-radius: 50%;
    margin: 0 auto 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.8rem;
    background: linear-gradient(135deg, rgba(107,33,168,0.3), rgba(14,116,144,0.3));
    border: 2px solid rgba(107,33,168,0.4);
    box-shadow: 0 0 24px rgba(107,33,168,0.3);
}}
.member-card.pi-card .member-avatar {{
    width: 120px; height: 120px;
    font-size: 3.5rem;
    border-color: rgba(103,232,249,0.6);
    box-shadow: 0 0 32px rgba(14,116,144,0.4);
}}
.pi-badge {{
    display: inline-block;
    padding: 3px 14px;
    background: linear-gradient(135deg, #6b21a8, #0e7490);
    border-radius: 20px;
    font-size: 0.7rem;
    font-family: 'Orbitron', monospace;
    color: white;
    letter-spacing: 0.08em;
    margin-bottom: 10px;
}}
.member-name {{
    font-weight: 600;
    color: #ffffff;
    font-size: 1rem;
    margin-bottom: 4px;
}}
.member-role {{
    color: #a78bfa;
    font-size: 0.82rem;
    margin-bottom: 8px;
    font-style: italic;
}}
.member-country {{
    color: #67e8f9;
    font-size: 0.78rem;
    font-family: 'Orbitron', monospace;
    letter-spacing: 0.05em;
}}

/* ── Contact section ── */
.contact-container {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 56px;
    max-width: 1100px;
    margin: 0 auto;
    align-items: start;
}}
@media (max-width: 768px) {{
    .contact-container {{ grid-template-columns: 1fr; }}
    .navbar {{ padding: 12px 20px; }}
    .nav-links {{ gap: 16px; }}
    .section {{ padding: 60px 20px; }}
    .jaguar-box {{ padding: 32px 20px; }}
}}
.contact-info h3 {{
    font-family: 'Orbitron', monospace;
    font-size: 1.2rem;
    color: #67e8f9;
    margin-bottom: 24px;
}}
.contact-info p {{
    color: #c4b5fd;
    font-size: 0.95rem;
    line-height: 1.7;
    margin-bottom: 32px;
}}
.contact-item {{
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 16px;
    color: #e8e8ff;
    font-size: 0.9rem;
}}
.contact-item-icon {{
    width: 40px; height: 40px;
    background: rgba(107,33,168,0.2);
    border: 1px solid rgba(107,33,168,0.4);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    flex-shrink: 0;
}}
.social-links {{
    display: flex;
    gap: 14px;
    margin-top: 32px;
    flex-wrap: wrap;
}}
.social-btn {{
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    border: 1px solid rgba(107,33,168,0.4);
    border-radius: 50px;
    color: #c4b5fd;
    text-decoration: none;
    font-size: 0.85rem;
    transition: all 0.2s;
    background: rgba(107,33,168,0.1);
}}
.social-btn:hover {{
    border-color: #67e8f9;
    color: #67e8f9;
    background: rgba(14,116,144,0.15);
}}

/* ── Streamlit form styling ── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {{
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(107,33,168,0.4) !important;
    border-radius: 12px !important;
    color: #e8e8ff !important;
    font-family: 'Exo 2', sans-serif !important;
}}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {{
    border-color: #67e8f9 !important;
    box-shadow: 0 0 0 2px rgba(103,232,249,0.15) !important;
}}
.stTextInput label, .stTextArea label, .stSelectbox label {{
    color: #a78bfa !important;
    font-family: 'Exo 2', sans-serif !important;
    font-size: 0.9rem !important;
}}
.stButton > button {{
    background: linear-gradient(135deg, #6b21a8, #0e7490) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.08em !important;
    padding: 12px 36px !important;
    width: 100% !important;
    box-shadow: 0 0 24px rgba(107,33,168,0.3) !important;
    transition: all 0.3s !important;
}}
.stButton > button:hover {{
    box-shadow: 0 0 40px rgba(107,33,168,0.5) !important;
    transform: translateY(-2px) !important;
}}
.stSelectbox > div > div {{
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(107,33,168,0.4) !important;
    border-radius: 12px !important;
    color: #e8e8ff !important;
}}
.success-msg {{
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(52,211,153,0.3);
    border-radius: 12px;
    padding: 16px 20px;
    color: #34d399;
    font-size: 0.9rem;
    margin-top: 12px;
}}

/* ── Footer ── */
.footer {{
    border-top: 1px solid rgba(107,33,168,0.2);
    padding: 48px;
    text-align: center;
    color: #4a4a7a;
    font-size: 0.85rem;
}}
.footer a {{ color: #6b21a8; text-decoration: none; }}
.footer-logo {{ height: 40px; margin-bottom: 16px; }}

/* ── Scrollbar ── */
::-webkit-scrollbar {{ width: 6px; }}
::-webkit-scrollbar-track {{ background: #07071a; }}
::-webkit-scrollbar-thumb {{ background: rgba(107,33,168,0.5); border-radius: 3px; }}
</style>
""", unsafe_allow_html=True)

# ─── Navbar ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<nav class="navbar">
  <div class="nav-logo">
    <img src="data:image/jpeg;base64,{logo_text_b64}" alt="Orion's Eye">
  </div>
  <ul class="nav-links">
    <li><a href="#acerca">Acerca</a></li>
    <li><a href="#historia">Historia</a></li>
    <li><a href="#jaguar">Jaguar Space</a></li>
    <li><a href="#noticias">Noticias</a></li>
    <li><a href="#equipo">Equipo</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ul>
</nav>
""", unsafe_allow_html=True)

# ─── HERO ──────────────────────────────────────────────────────────────────────
st.markdown(f"""
<section class="hero" id="inicio">
  <img class="hero-logo" src="data:image/jpeg;base64,{logo_text_b64}" alt="Orion's Eye">
  <p class="hero-tagline">✦ Democratizando la Astronomía en Centroamérica ✦</p>
  <h1 class="hero-title">Mira hacia las Estrellas.<br>Desde Casa.</h1>
  <p class="hero-sub">
    Un espectrómetro de bajo costo con rastreo motorizado, análisis espectral en tiempo real
    y una app móvil — construido por y para Centroamérica.
  </p>
  <a href="#acerca" class="btn-primary">🔭 Explorar el Proyecto</a>
</section>
""", unsafe_allow_html=True)

# ─── ACERCA ────────────────────────────────────────────────────────────────────
st.markdown('<div id="acerca"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section">
  <h2 class="section-title">Acerca de <span>Orion's Eye</span></h2>
  <div class="section-divider"></div>
  <div class="about-grid">
    <div class="about-card">
      <div class="about-card-icon">🌌</div>
      <h3>¿Qué es?</h3>
      <p>Un sistema de rastreo celeste basado en espectrometría de bajo costo, que integra herramientas ópticas, electrónicas y digitales en una plataforma accesible para observación y análisis espectral en tiempo real.</p>
    </div>
    <div class="about-card">
      <div class="about-card-icon">⚡</div>
      <h3>¿Cómo funciona?</h3>
      <p>Combina una cámara CMOS, rejilla de difracción, motores paso a paso, sensores IMU/GPS y un Raspberry Pi 4 dentro de una estructura impresa en 3D, compatible con telescopios asequibles.</p>
    </div>
    <div class="about-card">
      <div class="about-card-icon">📱</div>
      <h3>App + Web</h3>
      <p>Una app móvil (iOS/Android) y plataforma web permiten visualización en tiempo real, control del telescopio, calibración automática y una interfaz intuitiva para estudiantes y astrónomos aficionados.</p>
    </div>
    <div class="about-card">
      <div class="about-card-icon">🎓</div>
      <h3>Impacto Educativo</h3>
      <p>Democratizamos el acceso a herramientas de ciencia espacial para estudiantes, clubes de astronomía y entusiastas en regiones sin infraestructura adecuada — alineado con los ODS 4 y 9.</p>
    </div>
    <div class="about-card">
      <div class="about-card-icon">🛠️</div>
      <h3>Open Source</h3>
      <p>Construido completamente con hardware y software de código abierto. Disponible como kit DIY para armar y aprender, o como unidad ensamblada lista para usar.</p>
    </div>
    <div class="about-card">
      <div class="about-card-icon">🌎</div>
      <h3>Centroamérica Primero</h3>
      <p>Diseñado desde Guatemala, Costa Rica, Nicaragua y El Salvador — para posicionar a Centroamérica en la economía espacial global con talento y tecnología regional.</p>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ─── HISTORIA ─────────────────────────────────────────────────────────────────
st.markdown('<div id="historia"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-alt">
  <h2 class="section-title">Nuestra <span>Historia</span></h2>
  <div class="section-divider"></div>
  <div class="timeline">
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="date">Inicio — 2025</div>
        <h3>La Chispa</h3>
        <p>Un grupo de estudiantes e ingenieros de Guatemala, Costa Rica, Nicaragua y El Salvador se unen con una visión común: hacer que la astronomía profesional sea accesible para todos en Centroamérica, sin importar los recursos disponibles.</p>
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="date">Abril 2025</div>
        <h3>La Propuesta</h3>
        <p>El equipo presenta la propuesta "Orion's Eye: Low-Cost Celestial Tracking System" al concurso JS-2025-01 de Jaguar Space, compitiendo con proyectos de toda la región centroamericana.</p>
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="date">Junio 2025</div>
        <h3>¡Seleccionados!</h3>
        <p>Orion's Eye es invitado a la Etapa 2 del concurso. El equipo expande la propuesta técnica, define el WBS, Gantt charts y la estrategia de gestión de proyectos con herramientas de ingeniería de sistemas.</p>
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="date">2025 — Ganadores 🏆</div>
        <h3>¡Financiados por Jaguar Space!</h3>
        <p>Orion's Eye gana el grant de Jaguar Space JS-2025-01. Con $1,500 USD, el equipo inicia oficialmente el desarrollo del prototipo hardware, la app móvil y la plataforma web.</p>
      </div>
    </div>
    <div class="timeline-item">
      <div class="timeline-dot"></div>
      <div class="timeline-content">
        <div class="date">Nov 2025 – Oct 2026</div>
        <h3>Construcción del Futuro</h3>
        <p>12 meses de desarrollo intensivo: ensamblaje de hardware, firmware en C++, app React Native, plataforma web React.js + D3.js, pruebas de campo nocturnas y validación contra Stellarium. El sueño se vuelve realidad.</p>
      </div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ─── JAGUAR SPACE ─────────────────────────────────────────────────────────────
st.markdown('<div id="jaguar"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section">
  <h2 class="section-title">¿Qué es <span>Jaguar Space</span>?</h2>
  <div class="section-divider"></div>
  <div class="jaguar-box">
    <div class="jaguar-icon">🐆</div>
    <h2>Nuestro Patrocinador: Jaguar Space</h2>
    <p>
      <strong style="color:#67e8f9;">Jaguar Space</strong> es una organización fundada con la misión de abrir las puertas del espacio a quienes nunca han tenido esa oportunidad.
      Con raíces en Guatemala, busca galvanizar y fomentar la integración centroamericana en iniciativas espaciales.
    </p>
    <p>
      A través de su convocatoria <strong style="color:#a78bfa;">JS-2025-01 "Advancing Space Science and Engineering in Central America"</strong>,
      Jaguar Space invirtió $5,000 USD en hasta tres proyectos innovadores de la región — seleccionados por rigor técnico,
      factibilidad presupuestal, diversidad del equipo e impacto social.
    </p>
    <p>
      Orion's Eye fue uno de los proyectos ganadores, recibiendo financiamiento para desarrollar su prototipo completo
      durante noviembre 2025 – octubre 2026. Esta alianza nos posiciona como embajadores de la ciencia espacial centroamericana.
    </p>
    <div class="jaguar-badge">✦ Proyecto Ganador JS-2025-01 ✦</div>
  </div>
</section>
""", unsafe_allow_html=True)

# ─── NOTICIAS ─────────────────────────────────────────────────────────────────
st.markdown('<div id="noticias"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-alt">
  <h2 class="section-title">Últimas <span>Noticias</span></h2>
  <div class="section-divider"></div>
  <div class="news-grid">

    <div class="news-card">
      <div class="news-card-header">
        <div class="news-date">Junio 2025</div>
        <span class="news-badge badge-win">🏆 Victoria</span>
        <h3>¡Orion's Eye gana el grant de Jaguar Space!</h3>
      </div>
      <p>Nuestro proyecto fue seleccionado entre las propuestas de toda Centroamérica, obteniendo financiamiento oficial de Jaguar Space para desarrollar el prototipo completo durante 2025-2026.</p>
    </div>

    <div class="news-card">
      <div class="news-card-header">
        <div class="news-date">Mayo 2025</div>
        <span class="news-badge badge-dev">🚀 Desarrollo</span>
        <h3>Invitados a la Etapa 2 del concurso JS-2025-01</h3>
      </div>
      <p>Tras superar la revisión inicial, Orion's Eye fue invitado a presentar la propuesta completa de 5 páginas con plan de gestión, WBS, cronograma y análisis de oportunidades de negocio.</p>
    </div>

    <div class="news-card">
      <div class="news-card-header">
        <div class="news-date">Abril 2025</div>
        <span class="news-badge badge-event">📡 Lanzamiento</span>
        <h3>Kick-off del proyecto: primer hito completado</h3>
      </div>
      <p>El equipo presentó exitosamente el Kick-off Presentation Deck a Jaguar Space, marcando el inicio oficial del período de desempeño del proyecto. Los subequpos de hardware y software comienzan operaciones.</p>
    </div>

    <div class="news-card">
      <div class="news-card-header">
        <div class="news-date">2025</div>
        <span class="news-badge badge-dev">🔧 Técnico</span>
        <h3>Prototipo de espectrómetro en construcción</h3>
      </div>
      <p>El subequipo de hardware inició el ensamblaje del espectrómetro con cámara OV5640 5MP, rejilla de difracción y controlador Raspberry Pi 4. Primeras pruebas con lámpara de sodio programadas.</p>
    </div>

    <div class="news-card">
      <div class="news-card-header">
        <div class="news-date">2025</div>
        <span class="news-badge badge-event">📱 App</span>
        <h3>Wireframes de la app móvil listos</h3>
      </div>
      <p>El equipo de software presentó los wireframes de la app móvil React Native, incluyendo pantallas de login, bitácora estelar, tutorial interactivo y dashboard de análisis espectral.</p>
    </div>

    <div class="news-card">
      <div class="news-card-header">
        <div class="news-date">Próximamente</div>
        <span class="news-badge badge-win">⭐ CEC 2025</span>
        <h3>Presentación pública en CEC 2025</h3>
      </div>
      <p>Los ganadores del grant JS-2025-01 serán anunciados públicamente en el CEC 2025. Orion's Eye estará presente para compartir su visión de democratizar la astronomía en Centroamérica.</p>
    </div>

  </div>
</section>
""", unsafe_allow_html=True)

# ─── EQUIPO ───────────────────────────────────────────────────────────────────
st.markdown('<div id="equipo"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section">
  <h2 class="section-title">Nuestro <span>Equipo</span></h2>
  <div class="section-divider"></div>
  <p class="team-intro">
    Un equipo multidisciplinario de Guatemala, Costa Rica, Nicaragua y El Salvador —
    unidos por la pasión por el espacio y la misión de acercar la astronomía a Centroamérica.
  </p>

  <!-- PI -->
  <div class="team-pi">
    <div class="member-card pi-card">
      <div class="member-avatar">🔭</div>
      <div class="pi-badge">Principal Investigator</div>
      <div class="member-name">Rodolfo Alexander Ramos</div>
      <div class="member-role">Project Development Manager<br>Ingeniero Eléctrico</div>
      <div class="member-country">🇬🇹 Guatemala</div>
    </div>
  </div>

  <!-- Resto del equipo -->
  <div class="team-grid">
    <div class="member-card">
      <div class="member-avatar">🌐</div>
      <div class="member-name">Fausto Amador</div>
      <div class="member-role">Co-Principal Investigator<br>Ing. en Cibernética y Electrónica</div>
      <div class="member-country">🇳🇮 Nicaragua</div>
    </div>
    <div class="member-card">
      <div class="member-avatar">⭐</div>
      <div class="member-name">Mariana Marroquín</div>
      <div class="member-role">Team Leader<br>Tecnología Espacial</div>
      <div class="member-country">🇬🇹 Guatemala</div>
    </div>
    <div class="member-card">
      <div class="member-avatar">⚙️</div>
      <div class="member-name">María José Ramírez</div>
      <div class="member-role">Systems Engineer<br>Data Science Engineering</div>
      <div class="member-country">🇬🇹 Guatemala</div>
    </div>
    <div class="member-card">
      <div class="member-avatar">🤖</div>
      <div class="member-name">Sebastián Madrigal Núñez</div>
      <div class="member-role">Systems Engineer<br>Mecatrónica</div>
      <div class="member-country">🇨🇷 Costa Rica</div>
    </div>
    <div class="member-card">
      <div class="member-avatar">📱</div>
      <div class="member-name">Cristian De León</div>
      <div class="member-role">Principal App Developer<br>Ingeniería en Sistemas</div>
      <div class="member-country">🇬🇹 Guatemala</div>
    </div>
    <div class="member-card">
      <div class="member-avatar">💻</div>
      <div class="member-name">Andrés Hernández Campos</div>
      <div class="member-role">Co-Principal App Developer<br>Instituto Tecnológico de C.R.</div>
      <div class="member-country">🇨🇷 Costa Rica</div>
    </div>
    <div class="member-card">
      <div class="member-avatar">🔬</div>
      <div class="member-name">Luz López</div>
      <div class="member-role">Spectral Analyst<br>Ingeniería Química</div>
      <div class="member-country">🇸🇻 El Salvador</div>
    </div>
    <div class="member-card">
      <div class="member-avatar">📝</div>
      <div class="member-name">Daniela Reyes</div>
      <div class="member-role">Documentation Specialist<br>Mecatrónica · Olimpiada Nacional</div>
      <div class="member-country">🇬🇹 Guatemala</div>
    </div>
    <div class="member-card">
      <div class="member-avatar">🌍</div>
      <div class="member-name">Sarah Serrano</div>
      <div class="member-role">Handling Specialist<br>Web Dev · STEM Outreach</div>
      <div class="member-country">🇬🇹 Guatemala</div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)

# ─── CONTACTO ─────────────────────────────────────────────────────────────────
st.markdown('<div id="contacto"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-alt">
  <h2 class="section-title">Contáctanos</h2>
  <div class="section-divider"></div>
  <div class="contact-container">
    <div class="contact-info">
      <h3>¿Tienes preguntas o quieres colaborar?</h3>
      <p>
        Estamos abiertos a colaboraciones académicas, medios de comunicación, posibles aliados
        y cualquier persona apasionada por hacer el espacio más accesible en Centroamérica.
      </p>
      <div class="contact-item">
        <div class="contact-item-icon">✉️</div>
        <span>alexramosr2002@gmail.com</span>
      </div>
      <div class="contact-item">
        <div class="contact-item-icon">📍</div>
        <span>Guatemala, Costa Rica, Nicaragua, El Salvador</span>
      </div>
      <div class="contact-item">
        <div class="contact-item-icon">🔭</div>
        <span>Proyecto financiado por Jaguar Space JS-2025-01</span>
      </div>
      <div class="social-links">
        <a href="#" class="social-btn">📸 Instagram</a>
        <a href="#" class="social-btn">🐦 Twitter / X</a>
        <a href="#" class="social-btn">💼 LinkedIn</a>
        <a href="#" class="social-btn">💻 GitHub</a>
      </div>
    </div>
""", unsafe_allow_html=True)

# ── Formulario Streamlit (dentro del grid) ───
with st.container():
    st.markdown('<div style="background:rgba(255,255,255,0.04);border:1px solid rgba(107,33,168,0.3);border-radius:20px;padding:36px 32px;">', unsafe_allow_html=True)

    nombre = st.text_input("Nombre completo", placeholder="Tu nombre")
    email  = st.text_input("Correo electrónico", placeholder="tu@correo.com")
    asunto_opts = ["Colaboración académica", "Medios / Prensa", "Inversión / Alianza", "Consulta general", "Otro"]
    asunto = st.selectbox("Asunto", asunto_opts)
    mensaje = st.text_area("Mensaje", placeholder="Cuéntanos cómo podemos colaborar...", height=140)

    if st.button("🚀 Enviar Mensaje"):
        if nombre and email and mensaje:
            st.markdown('<div class="success-msg">✅ ¡Mensaje enviado! Nos pondremos en contacto pronto.</div>', unsafe_allow_html=True)
        else:
            st.warning("Por favor completa todos los campos.")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div></section>', unsafe_allow_html=True)

# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown(f"""
<footer class="footer">
  <img class="footer-logo" src="data:image/jpeg;base64,{logo_icon_b64}" alt="Orion's Eye">
  <p style="color:#6b6b9a; margin-bottom:8px;">
    Orion's Eye — Proyecto financiado por <a href="https://jaguarspace.net" target="_blank">Jaguar Space</a> · Grant JS-2025-01
  </p>
  <p style="color:#3a3a5c;">
    © 2025 Orion's Eye Team · Guatemala · Costa Rica · Nicaragua · El Salvador
  </p>
  <p style="color:#3a3a5c; margin-top:8px; font-size:0.8rem;">
    ✦ Democratizando la Astronomía en Centroamérica ✦
  </p>
</footer>
""", unsafe_allow_html=True)
