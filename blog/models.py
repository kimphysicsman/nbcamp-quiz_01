from django.db import models


class Category(models.Model):
    class Meta:
        db_table = "Category"

    category_name = models.CharField(max_length=256)
    bio = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Article(models.Model):
    class Meta:
        db_table = "Article"

    title = models.CharField(max_length=256)
    content = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
