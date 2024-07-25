from typing import Any
from django.db import models
from django.utils.text import slugify
from common.models import BaseModel

class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
class SubCategory(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255,null=True,blank=True)
    TYPE_STATUS = (
        ('files','files'),
        ('pages','pages')
    )
    type = models.CharField(max_length=10,choices=TYPE_STATUS)
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_pural = 'Subcategories'