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

## 🤖 GitHub Actions 자동화

이 프로젝트는 다음과 같은 GitHub Actions가 자동으로 실행됩니다:

### 📋 Pull Request (PR) 자동화

#### 1. 테스트 자동 실행 (`test.yml`)

- **트리거**: PR 생성/업데이트, main 브랜치 push
- **기능**:
  - Python 3.11 환경 설정
  - 의존성 설치 및 캐싱
  - 백엔드/프론트엔드 테스트 실행
  - 코드 커버리지 측정 및 업로드
  - 테스트 결과 PR 댓글 자동 등록

#### 2. PR 자동 댓글 (`pr-comment.yml`)

- **트리거**: PR 생성, 동기화, 재오픈
- **기능**:
  - PR 생성 시 환영 메시지 및 체크리스트 제공
  - PR 업데이트 시 알림 댓글 자동 등록
  - 개발 가이드라인 및 도움말 제공

#### 3. PR 자동 할당 (`pr-assigner.yml`)

- **트리거**: PR 생성, 리뷰 준비 완료
- **기능**:
  - 변경된 파일 분석하여 적절한 담당자 자동 할당
  - 백엔드/프론트엔드/문서/DevOps 영역별 할당
  - 할당 근거 및 정보 댓글 자동 등록

#### 4. PR 자동 라벨링 (`pr-labeler.yml`)

- **트리거**: PR 생성, 동기화, 편집
- **기능**:
  - 브랜치명, 제목, 내용 분석하여 자동 라벨링
  - 타입, 우선순위, 영역, 크기별 라벨 자동 적용
  - 기존 자동 라벨 업데이트 및 관리

#### 5. PR 코드 리뷰 자동화 (`pr-code-review.yml`)

- **트리거**: PR 생성, 동기화
- **기능**:
  - Black, isort, Flake8을 통한 코드 품질 검사
  - Bandit을 통한 보안 검사
  - Safety를 통한 종속성 보안 검사
  - 코드 복잡도 분석 및 개선 제안
  - 자동 코드 리뷰 댓글 등록

### 🐛 Issue 자동화

#### 6. 이슈 자동 댓글 (`issue-comment.yml`)

- **트리거**: 이슈 생성, 재오픈, 라벨링
- **기능**:
  - 이슈 생성 시 환영 메시지 및 처리 과정 안내
  - 이슈 재오픈 시 알림 및 다음 단계 안내
  - 우선순위/타입 라벨링 시 상세 정보 제공

#### 7. 이슈 자동 할당 (`issue-assigner.yml`)

- **트리거**: 이슈 생성, 라벨링
- **기능**:
  - 키워드 및 라벨 분석하여 담당자 자동 할당
  - 긴급 이슈 시 프로젝트 리드 추가 할당
  - 할당 근거 및 담당자 역할 안내

#### 8. 이슈 자동 라벨링 (`issue-labeler.yml`)

- **트리거**: 이슈 생성, 편집
- **기능**:
  - 제목/내용 키워드 분석하여 자동 라벨링
  - 타입, 우선순위, 영역, 플랫폼별 라벨 적용
  - 라벨링 결과 상세 정보 제공

## 🏷️ 라벨 시스템

### PR 라벨

- **타입**: `type: feature`, `type: bugfix`, `type: hotfix`, `type: refactor`, `type: docs`
- **우선순위**: `priority: high`, `priority: medium`, `priority: low`
- **영역**: `area: backend`, `area: frontend`, `area: documentation`, `area: testing`, `area: ci-cd`
- **크기**: `size: small`, `size: medium`, `size: large`
- **상태**: `status: draft`, `status: in-review`, `status: ready-to-merge`

### Issue 라벨

- **타입**: `type: bug`, `type: feature`, `type: enhancement`, `type: question`, `type: documentation`
- **우선순위**: `priority: critical`, `priority: high`, `priority: medium`, `priority: low`
- **영역**: `area: backend`, `area: frontend`, `area: documentation`, `area: testing`, `area: ci-cd`
- **상태**: `status: triage`, `status: in-progress`, `status: blocked`, `status: duplicate`
- **플랫폼**: `platform: windows`, `platform: macos`, `platform: linux`
- **특별**: `help wanted`, `good first issue`

## 🔧 개발 워크플로우

### 1. 이슈 생성

```bash
# 이슈 생성 시 자동으로:
# - 라벨링 (타입, 우선순위, 영역 등)
# - 담당자 할당
# - 환영 댓글 및 가이드 제공
```

### 2. 브랜치 생성 및 개발

```bash
# 브랜치 네이밍 규칙
git checkout -b feature/TASK-001-implement-chat-api
git checkout -b bugfix/TASK-002-fix-login-error
git checkout -b hotfix/TASK-003-security-patch
```

### 3. Pull Request 생성

```bash
# PR 생성 시 자동으로:
# - 라벨링 (브랜치명, 제목, 내용 분석)
# - 담당자 및 리뷰어 할당
# - 환영 댓글 및 체크리스트 제공
# - 코드 품질 검사 실행
```

### 4. 코드 리뷰 및 머지

```bash
# 자동 검사 항목:
# - 테스트 실행 및 커버리지 측정
# - 코드 포맷팅 (Black, isort)
# - 린팅 (Flake8)
# - 보안 검사 (Bandit, Safety)
# - 코드 복잡도 분석
```

## 📝 개발 규칙

프로젝트의 상세한 개발 규칙은 `.cursor/rules/` 디렉토리에서 확인할 수 있습니다:

- **github-management.mdc**: GitHub PR/이슈 관리 규칙
- **tech-stack.mdc**: 기술 스택 정보
- **development-tasks.mdc**: 개발 태스크 관리
- **project-structure.mdc**: 프로젝트 구조 가이드

## 🚀 시작하기

### 1. 환경 설정

```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

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

## 🤝 기여하기

1. 이슈를 생성하여 작업 내용을 공유해주세요
2. 적절한 브랜치명으로 개발 브랜치를 생성해주세요
3. 코드 작성 후 PR을 생성해주세요
4. 자동 검사를 통과하고 리뷰를 받은 후 머지됩니다

## 📞 도움이 필요하시나요?

- 🐛 **버그 리포트**: [Issues](../../issues)에서 버그를 신고해주세요
- ✨ **기능 요청**: [Issues](../../issues)에서 새로운 기능을 제안해주세요
- ❓ **질문**: [Discussions](../../discussions)에서 질문해주세요

---

_이 프로젝트는 GitHub Actions를 통해 자동화된 개발 워크플로우를 제공합니다._
