import streamlit as st
from datetime import datetime

# =========================================================
# Page
# =========================================================
st.set_page_config(
    page_title="AI 활용 역량 진단 · 맞춤 로드맵",
    page_icon="🫧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# Pastel UI CSS (tasteful emojis, soft gradients)
# =========================================================
st.markdown(
    """
<style>
:root{
  --bg1:#fbfbff;
  --bg2:#f3f7ff;
  --card:#ffffffcc;
  --stroke:rgba(30, 60, 90, .10);
  --txt:#19324a;
  --muted:#516a7c;
  --shadow:0 14px 40px rgba(30, 60, 90, .10);
  --shadow2:0 8px 22px rgba(30, 60, 90, .08);
  --sky:#cfe6ff;
  --lav:#d9d7ff;
  --mint:#bfeee3;
  --peach:#ffd6cc;
  --rose:#ffd3ea;
}

.stApp{
  background:
    radial-gradient(900px 520px at 15% 5%, rgba(217,215,255,.55), transparent 60%),
    radial-gradient(820px 520px at 88% 12%, rgba(191,238,227,.55), transparent 58%),
    radial-gradient(900px 520px at 55% 98%, rgba(255,214,204,.45), transparent 62%),
    linear-gradient(180deg, var(--bg1), var(--bg2));
  color: var(--txt);
}
.block-container{
  padding-top: 1.15rem !important;
  padding-bottom: 2.2rem !important;
  max-width: 1240px;
}
h1,h2,h3,h4, p, span, label, div { color: var(--txt); }

.hero{
  border: 1px solid var(--stroke);
  background: linear-gradient(135deg, rgba(255,255,255,.82), rgba(255,255,255,.68));
  border-radius: 22px;
  padding: 22px 22px 16px 22px;
  box-shadow: var(--shadow);
  position: relative;
  overflow: hidden;
}
.hero:before{
  content:"";
  position:absolute; inset:-2px;
  background:
    radial-gradient(540px 220px at 0% 0%, rgba(207,230,255,.75), transparent 60%),
    radial-gradient(520px 220px at 100% 0%, rgba(255,211,234,.55), transparent 62%),
    radial-gradient(520px 220px at 50% 120%, rgba(191,238,227,.50), transparent 62%);
  pointer-events:none;
}
.pillRow{ display:flex; flex-wrap:wrap; gap:8px; margin-top: 10px;}
.pill{
  display:inline-flex; align-items:center; gap:8px;
  padding: 7px 10px;
  border-radius: 999px;
  border: 1px solid var(--stroke);
  background: rgba(255,255,255,.70);
  box-shadow: var(--shadow2);
  font-size: .92rem;
  color: var(--muted);
}

.card{
  border: 1px solid var(--stroke);
  background: rgba(255,255,255,.72);
  border-radius: 18px;
  padding: 16px 16px 14px 16px;
  box-shadow: var(--shadow2);
}
.small{ color: var(--muted); font-size: .92rem; }
.hr{
  height:1px;
  background: linear-gradient(90deg, transparent, rgba(30,60,90,.14), transparent);
  margin: 14px 0;
  border:0;
}

.kpi{ display:flex; gap:12px; flex-wrap:wrap; }
.kpiBox{
  flex: 1 1 190px;
  border:1px solid var(--stroke);
  border-radius: 16px;
  padding: 12px 14px;
  background: rgba(255,255,255,.70);
  box-shadow: var(--shadow2);
}
.kpiTitle{ color: var(--muted); font-size: .86rem; margin-bottom: 2px;}
.kpiValue{ font-size: 1.18rem; font-weight: 750; }

.sectionTitle{
  display:flex; align-items:center; justify-content:space-between; gap:10px;
}
.badge{
  display:inline-flex; align-items:center; gap:8px;
  padding: 7px 10px;
  border-radius: 999px;
  border:1px solid var(--stroke);
  background: rgba(255,255,255,.72);
  color: var(--muted);
  font-size: .88rem;
  box-shadow: var(--shadow2);
}

.item{
  border: 1px solid var(--stroke);
  background: rgba(255,255,255,.64);
  border-radius: 16px;
  padding: 12px 14px;
  box-shadow: var(--shadow2);
  margin-bottom: 10px;
}
.item b{ font-size: 1.02rem; }
.tag{
  display:inline-block; margin-right: 8px; margin-top: 6px;
  padding: 6px 10px; border-radius: 999px;
  border:1px solid var(--stroke);
  background: rgba(255,255,255,.74);
  color: var(--muted);
  font-size: .86rem;
}

/* Roadmap lanes */
.lanes{
  display:grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}
.lane{
  border: 1px solid var(--stroke);
  background: linear-gradient(135deg, rgba(255,255,255,.78), rgba(255,255,255,.62));
  border-radius: 18px;
  padding: 14px;
  box-shadow: var(--shadow2);
  position: relative;
  overflow: hidden;
}
.lane:before{
  content:"";
  position:absolute; inset:-2px;
  opacity:.55;
  background: radial-gradient(520px 200px at 0% 0%, rgba(207,230,255,.65), transparent 60%);
  pointer-events:none;
}
.laneHeader{
  display:flex; align-items:flex-start; justify-content:space-between; gap:10px;
  position: relative;
}
.laneTitle{
  font-weight: 800;
  font-size: 1.02rem;
}
.laneMeta{ color: var(--muted); font-size: .90rem; margin-top: 3px; }

.flow{
  display:grid;
  grid-template-columns: 1fr;
  gap: 10px;
  margin-top: 10px;
  position: relative;
}
.step{
  border: 1px solid var(--stroke);
  background: rgba(255,255,255,.74);
  border-radius: 16px;
  padding: 12px 12px;
  box-shadow: var(--shadow2);
}
.stepTitle{ font-weight: 750; }
.stepDesc{ color: var(--muted); font-size:.90rem; margin-top:4px; }
.stepTags{ margin-top: 7px; }
.arrow{
  text-align:center;
  color: rgba(25,50,74,.55);
  font-size: 1.1rem;
  margin: -4px 0 -2px 0;
}

/* Buttons */
.stButton>button{
  border-radius: 999px !important;
  border: 1px solid rgba(30,60,90,.16) !important;
  background: linear-gradient(135deg, rgba(207,230,255,.95), rgba(191,238,227,.95)) !important;
  color: #16324a !important;
  box-shadow: var(--shadow2);
  padding: .62rem 1.05rem !important;
}
.stDownloadButton>button{
  border-radius: 999px !important;
  border: 1px solid rgba(30,60,90,.16) !important;
  background: linear-gradient(135deg, rgba(255,211,234,.92), rgba(217,215,255,.90)) !important;
  color: #16324a !important;
  box-shadow: var(--shadow2);
}
</style>
""",
    unsafe_allow_html=True,
)

# =========================================================
# Diagnostic model (4 dimensions, 16 items)
# =========================================================
DIMENSIONS = [
    {
        "key": "knowledge",
        "name": "AI 지식",
        "icon": "🧠",
        "tone": "개념을 이해하고 올바르게 설명·적용하는 힘",
        "pill": "개념·한계·용어",
    },
    {
        "key": "workflow",
        "name": "도구 활용 & 학습 워크플로우",
        "icon": "🧩",
        "tone": "과제 흐름에 맞춰 AI를 배치해 생산성과 학습효과를 높이는 힘",
        "pill": "단계화·템플릿",
    },
    {
        "key": "critical",
        "name": "비판적 사고",
        "icon": "🔎",
        "tone": "근거·가정·반례를 점검하며 결과를 개선하는 힘",
        "pill": "검증·논리",
    },
    {
        "key": "ethics",
        "name": "학습 윤리",
        "icon": "🫧",
        "tone": "표절·저작권·개인정보·기여도 등 책임 있는 활용",
        "pill": "투명성·책임",
    },
]

# 16 items (4 per dimension). Likert 1~5
ITEMS = [
    # AI Knowledge (4)
    {"dim": "knowledge", "q": "생성형 AI의 강점과 한계(환각·편향·최신성 등)를 설명할 수 있다."},
    {"dim": "knowledge", "q": "내 과제에서 AI가 잘하는 일/하면 안 되는 일을 구분할 수 있다."},
    {"dim": "knowledge", "q": "모델 출력이 왜 달라지는지(입력 맥락·지시·데이터)에 대해 이해한다."},
    {"dim": "knowledge", "q": "AI 활용 시 필요한 기본 용어(프롬프트, 컨텍스트, 토큰, RAG 등)를 대략 이해한다."},

    # Workflow (4)
    {"dim": "workflow", "q": "과제를 ‘자료수집→구조화→초안→검토→개선’ 단계로 나눠 AI를 배치한다."},
    {"dim": "workflow", "q": "반복 작업을 템플릿(요청서/목차/체크리스트)으로 만들어 재사용한다."},
    {"dim": "workflow", "q": "출력물을 표/요약/목차 등 구조로 먼저 만들고 문장화한다."},
    {"dim": "workflow", "q": "AI를 활용한 작업 기록(프롬프트/수정/근거)을 남겨 관리한다."},

    # Critical Thinking (4)
    {"dim": "critical", "q": "AI 결과의 핵심 주장/근거를 분리해 확인한다."},
    {"dim": "critical", "q": "불확실한 내용은 ‘가정·근거·반례’를 질문해 재검토한다."},
    {"dim": "critical", "q": "수치·정책·인용 등 고위험 정보는 원문/신뢰 출처로 교차검증한다."},
    {"dim": "critical", "q": "결과를 그대로 쓰지 않고, 내 판단으로 수정·보완해 품질을 높인다."},

    # Ethics (4)
    {"dim": "ethics", "q": "과제에서 AI 사용 범위(초안/교정/아이디어 등)를 투명하게 표시한다."},
    {"dim": "ethics", "q": "저작권/인용 규칙을 지키며, 무단 전재·표절을 피한다."},
    {"dim": "ethics", "q": "개인정보/민감정보는 입력하지 않으며 필요 시 익명화한다."},
    {"dim": "ethics", "q": "AI 생성문장을 그대로 제출하지 않고, 내 문장으로 재구성한다."},
]

# Improvements by level
IMPROVEMENTS = {
    "knowledge": {
        "low": ["핵심 개념 10개(환각·편향·최신성·근거 등) 1페이지 정리", "‘AI가 잘/못하는 일’ 체크리스트를 과제마다 적용"],
        "mid": ["내 전공 사례로 ‘AI 사용 가능 범위’ 기준 문장화", "출력 품질 변동 요인을 기록해 재현 가능하게 만들기"],
        "high": ["복수 접근(대안) 비교로 최적 전략 선택", "전공별 고위험 영역(법/의료/데이터) 위험관리 규칙 만들기"],
    },
    "workflow": {
        "low": ["과제 흐름 5단계(수집-구조-초안-검토-개선)로 분해", "출력 형식(표/목차/요약)을 먼저 고정"],
        "mid": ["과제 유형별 템플릿 3종(요약/비교/보고서) 만들기", "작업 로그(프롬프트-수정-근거) 간단히 남기기"],
        "high": ["나만의 워크플로우 패키지(템플릿+체크리스트) 구축", "팀 협업에서 역할/기여/버전관리 규칙 적용"],
    },
    "critical": {
        "low": ["핵심 주장 3개 뽑기 → 근거 여부만 먼저 확인", "출처가 필요한 문장에는 ‘근거/링크 요청’ 습관화"],
        "mid": ["가정-근거-반례 질문을 프롬프트에 기본 포함", "루브릭(정확·근거·명확·윤리)로 자기점검 후 수정"],
        "high": ["교차검증(다른 출처/관점) 루틴 고도화", "반박 가능한 지점(약점)을 선제적으로 보완"],
    },
    "ethics": {
        "low": ["AI 사용 범위 표기 템플릿을 과제에 붙이기", "개인정보 입력 금지/익명화 규칙 만들기"],
        "mid": ["인용·저작권 체크리스트(이미지·표·데이터) 적용", "‘내 문장 재구성’ 단계를 제출 전 필수로"],
        "high": ["과정 로그로 기여도/학습을 증빙(투명성 강화)", "팀 프로젝트 윤리 규칙(공동작성/AI 사용 합의) 운영"],
    },
}

def level(avg: float):
    if avg < 2.4:
        return "기초", "🌱", "지금은 ‘기본 루틴’을 안정적으로 만드는 단계예요."
    if avg < 3.6:
        return "중간", "🌿", "기본 활용은 가능! ‘품질·검증·재사용성’을 강화하면 좋아요."
    return "심화", "✨", "상당히 능숙! ‘표준화·협업·고도화’로 확장해볼 단계예요."

def band(score: float):
    if score <= 2.4:
        return "low"
    if score <= 3.6:
        return "mid"
    return "high"

# Program library: for each dimension, connect Tips -> Course -> Extracurricular
PROGRAMS = {
    "knowledge": {
        "course": [
            {"title": "AI 리터러시(기초)", "hours": "2학점(또는 8주)", "desc": "생성형 AI 개념·한계·전공 적용 기준", "tags": ["개념", "한계", "전공사례"]},
            {"title": "AI 이해와 사회(심화)", "hours": "3학점(또는 15주)", "desc": "편향·신뢰성·데이터 기반 사고 확장", "tags": ["편향", "신뢰", "데이터"]},
        ],
        "extra": [
            {"title": "AI 용어·사례 마이크로러닝", "hours": "60분", "desc": "핵심 개념 10개를 사례로 빠르게 정리", "tags": ["마이크로", "퀴즈"]},
            {"title": "전공별 AI 활용 세미나", "hours": "90분", "desc": "전공 과제에 맞춘 ‘가능/금지/주의’ 기준 만들기", "tags": ["전공", "사례"]},
        ],
    },
    "workflow": {
        "course": [
            {"title": "AI 기반 학습전략/글쓰기", "hours": "2학점(또는 8주)", "desc": "자료→구조→초안→검토→개선 워크플로우 설계", "tags": ["워크플로우", "템플릿"]},
            {"title": "데이터/리서치 방법과 AI", "hours": "3학점(또는 15주)", "desc": "조사 설계·정리·리포트 자동화", "tags": ["리서치", "자동화"]},
        ],
        "extra": [
            {"title": "프롬프트 & 템플릿 스튜디오", "hours": "2시간", "desc": "요약/비교/보고서 템플릿 3종 제작", "tags": ["템플릿", "실습"]},
            {"title": "개인 워크플로우 클리닉", "hours": "1시간", "desc": "내 과제 기반으로 루틴을 1개 완성", "tags": ["클리닉", "개별"]},
        ],
    },
    "critical": {
        "course": [
            {"title": "비판적 사고와 논증", "hours": "2~3학점", "desc": "가정-근거-반례로 사고 구조화", "tags": ["논증", "근거"]},
            {"title": "정보검증/미디어 리터러시", "hours": "2학점", "desc": "출처·팩트체크·통계 해석", "tags": ["팩트체크", "통계"]},
        ],
        "extra": [
            {"title": "AI 결과 검증 실습랩", "hours": "2시간", "desc": "오류 찾기→수정→근거 정리 훈련", "tags": ["검증", "실습"]},
            {"title": "루브릭 기반 자기점검 워크숍", "hours": "90분", "desc": "정확·근거·명확·윤리 루브릭 적용", "tags": ["루브릭", "품질"]},
        ],
    },
    "ethics": {
        "course": [
            {"title": "학습윤리/연구윤리", "hours": "1~2학점", "desc": "표절·인용·저작권·기여도", "tags": ["표절", "인용"]},
            {"title": "AI 윤리와 거버넌스", "hours": "2~3학점", "desc": "책임 있는 사용, 개인정보·편향·안전", "tags": ["책임", "개인정보"]},
        ],
        "extra": [
            {"title": "AI 사용 범위 표기 클리닉", "hours": "45분", "desc": "과제에 붙일 ‘AI 활용 공개문’ 템플릿 완성", "tags": ["투명성", "템플릿"]},
            {"title": "저작권·인용 가이드 세션", "hours": "60분", "desc": "이미지/표/데이터 라이선스 체크", "tags": ["저작권", "체크"]},
        ],
    },
}

# =========================================================
# Sidebar
# =========================================================
with st.sidebar:
    st.markdown("### 설정")
    st.caption("진단 → 개선 → 교과/비교과 로드맵")
    st.markdown("---")
    mode = st.radio("응답 방식", ["슬라이더(1~5)", "라디오(1~5)"], index=0)
    st.markdown("---")
    show_details = st.checkbox("문항 설명/세부 팁 펼치기", value=False)
    show_download = st.checkbox("결과 다운로드", value=True)

# =========================================================
# Hero
# =========================================================
st.markdown(
    """
<div class="hero">
  <h1>AI 활용 역량 진단 · 맞춤 학습 로드맵</h1>
  <p class="small" style="margin-top:6px;">
    🫧 4개 영역(지식·워크플로우·비판적 사고·윤리)을 진단하고, <b>개선 행동</b>과 <b>교과·비교과 프로그램</b>을
    하나의 흐름으로 연결해 추천합니다.
  </p>
  <div class="pillRow">
    <span class="pill">🧠 AI 지식</span>
    <span class="pill">🧩 도구·워크플로우</span>
    <span class="pill">🔎 비판적 사고</span>
    <span class="pill">🫧 학습 윤리</span>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# =========================================================
# Inputs
# =========================================================
left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 진단 문항 (총 16문항)")
    st.caption("각 문항은 1(아직 어려움) ~ 5(매우 능숙) 기준으로 응답하세요.")

    responses = []
    for i, it in enumerate(ITEMS, 1):
        label = f"{i:02d}. {it['q']}"
        key = f"item_{i}"
        if mode.startswith("슬라이더"):
            val = st.slider(label, 1, 5, 3, key=key)
        else:
            val = st.radio(label, [1, 2, 3, 4, 5], index=2, horizontal=True, key=key)
        responses.append((it["dim"], float(val)))

    if show_details:
        st.markdown("<hr class='hr'/>", unsafe_allow_html=True)
        st.markdown("**영역 안내**")
        for d in DIMENSIONS:
            st.markdown(f"- {d['icon']} **{d['name']}**: {d['tone']}")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# Compute scores
# =========================================================
dim_scores = {d["key"]: [] for d in DIMENSIONS}
for dim, v in responses:
    dim_scores[dim].append(v)

dim_avg = {k: (sum(vs) / len(vs) if vs else 0.0) for k, vs in dim_scores.items()}
overall = sum(dim_avg.values()) / len(dim_avg) if dim_avg else 0.0

sorted_dims = sorted(dim_avg.items(), key=lambda x: x[1])
weakest = [k for k, _ in sorted_dims[:2]]
strongest = [k for k, _ in sorted(dim_avg.items(), key=lambda x: -x[1])[:2]]

lvl_name, lvl_icon, lvl_msg = level(overall)

dim_map = {d["key"]: d for d in DIMENSIONS}

# =========================================================
# Summary (right)
# =========================================================
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 결과 요약")

    st.markdown(
        f"""
<div class="kpi">
  <div class="kpiBox">
    <div class="kpiTitle">종합 수준</div>
    <div class="kpiValue">{lvl_icon} {lvl_name}</div>
  </div>
  <div class="kpiBox">
    <div class="kpiTitle">종합 점수(평균)</div>
    <div class="kpiValue">{overall:.2f} / 5.00</div>
  </div>
  <div class="kpiBox">
    <div class="kpiTitle">강점 TOP2</div>
    <div class="kpiValue">{dim_map[strongest[0]]['icon']} {dim_map[strongest[1]]['icon']}</div>
  </div>
  <div class="kpiBox">
    <div class="kpiTitle">개선 우선 TOP2</div>
    <div class="kpiValue">{dim_map[weakest[0]]['icon']} {dim_map[weakest[1]]['icon']}</div>
  </div>
</div>
<hr class="hr"/>
""",
        unsafe_allow_html=True,
    )

    st.markdown(f"<div class='small'>💬 {lvl_msg}</div>", unsafe_allow_html=True)
    st.markdown("<hr class='hr'/>", unsafe_allow_html=True)

    st.markdown("**영역별 점수**")
    for d in DIMENSIONS:
        s = dim_avg[d["key"]]
        st.progress(s / 5.0, text=f"{d['icon']} {d['name']} · {s:.2f}/5")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# Roadmap (tips -> courses -> extracurricular) VISUAL
# =========================================================
st.write("")
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown(
    """
<div class="sectionTitle">
  <h3 style="margin:0;">맞춤 로드맵(영역별 흐름)</h3>
  <span class="badge">개선 행동 → 교과 → 비교과</span>
</div>
<p class="small" style="margin-top:6px;">
점수가 낮은 영역은 <b>즉시 행동 팁</b>을 먼저 제시하고, 그 다음 <b>교과(정규)</b>와 <b>비교과(워크숍/클리닉)</b>를 이어서 추천합니다.
</p>
""",
    unsafe_allow_html=True,
)

# Choose which dims to show first: weakest first then others
ordered_dim_keys = weakest + [k for k, _ in sorted(dim_avg.items(), key=lambda x: x[1]) if k not in weakest]

lanes_html = "<div class='lanes'>"
for k in ordered_dim_keys:
    d = dim_map[k]
    s = dim_avg[k]
    b = band(s)
    tips = IMPROVEMENTS[k][b][:2]  # keep visually clean
    course = PROGRAMS[k]["course"][0] if PROGRAMS[k]["course"] else None
    extra = PROGRAMS[k]["extra"][0] if PROGRAMS[k]["extra"] else None

    priority_badge = "우선 개선" if k in weakest else "유지/고도화"
    lane = f"""
<div class="lane">
  <div class="laneHeader">
    <div>
      <div class="laneTitle">{d['icon']} {d['name']}</div>
      <div class="laneMeta">{d['tone']}</div>
    </div>
    <div style="text-align:right;">
      <div class="badge">점수 {s:.2f}/5</div>
      <div style="margin-top:6px;" class="badge">{priority_badge}</div>
    </div>
  </div>

  <div class="flow">
    <div class="step">
      <div class="stepTitle">① 개선 행동(바로 적용)</div>
      <div class="stepDesc">아래 2가지만 먼저 실행해도 점수 상승이 빨라요.</div>
      <div class="stepTags">
        {''.join([f'<span class="tag">• {t}</span>' for t in tips])}
      </div>
    </div>

    <div class="arrow">↓</div>

    <div class="step">
      <div class="stepTitle">② 교과 추천(정규)</div>
      <div class="stepDesc"><b>{course['title']}</b> · {course['hours']}<br/>{course['desc']}</div>
      <div class="stepTags">
        {''.join([f'<span class="tag">{x}</span>' for x in course['tags']])}
      </div>
    </div>

    <div class="arrow">↓</div>

    <div class="step">
      <div class="stepTitle">③ 비교과 추천(워크숍/클리닉)</div>
      <div class="stepDesc"><b>{extra['title']}</b> · {extra['hours']}<br/>{extra['desc']}</div>
      <div class="stepTags">
        {''.join([f'<span class="tag">{x}</span>' for x in extra['tags']])}
      </div>
    </div>
  </div>
</div>
"""
    lanes_html += lane

lanes_html += "</div>"

st.markdown(lanes_html, unsafe_allow_html=True)

st.markdown(
    """
<div class="small" style="margin-top:10px;">
💡 운영 팁: ‘비교과(짧은 실습) → 교과(체계적 학습) → 비교과(개인화 클리닉)’처럼 왕복 설계하면 학습 전이가 좋아요.
</div>
""",
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# Prioritized action plan (compact)
# =========================================================
st.write("")
colA, colB = st.columns([1, 1], gap="large")

with colA:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 우선 개선 TOP2: 2주 미니 플랜")
    st.caption("가볍게 시작해서 습관화하는 구성입니다.")

    for k in weakest:
        d = dim_map[k]
        s = dim_avg[k]
        tips = IMPROVEMENTS[k][band(s)]
        st.markdown(
            f"""
<div class="item">
  <b>{d['icon']} {d['name']}</b>
  <div class="small" style="margin-top:4px;">권장 루틴(2주):</div>
  <div style="margin-top:8px;">
    <span class="tag">1주차 · {tips[0]}</span>
    <span class="tag">2주차 · {tips[1]}</span>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

with colB:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 강점 TOP2: 유지·고도화 제안")
    st.caption("잘하는 영역은 ‘표준화’와 ‘재사용’으로 성과를 키워요.")

    for k in strongest:
        d = dim_map[k]
        s = dim_avg[k]
        hi = IMPROVEMENTS[k]["high"][0]
        st.markdown(
            f"""
<div class="item">
  <b>{d['icon']} {d['name']}</b>
  <div class="small" style="margin-top:6px;">{hi}</div>
  <div style="margin-top:8px;">
    <span class="tag">점수 {s:.2f}/5</span>
    <span class="tag">재사용/표준화</span>
  </div>
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# Download
# =========================================================
if show_download:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"AI 활용 역량 진단 결과 ({now})",
        f"- 종합: {lvl_name} ({overall:.2f}/5.00)",
        "",
        "[영역별 점수]",
    ]
    for d in DIMENSIONS:
        lines.append(f"- {d['name']}: {dim_avg[d['key']]:.2f}/5.00")

    lines.append("")
    lines.append("[개선 우선 TOP2]")
    for k in weakest:
        lines.append(f"- {dim_map[k]['name']}")

    lines.append("")
    lines.append("[영역별 로드맵 요약]")
    for k in ordered_dim_keys:
        d = dim_map[k]
        s = dim_avg[k]
        tips = IMPROVEMENTS[k][band(s)][:2]
        course = PROGRAMS[k]["course"][0]
        extra = PROGRAMS[k]["extra"][0]
        lines.append(f"\n- {d['name']} (점수 {s:.2f}/5)")
        lines.append(f"  · 개선 행동: {tips[0]} / {tips[1]}")
        lines.append(f"  · 교과: {course['title']} ({course['hours']})")
        lines.append(f"  · 비교과: {extra['title']} ({extra['hours']})")

    st.download_button(
        "결과 TXT 다운로드",
        data="\n".join(lines),
        file_name="ai_competency_roadmap_result.txt",
        mime="text/plain",
    )

st.markdown(
    "<div class='small' style='margin-top:14px;'>"
    "※ 본 도구는 교육적 진단/피드백 목적이며, 실제 과제 맥락·전공 특성·수업 규정을 함께 고려해 적용하는 것이 좋습니다."
    "</div>",
    unsafe_allow_html=True,
)
