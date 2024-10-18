from fastapi import APIRouter
from app.utils.news_crawler import *
from app.utils.model import *

router = APIRouter()

"""
@router.get("/news/korean")
def korean_news():
    news = get_korean_news()
    return {"korean_news": news}

@router.get("/news/international")
def international_news():
    news = get_international_news()
    return {"international_news": news}
    """
