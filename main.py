import streamlit as st
from datetime import datetime
import random

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="🌟 MBTI 진로 추천 스튜디오",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Fancy CSS (no external libs)
# -----------------------------
st.markdown(
    """
<style>
:root{
  --bg1:#0b1020;
  --bg2:#101b3d;
  --card:#0f1730cc;
  --card2:#0f1730aa;
  --stroke:rgba(255,255,255,.14);
  --txt:rgba(255,255,255,.92);
  --muted:rgba(255,255,255,.72);
  --glow:0 0 24px rgba(124, 77, 255,.25), 0 0 48px rgba(0, 229, 255,.14);
  --shadow:0 18px 45px rgba(0,0,0,.45);
  --pill:rgba(255,255,255,.08);
  --accent1:#7c4dff;
  --accent2:#00e5ff;
  --accent3:#ff4fd8;
}

.stApp{
  background: radial-gradient(1200px 600px at 20% 10%, rgba(124,77,255,.35), transparent 60%),
              radial-gradient(900px 500px at 80% 20%, rgba(0,229,255,.25), transparent 55%),
              radial-gradient(800px 480px at 50% 90%, rgba(255,79,216,.18), transparent 60%),
              linear-gradient(160deg, var(--bg1), var(--bg2));
  color: var(--txt);
}
.block-container{
  padding-top: 1.25rem !important;
  padding-bottom: 2rem !important;
}
h1,h2,h3,h4,h5,h6, p, span, label, div { color: var(--txt); }
a { color: rgba(0,229,255,.9) !important; }

.hero{
  border: 1px solid var(--stroke);
  background: linear-gradient(135deg, rgba(124,77,255,.18), rgba(0,229,255,.10), rgba(255,79,216,.10));
  box-shadow: var(--shadow), var(--glow);
  border-radius: 26px;
  padding: 26px 26px 20px 26px;
  position: relative;
  overflow: hidden;
}
.hero:before{
  content:"";
  position:absolute;
  inset:-2px;
  background: radial-gradient(600px 180px at 15% 0%, rgba(255,255,255,.18), transparent 70%);
  pointer-events:none;
}
.badgeRow{
  display:flex; gap:10px; flex-wrap:wrap; align-items:center;
  margin-top: 10px;
}
.badge{
  display:inline-flex;
  align-items:center;
  gap:8px;
  padding: 8px 12px;
  border-radius: 999px;
  border: 1px solid var(--stroke);
  background: var(--pill);
  font-size: 0.92rem;
  box-shadow: 0 10px 30px rgba(0,0,0,.20);
}
.kicker{
  font-size: 1.02rem;
  opacity:.88;
  margin: 0.1rem 0 0.3rem 0;
}
.sub{
  opacity:.82;
  margin-top: .2rem;
}
hr.fancy{
  border:0;
  height:1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.25), transparent);
  margin: 18px 0;
}
.card{
  border:1px solid var(--stroke);
  background: linear-gradient(180deg, var(--card), var(--card2));
  border-radius: 22px;
  padding: 18px 18px 14px 18px;
  box-shadow: var(--shadow);
}
.cardTitle{
  font-size: 1.18rem;
  margin-bottom: 6px;
}
.small{
  opacity: .8;
  font-size: .92rem;
}
.grid2{
  display:grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}
.grid3{
  display:grid;
  grid-template-col

