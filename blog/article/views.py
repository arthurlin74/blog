from django.shortcuts import render
from article.models import Article,Comment
# Create your views here.
def article(request):
    '''
    Render the article page
    '''
#     articles = Article.objects.all()
  
    articles = {}
    for article in Article.objects.all():
        articles.update({article:Comment.objects.filter(article=article)})
    context = {'articles':articles}
    return render(request, 'article/article.html',context)