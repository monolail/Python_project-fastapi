# Python_project-fastapi

본 리포지토리는 인프런(Inflearn) 강의 **<실전! FastAPI 입문>**을 수강하며 진행한 실습 코드를 담고 있습니다.

## 📌 프로젝트 소개
- FastAPI의 기본 개념과 활용법을 익히기 위한 실습 프로젝트입니다.
- 초기 Mock Data를 활용한 API에서 시작하여, 실제 데이터베이스 연동 및 아키텍처 패턴을 적용하는 과정이 담겨 있습니다.

## 🌟 주요 구현 내용
- **CRUD API 구현:** ToDo 생성, 조회, 수정, 삭제 API 구현
- **데이터베이스 연동:** SQLAlchemy ORM을 활용한 데이터베이스 모델링 및 쿼리
- **Repository 패턴 적용:** 데이터 접근 계층(Repository)과 비즈니스 로직(API)의 분리 (`repository.py`)
- **Pydantic 스키마 활용:** Request 및 Response 데이터의 타입 검증 및 직렬화 (`schema` 디렉토리)
- **테스트 코드 작성:** Pytest와 FastAPI TestClient를 활용한 전체 CRUD API 유닛 테스트 구현 (Mocking 및 `conftest.py` 픽스처 적용)

## 🛠 기술 스택
- **Language:** Python 3
- **Framework:** FastAPI
- **Database:** SQLAlchemy (ORM), PyMySQL
- **Server:** Uvicorn
- **Testing:** Pytest

## 🚀 실행 방법

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
# src 디렉토리의 main.py 내 app 객체를 실행
uvicorn src.main:app --reload
```