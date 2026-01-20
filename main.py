import streamlit as st
from datetime import datetime
import random

st.set_page_config(
    page_title="🌟 MBTI 진로 추천 스튜디오",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# CSS
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
.hero{
  border: 1px solid var(--stroke);
  background: linear-gradient(135deg, rgba(124,77,255,.18), rgba(0,229,255,.10), rgba(255,79,216,.10));
  box-shadow: var(--shadow), var(--glow);
  border-radius: 26px;
  padding: 26px;
  position: relative;
  overflow: hidden;
}
.badgeRow{ display:flex; gap:10px; flex-wrap:wrap; align-items:center; margin-top: 10px; }
.badge{
  display:inline-flex; align-items:center; gap:8px;
  padding: 8px 12px; border-radius: 999px;
  border: 1px solid var(--stroke); background: var(--pill);
  font-size: 0.92rem;
}
hr.fancy{
  border:0; height:1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.25), transparent);
  margin: 18px 0;
}
.card{
  border:1px solid var(--stroke);
  background: linear-gradient(180deg, var(--card), var(--card2));
  border-radius: 22px;
  padding: 18px;
  box-shadow: var(--shadow);
}
.pill{
  display:inline-block;
  padding: 7px 10px;
  border-radius: 999px;
  border:1px solid var(--stroke);
  background: rgba(255,255,255,.06);
  margin: 4px 6px 0 0;
  font-size: .9rem;
}
.job{
  padding: 12px 14px;
  border-radius: 18px;
  border: 1px solid var(--stroke);
  background: rgba(255,255,255,.06);
  box-shadow: 0 10px 26px rgba(0,0,0,.22);
  margin-bottom: 10px;
}
.job b{ font-size: 1.05rem; }
.job .meta{ opacity:.78; font-size: .92rem; margin-top: 4px; }
.stButton>button, .stDownloadButton>button{
  border-radius: 999px !important;
  border: 1px solid rgba(255,255,255,.18) !important;
}
.stButton>button{
  background: linear-gradient(135deg, rgba(124,77,255,.70), rgba(0,229,255,.55)) !important;
  color: white !important;
  box-shadow: var(--glow);
  padding: .62rem 1.05rem !important;
}
.stDownloadButton>button{
  background: linear-gradient(135deg, rgba(255,79,216,.62), rgba(124,77,255,.62)) !important;
  color: white !important;
  box-shadow: var(--glow);
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Data
# -----------------------------
MBTI_DATA = {
    "ISTJ": {
        "title": "🛡️ ISTJ - 현실적이고 책임감 강한 관리자",
        "keywords": ["📋 체계", "🧾 정확성", "🧱 안정성", "🧠 논리"],
        "jobs": [
            ("📊 회계/재무 분석가", "숫자·규정·정확성이 핵심인 업무에 강해요.", "정밀함 · 책임감 · 신뢰"),
            ("🏛️ 공공행정/정책 실무", "절차를 지키며 안정적으로 운영하는 역할에 적합!", "규정준수 · 운영"),
            ("🧪 품질관리(QA) 매니저", "기준과 프로세스를 설계·점검하는 데 능숙!", "체크리스트 · 표준"),
            ("⚖️ 법무/컴플라이언스", "원칙과 증거를 기반으로 리스크를 관리해요.", "리스크관리 · 문서"),
        ],
        "study": ["📌 자격증/기본기", "🧩 업무 프로세스 이해", "🧠 문서 작성·검토 능력"],
    },
    "ISFJ": {
        "title": "🌿 ISFJ - 따뜻한 실무형 조력자",
        "keywords": ["🤝 배려", "🧷 꼼꼼함", "🏠 안정", "🫶 책임"],
        "jobs": [
            ("🏥 간호/보건 행정", "돌봄과 체계가 동시에 필요한 분야에서 빛나요.", "공감 · 정확"),
            ("📚 교육행정/학사관리", "학생/구성원을 지원하며 운영을 안정화해요.", "지원 · 운영"),
            ("🧑‍⚕️ 상담 코디네이터", "세심한 관찰과 신뢰 형성이 강점!", "관계 · 신뢰"),
            ("🧾 HR 운영/복지 담당", "사람을 챙기며 제도를 실무로 굴리는 역할!", "복지 · 운영"),
        ],
        "study": ["🗣️ 경청/상담 기초", "🧰 실무 툴(문서·데이터)", "📎 서비스 마인드"],
    },
    "INFJ": {
        "title": "🔮 INFJ - 통찰로 사람과 세상을 바꾸는 설계자",
        "keywords": ["🌌 비전", "🫀 가치", "🧭 의미", "🧠 통찰"],
        "jobs": [
            ("🧠 상담심리/코칭", "내면의 패턴을 읽고 성장 경로를 함께 설계해요.", "상담 · 성장"),
            ("📚 교육기획/커리큘럼 디자이너", "학습 경험을 설계하고 방향을 제시해요.", "교육설계 · 철학"),
            ("🧩 UX 리서처", "사용자의 숨은 니즈를 발견하는 데 강해요.", "인사이트 · 질적연구"),
            ("🌍 사회혁신/NGO 기획", "가치 기반 프로젝트에 몰입하기 좋아요.", "임팩트 · 기획"),
        ],
        "study": ["📝 글쓰기/기획", "📊 리서치 방법", "🧠 심리·교육 이론"],
    },
    "INTJ": {
        "title": "🧠 INTJ - 전략과 시스템을 만드는 마스터플래너",
        "keywords": ["♟️ 전략", "🧩 구조화", "📈 최적화", "🔭 장기전"],
        "jobs": [
            ("🛰️ 데이터/AI 전략가", "문제를 구조화하고 전략으로 풀어내요.", "전략 · 분석"),
            ("🏗️ 프로덕트 매니저(PM)", "목표/지표/로드맵으로 제품을 성장시켜요.", "기획 · 로드맵"),
            ("🔐 보안/리스크 아키텍트", "복잡한 시스템의 취약점을 설계 차원에서 해결!", "시스템 · 설계"),
            ("📉 경영컨설턴트", "가설-분석-대안을 빠르게 도출해요.", "가설 · 논리"),
        ],
        "study": ["📐 문제정의/논리", "📊 데이터/지표", "🧱 시스템 사고"],
    },
    "ISTP": {
        "title": "🛠️ ISTP - 실전형 문제 해결사",
        "keywords": ["🔧 실험", "⚙️ 기술", "🧊 침착", "🎯 효율"],
        "jobs": [
            ("🧑‍💻 소프트웨어 엔지니어", "직접 만들고 고치는 것에 강해요.", "실전 · 디버깅"),
            ("🧪 엔지니어(R&D)", "가설 검증과 실험 설계에 재능!", "실험 · 제작"),
            ("🕹️ 게임/실감콘텐츠 개발", "빠른 프로토타이핑에 적합!", "프로토타입 · 개선"),
            ("🚑 현장기술/응급대응", "현장에서 침착하게 해결해요.", "현장대응 · 판단"),
        ],
        "study": ["🧰 메이킹/프로젝트", "🧪 테스트", "📌 문제해결 루틴"],
    },
    "ISFP": {
        "title": "🎨 ISFP - 감각과 진정성을 담는 크리에이터",
        "keywords": ["🌈 감각", "🫧 진정성", "🎧 몰입", "🪷 유연"],
        "jobs": [
            ("🎬 영상/콘텐츠 크리에이터", "감정과 분위기를 표현하는 데 강해요.", "연출 · 스토리"),
            ("🧑‍🎨 그래픽/브랜드 디자이너", "감각적 결과물로 메시지를 전달!", "비주얼 · 감성"),
            ("🎭 예술/공연 기획", "사람들의 경험을 아름답게 만들어요.", "경험 · 큐레이션"),
            ("🧩 UX/UI 디자이너", "사용자의 감정을 고려한 설계에 강점!", "감성 · 사용자"),
        ],
        "study": ["🖌️ 포트폴리오", "🎛️ 툴 숙련", "🧠 사용자 이해"],
    },
    "INFP": {
        "title": "🦋 INFP - 이야기를 만들고 의미를 찾는 이상주의자",
        "keywords": ["📖 스토리", "💗 가치", "🕊️ 자유", "🌱 성장"],
        "jobs": [
            ("✍️ 작가/에디터", "언어로 세계를 만들고 다듬어요.", "글 · 감성"),
            ("🧠 심리/상담 분야", "공감과 의미 찾기를 돕는 일에 강해요.", "공감 · 치유"),
            ("🎨 브랜딩/콘텐츠 전략", "진정성 있는 메시지를 설계해요.", "메시지 · 스토리"),
            ("🌍 국제/사회 분야 기획", "가치 기반 프로젝트에 동기 부여가 큼!", "임팩트 · 가치"),
        ],
        "study": ["📝 글쓰기", "🧭 가치 기반 목표설정", "📚 인문/사회 이해"],
    },
    "INTP": {
        "title": "🧪 INTP - 논리로 세계를 해킹하는 아이디어 엔지니어",
        "keywords": ["🧠 논리", "🧬 탐구", "🧩 모델", "🧿 호기심"],
        "jobs": [
            ("🔬 연구원", "가설을 세우고 검증하는 걸 즐겨요.", "가설 · 검증"),
            ("📊 데이터 사이언티스트", "복잡한 현상을 모델로 설명!", "모델링 · 분석"),
            ("🧑‍💻 알고리즘/백엔드 개발", "구조적 사고로 시스템을 설계해요.", "구조 · 최적화"),
            ("🧠 이론 기반 기획", "개념을 정교하게 다듬는 역할에 강함!", "이론 · 개념"),
        ],
        "study": ["📐 수리/논리", "🐍 파이썬/통계", "🧩 문제정의"],
    },
    "ESTP": {
        "title": "⚡ ESTP - 현장감 넘치는 액션 플레이어",
        "keywords": ["🏁 실행", "🗣️ 설득", "🔥 도전", "🎯 성과"],
        "jobs": [
            ("📣 세일즈/BD", "사람 만나고 기회 잡는 데 강해요.", "협상 · 성과"),
            ("🎤 이벤트/프로모션 기획", "현장 운영과 빠른 대응이 장점!", "현장 · 운영"),
            ("🏃‍♂️ 스포츠/피트니스 코치", "실전 중심 피드백을 빠르게 제공!", "코칭 · 동기"),
            ("📰 현장 취재/미디어", "즉흥성과 관찰력이 강점!", "관찰 · 속도"),
        ],
        "study": ["🗣️ 커뮤니케이션", "📈 성과 지표", "🤝 네트워킹"],
    },
    "ESFP": {
        "title": "🎉 ESFP - 사람 중심의 퍼포머",
        "keywords": ["😄 활력", "🤗 관계", "🎤 표현", "✨ 즐거움"],
        "jobs": [
            ("🎬 크리에이터/MC", "사람을 즐겁게 만드는 재능!", "표현 · 에너지"),
            ("🧑‍💼 고객경험(CX) 매니저", "고객의 감정을 읽고 만족을 높여요.", "관계 · 서비스"),
            ("🎪 행사/공연 기획", "현장 에너지를 만드는 역할!", "운영 · 기획"),
            ("🧑‍🏫 체험형 교육 강사", "즐겁게 참여를 이끄는 강점!", "참여 · 몰입"),
        ],
        "study": ["🎙️ 발표/퍼실리테이션", "🧠 서비스디자인", "📷 콘텐츠 제작"],
    },
    "ENFP": {
        "title": "🌈 ENFP - 열정의 가능성 탐험가",
        "keywords": ["💡 아이디어", "🧨 열정", "🫂 공감", "🚀 확장"],
        "jobs": [
            ("🚀 스타트업/사업기획", "새로운 기회를 만들고 확장하는 걸 좋아해요.", "아이디어 · 실행"),
            ("📣 마케팅/브랜드 전략", "사람의 마음을 움직이는 메시지를 만듦!", "브랜딩 · 캠페인"),
            ("🧑‍🏫 교육/커뮤니티 빌더", "사람을 연결하고 성장시키는 역할!", "커뮤니티 · 성장"),
            ("🧩 HRD/조직문화", "조직의 에너지와 문화를 설계해요.", "문화 · 동기"),
        ],
        "study": ["🧭 진로탐색/포트폴리오", "🗣️ 스토리텔링", "📊 기획/실행 루틴"],
    },
    "ENTP": {
        "title": "🧨 ENTP - 혁신가형 발명가",
        "keywords": ["🧠 발상", "🎭 유머", "🧩 논리", "🛸 혁신"],
        "jobs": [
            ("🧠 전략/기획(컨설팅)", "문제를 재정의하고 판을 바꾸는 데 강해요.", "문제정의 · 혁신"),
            ("🧑‍💻 프로덕트/서비스 기획", "새 기능/새 시장을 설계해요.", "실험 · 기획"),
            ("📢 광고/캠페인 크리에이티브", "한 방의 콘셉트에 강함!", "콘셉트 · 설득"),
            ("🎙️ 커뮤니케이터", "논리+표현으로 설득력을 만듦!", "설득 · 구조"),
        ],
        "study": ["🧩 논증/토론", "📈 실험 설계", "🧠 비판적 사고"],
    },
    "ESTJ": {
        "title": "🏛️ ESTJ - 조직을 굴리는 강력한 리더",
        "keywords": ["📣 리더십", "🧱 질서", "🧾 실행", "🏁 성과"],
        "jobs": [
            ("🧑‍💼 운영/PM", "일정·자원·성과를 맞추는 데 강해요.", "관리 · 실행"),
            ("🏢 인사/조직관리", "규칙과 제도로 조직을 안정화!", "제도 · 운영"),
            ("📦 물류/공급망 관리자", "프로세스를 최적화하고 운영해요.", "운영 · 최적화"),
            ("⚖️ 공공/행정 리더", "명확한 기준으로 조직을 이끎!", "리더십 · 기준"),
        ],
        "study": ["📊 관리/운영", "🧠 의사결정", "🤝 조율"],
    },
    "ESFJ": {
        "title": "💖 ESFJ - 사람을 챙기는 코디네이터",
        "keywords": ["🤝 관계", "🎁 배려", "🗓️ 조율", "🌸 협력"],
        "jobs": [
            ("🧑‍🏫 교사/교육 코디", "학습자 지원과 운영에 강해요.", "지원 · 조율"),
            ("🧑‍💼 HR/채용/교육", "사람을 돕고 연결하는 역할!", "관계 · 케어"),
            ("🏨 서비스/호스피탈리티", "만족도를 높이는 디테일이 강점!", "서비스 · 디테일"),
            ("🧑‍⚕️ 의료/복지 코디", "사람 중심 지원 시스템에 적합!", "지원 · 신뢰"),
        ],
        "study": ["🗣️ 커뮤니케이션", "🧠 서비스 기획", "🧩 갈등 조정"],
    },
    "ENFJ": {
        "title": "👑 ENFJ - 사람을 이끄는 멘토형 리더",
        "keywords": ["🧭 리더십", "💬 설득", "🫶 공감", "🌟 성장"],
        "jobs": [
            ("🧑‍🏫 교육 리더/교수설계", "사람의 성장을 돕는 구조를 만들어요.", "성장 · 설계"),
            ("🧩 HRD/코칭", "조직과 개인의 성장을 연결!", "코칭 · 개발"),
            ("📣 PR/커뮤니케이션", "메시지를 통해 사람을 움직여요.", "설득 · 관계"),
            ("🌍 사회혁신/공익 프로젝트 리드", "가치 기반 팀을 이끌기 좋아요.", "임팩트 · 리드"),
        ],
        "study": ["🎙️ 퍼실리테이션", "📚 교육/심리", "🧭 리더십 훈련"],
    },
    "ENTJ": {
        "title": "🚀 ENTJ - 목표 달성에 강한 지휘관",
        "keywords": ["🏁 목표", "📈 성장", "🧠 전략", "🧱 구조"],
        "jobs": [
            ("📌 사업/전략 기획", "방향을 잡고 실행 체계를 세워요.", "전략 · 실행"),
            ("🏗️ PM/프로그램 디렉터", "복잡한 프로젝트를 추진력 있게 이끎!", "추진 · 관리"),
            ("📊 경영/조직 컨설턴트", "문제 해결과 의사결정에 강점!", "가설 · 개선"),
            ("💼 창업/경영", "큰 그림 + 실행을 동시에!", "리더십 · 성과"),
        ],
        "study": ["📊 KPI/지표", "🧠 의사결정", "🤝 협상"],
    },
    "ENFP2": {},  # 안전장치(사용 안 함)
    "ESFJ2": {},  # 안전장치(사용 안 함)
    "INTJ2": {},  # 안전장치(사용 안 함)
    "INFJ2": {},  # 안전장치(사용 안 함)
    "ENTP2": {},  # 안전장치(사용 안 함)
    "ISFP2": {},  # 안전장치(사용 안 함)
    "ISTP2": {},  # 안전장치(사용 안 함)
    "ISTJ2": {},  # 안전장치(사용 안 함)
    "ISFJ2": {},  # 안전장치(사용 안 함)
    "INFP2": {},  # 안전장치(사용 안 함)
    "INTP2": {},  # 안전장치(사용 안 함)
    "ESTP2": {},  # 안전장치(사용 안 함)
    "ESFP2": {},  # 안전장치(사용 안 함)
    "ESTJ2": {},  # 안전장치(사용 안 함)
}

# 16 types only
MBTI_TYPES = ["ISTJ","ISFJ","INFJ","INTJ","ISTP","ISFP","INFP","INTP","ESTP","ESFP","ENFP","ENTP","ESTJ","ESFJ","ENFJ","ENTJ"]

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown("### 🧭 설정 패널")
    st.markdown('<div class="sidebarCard">', unsafe_allow_html=True)
    selected = st.selectbox("✨ MBTI를 선택하세요", MBTI_TYPES, index=10)
    n_reco = st.slider("🎯 추천 개수", 2, 4, 4)
    vibe = st.select_slider("🌟 추천 분위기", ["안정적", "밸런스", "도전적"], value="밸런스")
    show_study = st.checkbox("📚 추천 역량/준비 팁 보기", value=True)
    show_download = st.checkbox("⬇️ 추천 결과 다운로드 버튼", value=True)
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Header / Hero
# -----------------------------
data = MBTI_DATA[selected]

st.markdown(
    f"""
<div class="hero">
  <h1>🌟 MBTI 진로 추천 스튜디오 🧭</h1>
  <p class="kicker">🎓 진로 교육용 · ✨ 화려한 UI · 💼 직업 추천 · 📚 준비 팁까지 한 번에!</p>
  <hr class="fancy"/>
  <h2 class="spark">{data["title"]}</h2>
  <div class="badgeRow">
    {''.join([f'<span class="badge">{k}</span>' for k in data["keywords"]])}
  </div>
  <p style="margin-top:10px; opacity:.85;">
    🪄 선택한 MBTI의 강점을 바탕으로 <b>잘 맞는 직업</b>을 추천해드려요. (교육용 참고 자료이며 개인차가 있어요! 🙌)
  </p>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# -----------------------------
# Recommend logic (simple)
# -----------------------------
jobs = data["jobs"].copy()
if vibe == "안정적":
    random.shuffle(jobs)  # 가볍게 섞되, 안내만
elif vibe == "도전적":
    random.shuffle(jobs)
else:
    pass

jobs = jobs[:n_reco]

# -----------------------------
# Main content
# -----------------------------
col1, col2 = st.columns([1.15, 0.85], gap="large")

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 💼 추천 직업 리스트 ✨")
    for (job, desc, tags) in jobs:
        st.markdown(
            f"""
<div class="job">
  <b>{job}</b>
  <div class="meta">🧷 {desc}</div>
  <div class="meta">🏷️ {tags}</div>
</div>
""",
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧩 진로 탐색 미션 (교육용) 🎒")
    st.markdown(
        """
- 🧠 **나의 강점 3가지**를 적어보기 (예: 분석력/공감/실행력)  
- 🎯 추천 직업 중 **관심 직업 1개** 선택 → “왜 끌리는지” 5문장 쓰기 ✍️  
- 🔍 그 직업의 **하루 업무/필요 역량/필요 전공**을 조사해서 카드로 정리하기 🗂️  
- 🧪 가능하면 **미니 프로젝트**로 체험해보기 (예: 기획서 1장, 포스터 1개, 분석 리포트 1쪽) 🚀
"""
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🌈 오늘의 한 줄 조언 ✨")
    tips = [
        "🌟 MBTI는 ‘딱 맞는 직업’이 아니라 ‘잘할 가능성이 높은 방식’을 보여줘요!",
        "🧭 진로는 ‘정답 찾기’가 아니라 ‘실험하며 좁혀가기’예요!",
        "🎒 작은 프로젝트 1개가 스펙 10개보다 진로 탐색에 강력할 때가 있어요!",
        "💎 나에게 맞는 환경(팀/업무/피드백 방식)을 찾는 게 핵심!",
    ]
    st.markdown(f"#### 🪄 {random.choice(tips)}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    if show_study:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 📚 추천 준비 팁 & 역량 🔥")
        for s in data["study"]:
            st.markdown(f'<span class="pill">{s}</span>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    if show_download:
        # Create export text
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        export_lines = [
            f"MBTI 진로 추천 결과 ({now})",
            f"- MBTI: {selected}",
            f"- 타이틀: {data['title']}",
            "",
            "추천 직업:",
        ]
        for i, (job, desc, tags) in enumerate(jobs, 1):
            export_lines.append(f"{i}. {job} / {desc} / {tags}")
        export_lines.append("")
        export_lines.append("추천 준비 팁:")
        export_lines.extend([f"- {x}" for x in data["study"]])

        st.download_button(
            "⬇️ 추천 결과 TXT로 저장하기 ✨",
            data="\n".join(export_lines),
            file_name=f"mbti_career_{selected}.txt",
            mime="text/plain",
        )

st.markdown(
    "<div style='opacity:.72; font-size:.92rem; margin-top:18px;'>"
    "🧠 참고: MBTI는 성향 참고용 도구이며, 진로 선택은 적성·가치·역량·경험·환경을 함께 고려하는 것이 좋아요! 🙌"
    "</div>",
    unsafe_allow_html=True,
)
