# Multi-Agent 기반 제안요청서(RFP) 분석 및 제안서 평가 지원 시스템

RFP(PDF)와 제안서 텍스트를 입력하면, **요구사항 추출 → 제안서 컴플라이언스 대조 → 취약점/예상 Q&A 생성**까지 한 번에 수행하는 **Multi-Agent(crewAI) 기반 분석 파이프라인**입니다.

이 레포지토리는 원본 Notebook 구현을 **스크립트 형태로 정리**하여, 포트폴리오로 바로 사용할 수 있게 구성했습니다.

---

## ✅ 무엇을 해결하나요?

- RFP 해석/정리 시간을 줄이고 요구사항 누락을 방지
- 제안서 초안이 RFP 요구사항을 충족하는지 자동 점검(O/△/X)
- 최종 발표(PT)에서 공격받기 쉬운 취약점을 미리 도출하고 Q&A까지 준비

---

## 🧠 구성 요소

### 1) Multi-Agent (crewAI)
- **Extractor Agent**: RFP에서 요구사항을 테이블로 구조화
- **Matcher Agent**: 요구사항 vs 제안서 비교하여 O/△/X 판정 + 근거 위치
- **Reviewer Agent**: 취약점 3가지 + 예상 질문/답변(Q&A) 생성

---

## 📦 산출물(자동 생성)

실행이 끝나면 아래 파일들이 생성됩니다.
 
1. `1_요구사항_체크리스트.csv` 
2. `2_일치_여부_보고서.csv`
3. `3_최종_전략_리포트.txt`

---

## 🚀 실행 방법

> OpenAI API Key가 필요합니다.

### 1) 설치
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) 환경 변수 설정
```bash
export OPENAI_API_KEY="YOUR_KEY"
```

### 3) 실행
```bash
python main.py --rfp example_rfp_배관관리.pdf --proposal proposal.txt
```

- `--proposal`을 생략하면 `main.py` 내부의 테스트용 제안서 문자열을 사용합니다.

---

## 🧾 입력 파일

- `--rfp`: RFP PDF 경로 (예: `example_rfp_배관관리.pdf`)
- `--proposal`: 제안서 초안 텍스트 파일 경로(선택)

---

## 📁 프로젝트 구조

```
.
├── main.py
├── requirements.txt
├── proposal.txt                # (선택) 제안서 입력 텍스트
├── rfp.pdf    # (사용자가 준비)
└── (실행 후 생성)
    ├── 1_요구사항_체크리스트.md
    ├── 1_요구사항_체크리스트.csv
    ├── 2_일치_여부_보고서.md
    ├── 2_일치_여부_보고서.csv
    └── 3_최종_전략_리포트.txt
```

---

## 👥 Contributors
- 배은서
- 한채윤
