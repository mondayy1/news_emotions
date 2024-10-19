from fastapi import APIRouter
from api.utils.news_crawler import *
from api.utils.model import *
from api.utils.word_cloud import *

router = APIRouter()

@router.get("/api/news/korean")
def news_korean_emotions():
    news = get_korean_news()
    emotions = get_emotions(news['title'], news['content'])
    wordcount = get_wordcount(news['title'], news['content'])
    return {"korean_news": news, "emotions": emotions, "wordcount": wordcount}
    