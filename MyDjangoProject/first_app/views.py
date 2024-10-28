from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from first_app.models import Article


def main_page(request):
        articles = Article.objects.all()
        return render(request, 'index.html', {'articles': articles})

def article(request):
        if request.method == 'POST':
                article_id = request.POST.get('article_id')
                article = get_object_or_404(Article, id=article_id)
                return render(request, 'article.html', {'article':article})
        return render(request, 'index.html')

def contacts(request):
        return render(request,'contacts.html')