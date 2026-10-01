# Python_project-fastapi

본 리포지토리는 인프런(Inflearn) 강의 <**실전! FastAPI 입문**>을 수강하며 진행한 백엔드 API 서버 실습 코드를 담고 있습니다.

## 프로젝트 소개
- FastAPI의 핵심 개념과 동작 원리를 익히고, 실무에서 사용하는 백엔드 아키텍처를 점진적으로 구축하는 실습 프로젝트입니다.
- 초기에는 메모리(Mock Data) 기반의 간단한 라우팅으로 시작하여, 데이터베이스 연동, 아키텍처 패턴 적용, 테스트 코드 작성 등 점진적 리팩토링(Refactoring) 과정을 거쳐 발전해 온 코드베이스입니다.

---

## 지금까지의 상세 구현 내용 (히스토리)

### 1. API 라우팅 및 CRUD 완벽 구현
- **ToDo 도메인 (`api/todo.py`):** 할 일(ToDo) 항목에 대한 **생성(Create), 단일/전체 조회(Read), 수정(Update - 상태 변경), 삭제(Delete)** API를 모두 구현했습니다.
- **User 도메인 (`api/user.py`):** 사용자 회원가입(`sign-up`) API를 구현했습니다.
- **모듈화 (APIRouter):** `main.py`에 모든 엔드포인트가 집중되어 있던 구조를 벗어나 도메인별(Todo, User)로 라우터를 분리하여 응집도를 높였습니다.

### 2. 데이터베이스 모델링 및 ORM 연동 (SQLAlchemy)
- **User & ToDo 1:N 관계:** 사용자와 할 일이 1대 다(1:N) 관계를 가지도록 `ForeignKey`를 매핑하고 `relationship(lazy="joined")`을 설정했습니다 (`database/orm.py`).
- **ORM 메서드 활용:** `@classmethod`를 활용한 팩토리 패턴(Factory pattern)으로 객체 생성을 깔끔하게 처리하도록 구현했습니다.

### 3. 비즈니스 로직 및 아키텍처 계층 분리
- **Repository 패턴 (`database/repository.py`):** 
  - DB에 직접 접근하는 로직을 분리하여 `ToDoRepository` 및 `UserRepository` 클래스로 추상화했습니다. 
  - `Depends()`를 통한 **의존성 주입(Dependency Injection)** 구조를 확립했습니다.
- **Service 계층 분리 (`service/user.py`):** 
  - 패스워드 해싱(`bcrypt` 라이브러리 사용)과 같은 핵심 비즈니스 로직을 API 엔드포인트에서 분리해 `UserService`로 모듈화했습니다.
- **Pydantic 스키마 (`schema/request.py`, `schema/response.py`):** 
  - 클라이언트로부터 전달받는 Request 데이터 검증, 그리고 서버가 응답하는 Response 직렬화를 엄격한 타입 시스템으로 통제하도록 구현했습니다 (`orm_mode` 활성화).

### 4. 테스트 코드 (Pytest & Mocking)
- **도메인별 테스트 분리:** `tests/test_todos_api.py`와 `tests/test_users_api.py`로 도메인별 테스트를 분리하여 관리합니다.
- **단위 테스트 (Unit Test):** `mocker.patch.object`를 사용하여 실제 DB에 의존하지 않고 Repository 및 Service 계층을 모킹(Mocking)함으로써 API 엔드포인트 자체의 로직을 독립적으로 검증합니다.
- **Fixture 적용:** `conftest.py`에 `TestClient`를 픽스처로 등록해 모든 테스트에서 재사용 가능하게 구성했습니다.

---

## 기술 스택
- **Language:** Python 3
- **Framework:** FastAPI
- **Database:** SQLAlchemy (ORM), PyMySQL
- **Security:** bcrypt (비밀번호 단방향 암호화)
- **Testing:** Pytest, pytest-mock
- **Server:** Uvicorn
- **Tools:** Docker, PyCharm, MySQL

## 실행 방법

### 1. 가상 환경 설정 및 패키지 설치
```bash
# 가상 환경 생성
python -m venv venv

# 가상 환경 활성화 (Windows)
.\venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt
```

### 2. 서버 실행
```bash
# src 디렉토리 내의 main.py의 app 인스턴스 실행
uvicorn src.main:app --reload
```
