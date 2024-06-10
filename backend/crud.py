from sqlalchemy.orm import Session
import models

def get_california_data(db: Session):
    return db.query(models.CaliforniaHouse).all()

def get_iris_data(db: Session):
    return db.query(models.Iris).all()

def get_california_original_data(db: Session):
    return [item.as_dict() for item in db.query(models.CaliforniaHouse).all()]

def get_iris_original_data(db: Session):
    return [item.as_dict() for item in db.query(models.Iris).all()]