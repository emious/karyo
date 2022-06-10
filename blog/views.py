from django.shortcuts import render, get_object_or_404
from .models import Article, Category


# Create your views here.


def home(request):
    return render(request, "blog/index.html")



def about(request):
    return render(request, "blog/about.html")



def contact(request):
    return render(request, "blog/contact.html")



def blog(request):
    context = {
        'articles': Article.objects.published(),
    }
    return render(request, 'blog/blog.html', context)



def detailBlog(request,slug):
    context = {
        'article': get_object_or_404(Article.objects.published(), slug=slug)
    }
    return render(request, 'blog/single.html', context)


def category(request,slug):
    context = {
        'category': get_object_or_404(Category, slug=slug, status="True")
    }
    return render(request, 'blog/category.html', context)

