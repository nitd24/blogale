from django.shortcuts import get_object_or_404, render
from blog.models import Articles



def index(request):
    articles_list = Articles.objects.all()
    context = {'articles': articles_list}
    #output = '<br/> '.join([p.title for p in articles_list])
    #return HttpResponse(template.render(context))
    return render(request, 'blog/index.html', context)

def description(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    return render(request, 'blog/description.html', {'article': article})