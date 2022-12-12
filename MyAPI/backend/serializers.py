from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        ''' with model serializer
        we dont need define every field in class'''

        model = Article
        fields = '__all__'

    slug = serializers.SlugField(read_only=True)
    

""" Data Serializer 
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    slug = serializers.SlugField(read_only=True)
    published = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def updated(self, instacnce, validated_data):
        article.title = validated_data.get('title', instance.title)
        article.description = validated_data.get('description', instance.description)
        article.slug = validated_data.get('slug', instance.slug)
        article.published =validated_data.get('published', instance.published)
        article.save()
        
        return article
"""

