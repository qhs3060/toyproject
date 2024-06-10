from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # CORS 미들웨어 가져오기
from sqlalchemy.orm import Session
from db import get_db
import crud, schemas, ml
import logging

app = FastAPI()

# CORS 설정
origins = [
    "http://localhost:3000",  # 프론트엔드가 실행되는 도메인
    "http://127.0.0.1:3000",  # 로컬 IP로 접근할 경우
    # 필요에 따라 다른 도메인도 추가 가능
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 특정 도메인을 허용
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드를 허용
    allow_headers=["*"],  # 모든 HTTP 헤더를 허용
)

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"message": "Hello, World, 20240607"}

@app.get("/train")
def train_model(db: Session = Depends(get_db)):
    try:
        california_data = crud.get_california_data(db)
        iris_data = crud.get_iris_data(db)
        if not california_data or not iris_data:
            raise HTTPException(status_code=404, detail="Table data not found")
        
        result = ml.train_and_predict(california_data, iris_data)
        return {"result": result}
    except Exception as e:
        logger.error(f"Error during training: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@app.get("/california/original")
def get_california_original_data(db: Session = Depends(get_db)):
    data = crud.get_california_original_data(db)
    if not data:
        raise HTTPException(status_code=404, detail="California House original data not found")
    return data

@app.get("/iris/original")
def get_iris_original_data(db: Session = Depends(get_db)):
    data = crud.get_iris_original_data(db)
    if not data:
        raise HTTPException(status_code=404, detail="Iris original data not found")
    return data

## 추후 frontend에 보낼 데이터 확정하기