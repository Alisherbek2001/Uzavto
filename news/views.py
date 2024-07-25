from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers

class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        for image in instance.news_images.all():
            image.image.delete()
            image.delete()
        instance.delete() 
