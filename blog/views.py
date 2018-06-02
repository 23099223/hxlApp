from django.shortcuts import render
import blog.models as models


# Create your views here.

# 查询博客列表
def query_blogs(request, tag=''):
    if tag:
        blog_list = models.Article.objects.filter(tag__exact=tag)
    else:
        blog_list = models.Article.objects.all()
    return render(request, 'blogs.html', {'blog_list': blog_list})


# 根据标签查询博客
def query_blog_bytag(request, tag):
    blogs = models.Article.objects.filter(tag__exact=tag)
    return render(request, 'blogs.html', {'blog_list': blogs})


# 获取一篇博客
def query_blog(request, id):
    blog_list = models.Article.objects.filter(id__exact=id)
    return render(request, 'blog.html', {'blog_list': blog_list})


# 页面跳转
def index(request):
    return render(request, 'index.html')
