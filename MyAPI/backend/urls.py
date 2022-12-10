from django.urls import path, include

''' for APIView version '''
# from .views import ArticleList, ArticleDetails

from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [

    path('', include(router.urls))
    # for APIView version 
    # path('articles/', ArticleList.as_view()),
    # path('articles/<slug:slug>/', ArticleDetails.as_view()),
]