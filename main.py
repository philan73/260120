import streamlit as st
from datetime import datetime

# -----------------------------
# Page
# -----------------------------
st.set_page_config(
    page_title="AI 활용 역량 진단 · 맞춤 교육 추천",
    page_icon="🫧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Pastel UI CSS
# -----------------------------
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
  --mint:#bfeee3;
  --lav:#d9d7ff;
  --peach:#ffd6cc;
  --sky:#cfe6ff;
  --rose:#ffd3ea;
  --accent:#7aa7ff;
}

.stApp{
  background:
    radial-gradient(900px 520px at 15% 5%, rgba(217,215,255,.55), transparent 60%),
    radial-gradient(820px 520px at 88% 12%, rgba(191,238,227,.55), transparent 58%),
    radial-gradient(900px 520px at 55% 98%, rgba(255,214,204,.45), transparent 62%),
    linear-gradient(180deg, var(--bg1), var(--bg2));
  color: var(--txt);
}
.block-container{ padding-top: 1.2rem !important; padding-bottom: 2.2rem !important; max-width: 1200px;}
h1,h2,h3,h4, p, span, label, div { color: var(--txt); }

.hero{
  border: 1px solid var(--stroke);
  background: linear-gradient(135deg, rgba(255,255,255,.80), rgba(255,255,255,.68));
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
    radial-gradient(520px 220px at 0% 0%, rgba(207,230,255,.75), transparent 60%),
    radial-gradient(520px 220px at 100% 0%, rgba(255,211,234,.60), transparent 62%),
    radial-gradient(520px 220px at 50% 120%, rgba(191,238,227,.55), transparent 62%);
  pointer-events:none;
}
.pillRow{ display:flex; flex-wrap:wrap; gap:8px; margin-top: 10px;}
.pill{
  display:inline-flex; align-items:center; gap:8px;
  padding: 7px 10px;
  border-radius: 999px;
  border: 1px solid var(--stroke);
  background: rgba(255,255,255,.68);
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
.kpi{
  display:flex; gap:12px; flex-wrap:wrap;
}
.kpiBox{
  flex: 1 1 170px;
  border:1px solid var(--stroke);
  border-radius: 16px;
  padding: 12px 14px;
  background: rgba(255,255,255,.68);
  box-shadow: var(--shadow2);
}
.kpiTitle{ color: var(--muted); font-size: .85rem; margin-bottom: 2px;}
.kpiValue{ font-size: 1.18rem; font-weight: 700; }
.hr{
  height:1px;
  background: linear-gradient(90deg, transparent, rgba(30,60,90,.14), transparent);
  margin: 14px 0;
  border:0;
}
.item{
  border: 1px solid var(--stroke);
  background: rgba(255,255,255,.62);
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
  background: rgba(255,255,255,.70);
  color: var(--muted);
  font-size: .86rem;
}
.note{
  border: 1px dashed rgba(30,60,90,.22);
  background: rgba(255,255,255,.55);
  border-radius: 16px;
  padding: 12px 14px;
  color: var(--muted);
}
.stButton>button{
  border-radius: 999px !important;
  border: 1px solid rgba(30,60,90,.16) !important;
  background: linear-gradient(135deg, rgba(122,167,255,.55), rgba(191,238,227,.75)) !important;
  color: #16324a !important;
  box-shadow: var(--shadow2);
  padding: .62rem 1.05rem !important;
}
.stDownloadButton>button{
  border-radius: 999px !important;
  border: 1px solid rgba(30,60,90,.16) !important;
  background: linear-gradient(135deg, rgba(255,211,234,.78), rgba(217,215,255,.72)) !important;
  color: #16324a !important;
  box-shadow: var(--shadow2);
}
</style>
""",
    unsafe_allow_html=True,
)

# -----------------------------
# Model: competencies & recommendations
# -----------------------------
COMPETENCIES = [
    {
        "key": "problem",
        "name": "문제정의 & 목표설정",
        "icon": "🧭",
        "desc": "과제의 목적·제약·평가기준을 명확히 하고, AI에 맡길 범위를 구분하는 역량",
        "low_fix": [
            "과제 목표를 1문장으로 재정의(누구에게/무엇을/왜/어떤 제약)하기",
            "평가기준(정확성·근거·표현·윤리)을 미리 체크리스트로 만들기",
        ],
        "mid_fix": [
            "입력 자료·맥락·용어 정의를 먼저 정리한 뒤 프롬프트 작성하기",
            "산출물 형식(표/요약/보고서)과 길이·톤을 사전에 고정하기",
        ],
        "high_fix": [
            "여러 접근법(비교안)과 의사결정 기준을 세워 A/B로 검토하기",
            "업무 흐름에 맞춘 템플릿(요청서/평가기준)을 만들고 재사용하기",
        ],
    },
    {
        "key": "prompt",
        "name": "프롬프트 설계 & 대화전략",
        "icon": "✍️",
        "desc": "명확한 지시·역할·맥락·출력 조건으로 원하는 결과를 안정적으로 얻는 역량",
        "low_fix": [
            "‘역할-목표-자료-제약-출력형식’ 5요소 템플릿으로 요청하기",
            "한 번에 큰 요청 대신, 단계(초안→검토→개선)로 나누기",
        ],
        "mid_fix": [
            "샘플(좋은/나쁜 예시)을 함께 제공해 출력 품질을 고정하기",
            "검증 질문(근거/가정/불확실성)을 자동으로 포함시키기",
        ],
        "high_fix": [
            "반복 작업은 프롬프트 라이브러리(카드/노션/문서)로 축적하기",
            "작업 유형별 프롬프트(요약/비교/루브릭/코드) 템플릿 표준화하기",
        ],
    },
    {
        "key": "verify",
        "name": "검증 & 근거 기반 사고",
        "icon": "🔎",
        "desc": "AI 결과의 사실성·논리·출처를 점검하고, 오류를 수정·보완하는 역량",
        "low_fix": [
            "핵심 주장 3개를 뽑아 ‘근거가 있는지’부터 확인하기",
            "수치/인용/정책 같은 고위험 정보는 원문 출처 확인하기",
        ],
        "mid_fix": [
            "‘가정-근거-반례’ 질문으로 결과를 재검토하게 하기",
            "자기 평가 루브릭(정확·명확·근거·윤리)을 적용해 수정하기",
        ],
        "high_fix": [
            "검증 체크리스트를 자동화(항목화)해 매번 동일 기준 적용하기",
            "다른 모델/자료로 교차검증하거나, 상반된 관점 비교하기",
        ],
    },
    {
        "key": "ethics",
        "name": "학습윤리 & 책임 있는 활용",
        "icon": "🫧",
        "desc": "표절·허위·저작권·개인정보를 고려하고, 본인 기여를 투명하게 관리하는 역량",
        "low_fix": [
            "AI 사용 범위(초안/교정/아이디어)를 과제에 투명하게 표시하기",
            "개인정보/민감정보는 입력하지 않기(익명화/요약) 습관화하기",
        ],
        "mid_fix": [
            "인용·참고문헌 규칙을 적용하고, ‘AI가 만든 문장’ 그대로 제출하지 않기",
            "학습 목적이면 ‘내 문장으로 재구성’ 단계를 반드시 넣기",
        ],
        "high_fix": [
            "과정 로그(질문-수정-근거)를 남겨 기여도와 학습을 증빙하기",
            "저작권/라이선스(이미지·데이터) 체크 루틴을 운영하기",
        ],
    },
    {
        "key": "workflow",
        "name": "도구 활용 & 학습 워크플로우",
        "icon": "🧩",
        "desc": "AI를 조사·정리·작성·피드백 루프에 통합해 생산성과 학습효과를 높이는 역량",
        "low_fix": [
            "작업을 ‘자료수집→초안→검토→개선’ 4단계로 분해해 AI를 배치하기",
            "결과물을 ‘표/목차/요약’으로 먼저 뽑고, 나중에 문장화하기",
        ],
        "mid_fix": [
            "노트/문서 템플릿으로 반복 작업 시간을 줄이기",
            "과제별 체크리스트(마감·형식·루브릭)를 붙여 관리하기",
        ],
        "high_fix": [
            "나만의 워크플로우(프롬프트+체크리스트+템플릿) 묶음 만들기",
            "팀 작업에서는 역할/기여/버전 관리를 체계화하기",
        ],
    },
]

PROGRAM_LIBRARY = {
    "foundation": [
        ("AI 활용 기초: 좋은 질문 만들기", "1.5h", ["문제정의", "프롬프트"], "입력-출력 구조 이해, 템플릿 실습"),
        ("학습윤리 & 저작권/표절 예방", "1h", ["윤리"], "AI 활용 범위 표기, 인용 규칙, 사례 기반"),
        ("AI 결과 검증 입문", "1h", ["검증"], "사실/논리/출처 점검 루틴 만들기"),
    ],
    "practice": [
        ("프롬프트 스튜디오: 과제 유형별 템플릿", "2h", ["프롬프트", "워크플로우"], "요약/비교/보고서/루브릭 템플릿 제작"),
        ("리서치 워크플로우: 자료→초안→개선", "2h", ["워크플로우", "검증"], "근거 정리표, 체크리스트, 재작성"),
        ("AI와 협업 글쓰기(내 문장으로 재구성)", "2h", ["윤리", "프롬프트"], "초안 생성→근거→재구성 훈련"),
    ],
    "advanced": [
        ("평가 루브릭으로 품질 고도화", "2h", ["검증", "문제정의"], "루브릭 기반 자기평가/개선"),
        ("팀 프로젝트: AI 활용 로그 & 기여도 관리", "2h", ["윤리", "워크플로우"], "기여도 기록, 버전 관리, 역할 설계"),
        ("캡스톤: 나만의 AI 학습 시스템 만들기", "3h", ["워크플로우", "프롬프트", "검증"], "개인 템플릿/체크리스트 패키징"),
    ],
}

def level_from_score(avg):
    if avg < 2.4:
        return "기초", "🌱"
    elif avg < 3.6:
        return "중간", "🌿"
    else:
        return "심화", "🌟"

def pick_programs(avg, weakest_keys):
    # 기본: 수준별 1~2개 + 약점 영역 보완 1개
    foundation = PROGRAM_LIBRARY["foundation"][:]
    practice = PROGRAM_LIBRARY["practice"][:]
    advanced = PROGRAM_LIBRARY["advanced"][:]

    if avg < 2.4:
        base = [foundation[0], foundation[2], foundation[1]]
        extra = practice[0]
    elif avg < 3.6:
        base = [practice[1], practice[0], foundation[1]]
        extra = advanced[0]
    else:
        base = [advanced[2], advanced[0], advanced[1]]
        extra = practice[1]

    # 약점 키 기반으로 한 개 더 맞춤
    tag_map = {
        "problem": "문제정의",
        "prompt": "프롬프트",
        "verify": "검증",
        "ethics": "윤리",
        "workflow": "워크플로우",
    }
    targets = [tag_map[k] for k in weakest_keys]
    all_programs = foundation + practice + advanced

    tailored = None
    for p in all_programs:
        if any(t in p[2] for t in targets):
            tailored = p
            break

    recs = base[:]
    if tailored and tailored not in recs:
        recs.append(tailored)
    if extra and extra not in recs:
        recs.append(extra)

    # 최대 4개
    return recs[:4]

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown("### 설정")
    st.caption("파스텔톤 UI · 대학생 AI 활용 역량 진단")
    st.markdown("---")
    mode = st.radio("진단 방식", ["자가진단(슬라이더)", "간단 설문(라디오)"], index=0)
    st.markdown("---")
    st.markdown("**출력 옵션**")
    show_tips = st.checkbox("개선 팁 보기", value=True)
    show_programs = st.checkbox("교육 프로그램 추천 보기", value=True)
    show_download = st.checkbox("결과 다운로드", value=True)

# -----------------------------
# Hero
# -----------------------------
st.markdown(
    """
<div class="hero">
  <h1>AI 활용 역량 진단 · 맞춤 교육 추천</h1>
  <p class="small" style="margin-top:6px;">
    🫧 대학생이 AI를 <b>잘, 그리고 책임 있게</b> 활용하도록 돕는 진로·학습 지원 도구입니다.
    5개 영역을 진단하고, 결과에 따라 개선 방향과 추천 프로그램을 제안합니다.
  </p>
  <div class="pillRow">
    <span class="pill">🧭 문제정의</span>
    <span class="pill">✍️ 프롬프트</span>
    <span class="pill">🔎 검증</span>
    <span class="pill">🫧 윤리</span>
    <span class="pill">🧩 워크플로우</span>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

# -----------------------------
# Inputs
# -----------------------------
scores = {}
left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 진단 문항")
    st.caption("각 항목은 1(아직 어려움) ~ 5(매우 능숙) 기준으로 응답하세요.")

    for c in COMPETENCIES:
        if mode == "자가진단(슬라이더)":
            val = st.slider(
                f"{c['icon']} {c['name']}",
                min_value=1,
                max_value=5,
                value=3,
                help=c["desc"],
                key=c["key"],
            )
        else:
            val = st.radio(
                f"{c['icon']} {c['name']}",
                options=[1, 2, 3, 4, 5],
                index=2,
                horizontal=True,
                help=c["desc"],
                key=c["key"],
            )
        scores[c["key"]] = float(val)

    st.markdown("</div>", unsafe_allow_html=True)

with right:
    # Compute results
    avg = sum(scores.values()) / len(scores)
    lvl, lvl_icon = level_from_score(avg)

    # Rank
    sorted_items = sorted(scores.items(), key=lambda x: x[1])
    weakest = [k for k, _ in sorted_items[:2]]
    strongest = [k for k, _ in sorted(scores.items(), key=lambda x: -x[1])[:2]]

    key_to_name = {c["key"]: c["name"] for c in COMPETENCIES}
    key_to_icon = {c["key"]: c["icon"] for c in COMPETENCIES}
    programs = pick_programs(avg, weakest)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 결과 요약")
    st.markdown(
        f"""
<div class="kpi">
  <div class="kpiBox">
    <div class="kpiTitle">종합 수준</div>
    <div class="kpiValue">{lvl_icon} {lvl}</div>
  </div>
  <div class="kpiBox">
    <div class="kpiTitle">종합 점수(평균)</div>
    <div class="kpiValue">{avg:.2f} / 5.00</div>
  </div>
  <div class="kpiBox">
    <div class="kpiTitle">강점 TOP2</div>
    <div class="kpiValue">{key_to_icon[strongest[0]]} {key_to_icon[strongest[1]]}</div>
  </div>
  <div class="kpiBox">
    <div class="kpiTitle">개선 우선 TOP2</div>
    <div class="kpiValue">{key_to_icon[weakest[0]]} {key_to_icon[weakest[1]]}</div>
  </div>
</div>
<hr class="hr"/>
""",
        unsafe_allow_html=True,
    )

    st.markdown("**영역별 점수**")
    for c in COMPETENCIES:
        st.progress(scores[c["key"]] / 5.0, text=f"{c['icon']} {c['name']} · {scores[c['key']]:.0f}/5")

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Recommendations
# -----------------------------
st.write("")
colA, colB = st.columns([1, 1], gap="large")

with colA:
    if show_tips:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 개선 방향 (우선순위 기반)")
        st.caption("점수가 낮은 영역부터 ‘바로 적용 가능한’ 행동 팁을 제안합니다.")

        for k in weakest:
            c = next(x for x in COMPETENCIES if x["key"] == k)
            s = scores[k]
            if s <= 2:
                tips = c["low_fix"]
            elif s <= 3:
                tips = c["mid_fix"]
            else:
                tips = c["high_fix"]

            st.markdown(
                f"""
<div class="item">
  <b>{c["icon"]} {c["name"]}</b>
  <div class="small" style="margin-top:4px;">{c["desc"]}</div>
  <div style="margin-top:8px;">
    {''.join([f'<span class="tag">• {t}</span>' for t in tips])}
  </div>
</div>
""",
                unsafe_allow_html=True,
            )

        st.markdown(
            """
<div class="note">
  <b>짧은 루틴 추천</b><br/>
  ① 과제 목표 1문장 → ② 프롬프트(5요소) → ③ 결과 검증(근거/가정/반례) → ④ 내 문장으로 재작성 → ⑤ AI 활용 범위 기록
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown("</div>", unsafe_allow_html=True)

with colB:
    if show_programs:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 맞춤 교육 프로그램 추천")
        st.caption("수준 + 약점 영역을 반영한 추천입니다. (교내 비교과/워크숍 형태로 구성 가능)")

        for (title, duration, tags, desc) in programs:
            tag_str = " · ".join(tags)
            st.markdown(
                f"""
<div class="item">
  <b>🎓 {title}</b>
  <div class="small" style="margin-top:4px;">⏱️ {duration} · 🧩 {tag_str}</div>
  <div class="small" style="margin-top:6px;">{desc}</div>
</div>
""",
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Download
# -----------------------------
if show_download:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"AI 활용 역량 진단 결과 ({now})",
        f"- 종합 수준: {lvl} ({avg:.2f}/5.00)",
        "",
        "[영역별 점수]",
    ]
    for c in COMPETENCIES:
        lines.append(f"- {c['name']}: {scores[c['key']]:.0f}/5")

    lines.append("")
    lines.append("[강점 TOP2]")
    for k in strongest:
        lines.append(f"- {key_to_name[k]}")

    lines.append("")
    lines.append("[개선 우선 TOP2]")
    for k in weakest:
        lines.append(f"- {key_to_name[k]}")

    lines.append("")
    lines.append("[추천 프로그램]")
    for (title, duration, tags, desc) in programs:
        lines.append(f"- {title} ({duration}) / 태그: {', '.join(tags)} / {desc}")

    st.download_button(
        "결과 TXT 다운로드",
        data="\n".join(lines),
        file_name="ai_skill_diagnosis_result.txt",
        mime="text/plain",
    )

st.markdown(
    "<div class='small' style='margin-top:14px;'>"
    "※ 본 도구는 교육적 진단/피드백 목적이며, 개인차와 과제 맥락을 함께 고려하는 것이 좋습니다."
    "</div>",
    unsafe_allow_html=True,
)
