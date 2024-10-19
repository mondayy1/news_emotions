from fastapi import APIRouter
from api.utils.news_crawler import *
from api.utils.model import *

router = APIRouter()

@router.get("/api/news/korean")
def korean_news():
    news = get_korean_news()
    emotions = get_emotions(news['title'], news['content'])
    return {"korean_news": news, "emotions": emotions}