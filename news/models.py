from django.db import models
from django.utils.text import slugify
from common.models import BaseModel

class News(BaseModel):
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return f"{self.pk}) {self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class NewsImage(BaseModel):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_images')
    image = models.ImageField(upload_to='media/news/news_images/')

    def __str__(self):
        return f"{self.pk}) {self.news.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.news.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "News image"
        verbose_name_plural = "News images"