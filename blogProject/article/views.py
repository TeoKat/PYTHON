from django.shortcuts import get_object_or_404,get_list_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from .models import Article, Likes, Comments

# Create your views here.




@login_required(login_url='login')
def home(request):
 

    return render(request, 'home.html')

@login_required(login_url='login')
def articles(request):

    articles = get_list_or_404(Article)
    

    return render(request, 'articles.html', {'articles': articles })

@login_required(login_url='login')
def article(request, id):

    article = get_object_or_404(Article, pk=id)
    comments = get_list_or_404(Comments, article_id = id )
    likes = get_list_or_404(Likes, article_id = id )
    
    return render(request, 'article.html', {'article': article,'comments': comments, 'likes': likes, })

@login_required(login_url='login')
def titles(request):

    articles = Article.objects.all()
    return render(request, 'titles.html', {'articles': articles})

@login_required(login_url='login')
def comments(request):
    art_id = request.GET['aid']
    if request.method == 'POST':
        newComment = Comments(article_id = art_id, name = request.user.username, comment = request.POST['comments'], date = '2020-03-23')
        newComment.save()
    # article = get_object_or_404(Article, pk=article_id)
    
    return redirect('article/'+ art_id)

@login_required(login_url='login')
def likes(request):
    
    l_id = request.GET.get('l_id')
    xlike = Likes.objects.get(id=l_id)
    xlike.counter+=1
    xlike.save()
        
    return redirect('article/' + l_id)
   



