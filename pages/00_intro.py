import streamlit as st

st.set_page_config(
    page_title="Hi, I'm ___ 👋",
    page_icon="👋",
    layout="wide",
)

# Public-domain-style (clean) Pooh illustration from the 1926 book (Wikimedia Commons)
POOH_IMG_URL = "https://commons.wikimedia.org/wiki/Special:FilePath/Winnie-the-Pooh%2019.png"

# ---- Minimal modern styling (works on Streamlit Cloud) ----
st.markdown(
    """
<style>
:root{
  --bg1:#0b1020;
  --bg2:#101b3d;
  --card:rgba(255,255,255,.06);
  --stroke:rgba(255,255,255,.14);
  --txt:rgba(255,255,255,.92);
  --muted:rgba(255,255,255,.72);
  --glow:0 0 28px rgba(59,130,246,.20), 0 0 56px rgba(34,211,238,.10);
  --shadow:0 18px 50px rgba(0,0,0,.45);
}

.stApp{
  background:
    radial-gradient(1000px 520px at 15% 10%, rgba(59,130,246,.22), transparent 62%),
    radial-gradient(900px 520px at 85% 18%, rgba(34,211,238,.16), transparent 58%),
    linear-gradient(160deg, var(--bg1), var(--bg2));
  color: var(--txt);
}
.block-container{ max-width: 1100px; padding-top: 1.2rem; padding-bottom: 2rem; }
h1,h2,h3,p,span,div { color: var(--txt); }

.hero{
  border:1px solid var(--stroke);
  background: linear-gradient(135deg, rgba(255,255,255,.08), rgba(255,255,255,.05));
  border-radius: 22px;
  padding: 22px;
  box-shadow: var(--shadow), var(--glow);
  overflow:hidden;
}
.badges{ display:flex; gap:8px; flex-wrap:wrap; margin-top:10px; }
.badge{
  border:1px solid var(--stroke);
  background: rgba(255,255,255,.06);
  border-radius: 999px;
  padding: 7px 10px;
  color: var(--muted);
  font-size: .92rem;
}
.card{
  border:1px solid var(--stroke);
  background: rgba(255,255,255,.06);
  border-radius: 18px;
  padding: 16px;
  box-shadow: 0 12px 30px rgba(0,0,0,.35);
}
.small{ color: var(--muted); }
a{ color: rgba(34,211,238,.95) !important; }
</style>
""",
    unsafe_allow_html=True,
)

# ---- Hero ----
st.markdown(
    """
<div class="hero">
  <h1>안녕하세요 👋 저는 <span style="color: rgba(34,211,238,.95);">sue</span>입니다</h1>
  <p class="small" style="margin-top:6px;">
    교육·연구·콘텐츠를 만드는 일을 합니다.
    여기는 제 <b>가볍고 짧은 자기소개 페이지</b>예요.
  </p>
  <div class="badges">
    <span class="badge">🎓 Higher Ed / Learning Design</span>
    <span class="badge">🧩 AI in Education</span>
    <span class="badge">📊 Data-informed Research</span>
    <span class="badge">✍️ Writing & Strategy</span>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# ---- Main layout ----
left, right = st.columns([0.95, 1.05], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("오늘의 한 줄 인사 🌿")
    st.write("“반갑습니다! 배움이 더 쉬워지는 순간을 함께 만들고 싶어요.”")
    st.write("")
    st.subheader("요즘 관심사 🔎")
    st.markdown(
        """
- 생성형 AI 활용 역량 진단/피드백 설계  
- 학습윤리·평가체계(공정성/투명성)  
- 오픈형 온라인 교육 플랫폼 운영 전략  
"""
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("연락 & 링크 ✉️")
    st.markdown(
        """
- 🌐 Portfolio: (여기에 링크)
- 🧾 CV: (여기에 링크)
- 💼 LinkedIn: (여기에 링크)
- ✉️ Email: (여기에 메일)
"""
    )
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("작은 친구와 함께 🧸")
    st.caption("※ 디즈니 버전이 아닌 1926년 원작 삽화(공개 이미지)를 사용했습니다.")
    st.image(POOH_IMG_URL, caption="Winnie-the-Pooh (1926) illustration by E. H. Shepard", use_container_width=True)
    st.markdown(
        """
<div class="small" style="margin-top:10px;">
이 그림은 1926년 출간된 원작 삽화로 Wikimedia Commons에 공개되어 있어요. :contentReference[oaicite:1]{index=1}
</div>
""",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("함께 해볼까요? 🚀")
st.write("원하시면 아래 중 하나로 시작해요:")
c1, c2, c3 = st.columns(3)
with c1:
    st.button("🧠 AI 활용 역량 진단 만들기", use_container_width=True)
with c2:
    st.button("🧩 수업/비교과 프로그램 설계", use_container_width=True)
with c3:
    st.button("✍️ 보고서/콘텐츠 윤문", use_container_width=True)

st.markdown(
    "<p class='small' style='margin-top:10px;'>© Personal intro page · Built with Streamlit</p>",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

