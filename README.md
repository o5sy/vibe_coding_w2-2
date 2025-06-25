# Vibe Coding W2-2 Project

FastAPI + Streamlit 기반의 LangGraph Agent 프로젝트입니다.

## 🏗️ 프로젝트 구조

```
vibe_coding_w2-2/
├── backend/                           # FastAPI 백엔드
│   ├── main.py                        # FastAPI 애플리케이션 엔트리포인트
│   ├── requirements.txt               # Python 의존성
│   └── app/
│       ├── api/                       # API Layer
│       ├── services/                  # Service Layer
│       └── agents/                    # Agent Layer (LangGraph)
├── frontend/                          # Streamlit 프론트엔드
├── docs/                              # 프로젝트 문서
├── .github/workflows/                 # GitHub Actions
└── .cursor/rules/                     # 개발 규칙
```

## 🚀 기술 스택

### 백엔드

- **FastAPI**: 웹 프레임워크
- **LangGraph**: React Agent 구현
- **Gemini-2.5-flash**: LLM 모델
- **DuckDuckGo Search**: 웹 검색 도구

### 프론트엔드

- **Streamlit**: 챗봇 UI 구현

### 개발 환경

- **Python 3.11**
- **GitHub Actions**: CI/CD 자동화
- **LangSmith**: Agent 모니터링

## 🚀 시작하기

### 1. 환경 설정

```bash
# 가상환경 생성
python -m venv venv

# 의존성 설치
pip install -r backend/requirements.txt
```

### 2. 환경 변수 설정

```bash
# .env 파일 생성
cp .env.example .env

# 필요한 환경 변수 설정
LANGSMITH_API_KEY=your_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. 개발 서버 실행

```bash
# 백엔드 서버 실행
cd backend
uvicorn main:app --reload

# 프론트엔드 실행 (별도 터미널)
cd frontend
streamlit run app.py
```
