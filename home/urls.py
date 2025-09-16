from django.urls import path
from home import views

urlpatterns = [
    # 홈 랜더
    path("", views.home, name="home"),
    # 크롤링 요청
    path("craw/", views.crawling, name="crawling"),
    
]
