from fastapi import FastAPI
from app.database import Base, engine
from app.models.user import User
from app.routers.users import router as users_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users_router)

@app.get("/health")
def health():
    return {"status": "ok"}
