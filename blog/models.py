from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('title', max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('title', max_length=20)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField('title', max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    content = models.TextField('content')
    created_at = models.DateField('created_at', auto_now_add=True)
    updated_at = models.DateField('updated_at', auto_now=True)
    
    def __str__(self):
        return self.title