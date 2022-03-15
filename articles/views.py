from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

# Create your views here.

def article_search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")  # vem do base.html <input type='text' name='q'/>

    try:
        query = int(query_dict.get("q"))
    except:
        query=None
        
    article_obj = None
    if query is not None:
        article_obj =  Article.objects.get(id=query)
    context = { 
        "object":article_obj,
        }
    return render(request,"articles/search.html",
    context=context)

@login_required
def article_create_view(request):
    #print(request.POST)
    form = ArticleForm()
    #print(dir(form))
    context = {"form": form
    }
    if request.method == "POST":
        form = ArticleForm(request.POST)
        context['form'] = form
        if form.is_valid():
            article_object = form.save()
            
            # title = form.cleaned_data.get("title")
            # content = form.cleaned_data.get("content")
            # print(title,content)
            # article_object =  Article.objects.create(title=title,content=content)
            context['object'] = article_object
            context['created'] = True
    return render (request, "articles/create.html",
     context=context)


def article_detail_view(request, id = None):
    article_obj = None
    if id is not None:
        article_obj =  Article.objects.get(id=id)
    
    context = {
        "object":article_obj,
    }
    
    return render (request, "articles/detail.html",
     context=context)