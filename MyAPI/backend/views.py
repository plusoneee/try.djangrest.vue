from .models import Article as ArticleModel
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ArticleList(APIView):

    def get(self, request):
        articles = ArticleModel.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):

    def get_article(self, slug):
        try:
            article = ArticleModel.objects.get(slug=slug)
        except ArticleModel.DoesNotExist:
            return None
        return article

    def get(self, request, slug):
        article = self.get_article(slug)
        
        if article is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def delete(self, request, slug):
        article = self.get_article(slug)
        
        if article:
            article.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, slug):
        article = self.get_article(slug)
        
        if article is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ArticleSerializer(article, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)