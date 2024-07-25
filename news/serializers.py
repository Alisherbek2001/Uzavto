from rest_framework import serializers
from . import models

class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsImage
        fields = ['id', 'image']

class NewsSerializer(serializers.ModelSerializer):
    news_images = NewsImageSerializer(many=True, required=False, read_only=True)
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = models.News
        fields = ['id', 'author', 'title', 'body', 'created_at', 'news_images']
        read_only_fields = ['author', 'created_at']

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        news = models.News.objects.create(**validated_data)
        for image_data in images_data:
            models.NewsImage.objects.create(news=news, image=image_data)
        return news

    def update(self, instance, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()

        if images_data:
            for old_image in instance.news_images.all():
                old_image.image.delete()
                old_image.delete()

            for image_data in images_data:
                models.NewsImage.objects.create(news=instance, image=image_data)

        return instance