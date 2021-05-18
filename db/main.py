from fastapi import FastAPI, Request, status, Response, Depends
import models
from database import get_db
from sqlalchemy.orm import Session
import crud
import uvicorn

app = FastAPI()


@app.get("/")
async def root(db: Session = Depends(get_db)):
    blog = db.query(models.Shipper).all()
    return blog


@app.get("/suppliers")
async def suppliers(db: Session = Depends(get_db)):
    return crud.get_suppliers(db)


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)
