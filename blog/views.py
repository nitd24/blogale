from django.shortcuts import get_object_or_404, render

from blog.models import Articles
import random


def index(request):
    '''
    serves all request to the index page.
    :param request: request object
    :return: list of all published articles
    '''
    template = 'blog/index.html'
    random_idx = random.randint(0, Articles.objects.filter(is_published='True').count() - 1)
    random_obj = Articles.objects.all().filter(is_published='True')[random_idx]
    context_obj = {'rand_article': random_obj, 'articles': Articles.objects.all().order_by('-pub_date')
        .filter(is_published='True')}
    return render(request, template, context_obj)

#
# class DescriptionView(generic.DetailView):
#     model = Articles
#     template = 'blog/description.html'


def description(request, article_id):
    '''
    retrieves details of an article, retrieves by article_id from the database
    :param request: request object
    :param article_id: article_id of the article to get.
    :return: an Article object with the article_id
    '''
    article = get_object_or_404(Articles, pk=article_id)
    return render(request, 'blog/description.html', {'article': article})
