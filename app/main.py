from doc import views
from fastapi import FastAPI, APIRouter
router = APIRouter
import routers

app = FastAPI()
app.include_router(routers.router, prefix='/api')
