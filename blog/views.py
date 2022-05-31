from django.shortcuts import render, redirect
from .models import Category, Article


def new_article(request):
    if request.method == 'GET':
        all_category = Category.objects.all()
        return render(request, 'new.html', {'categorys': all_category})
    elif request.method == 'POST':
        title = request.POST.get('article-title', None)
        content = request.POST.get('bio', None)
        category = request.POST.get('category', None)

        category = Category.objects.get(category_name=category)

        article = Article()
        article.title = title
        article.content = content
        article.category = category
        article.save()

        return redirect('/new')


def categorys(request):
    if request.method == 'GET':
        all_category = Category.objects.all()
        return render(request, 'category.html', {'categorys': all_category})


def articles(request):
    if request.method == 'GET':
        all_category = Category.objects.all()
        all_article = Article.objects.all().order_by('-created_at')
        return render(request, 'article.html', {'categorys': all_category,
                                                'articles': all_article})
    elif request.method == 'POST':
        all_category = Category.objects.all()
        category_name = request.POST.get('category')
        category = Category.objects.get(category_name=category_name)
        sub_article = Article.objects.filter(category=category)
        return render(request, 'article.html', {'categorys': all_category,
                                                'articles': sub_article})