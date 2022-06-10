
from django.urls import path
from .views import home, about, contact, blog, detailBlog, category

urlpatterns = [
    path('', home),
    path('aboutus', about),
    path('contact', contact),
    path('blog', blog, name='blog'),
    path('<slug:slug>',detailBlog, name="detailBlog"),
    path('<slug:slug>', category, name="category"),

]
