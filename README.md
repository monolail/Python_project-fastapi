# Python_project-fastapi

본 리포지토리는 인프런(Inflearn) 강의 **<실전! FastAPI 입문>**을 수강하며 진행한 실습 코드를 담고 있습니다.

## 📌 프로젝트 소개
- FastAPI의 기본 개념과 활용법을 익히기 위한 실습 프로젝트입니다.
- 라우팅, 데이터베이스 연동(SQLAlchemy), Pydantic을 활용한 데이터 검증 등의 실습 내용이 포함되어 있습니다.

## 🛠 기술 스택
- **Language:** Python 3
- **Framework:** FastAPI
- **Database:** SQLAlchemy (ORM), PyMySQL
- **Server:** Uvicorn

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