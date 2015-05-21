from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from blog.models import Articles
import random


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Articles.objects.all()


def index(request):
    template = 'blog/index.html'
    random_idx = random.randint(0, Articles.objects.count() - 1)
    random_obj = Articles.objects.all()[random_idx]
    context_obj = {'rand_article': random_obj, 'articles': Articles.objects.all()}
    return render(request, template, context_obj)


class DescriptionView(generic.DetailView):
    model = Articles
    template = 'blog/description.html'


def description(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    return render(request, 'blog/description.html', {'article': article})
