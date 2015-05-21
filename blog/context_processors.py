from blog.models import Articles
import random


def related_articles(request):
    '''
    :param request:
    :return: returns 4 random articles from published articles
    '''
    # last = Articles.objects.count() - 1
    # index1 = random.randint(0, last)
    # index2 = random.randint(0, last - 1)
    # if index2 == index1: index2 = last
    #
    # MyObj1 = Articles.objects.all()[index1]
    # MyObj2 = Articles.objects.all()[index2]
    return {'related_articles': Articles.objects.all().filter(is_published='True').order_by('?')[:4]}


def random_article_id(request):
    '''
    :param request:
    :return: returns a random article id from published articles
    '''
    a = Articles.objects.all().filter(is_published='True')
    arr = []
    for article in a:
        arr.append(article.id)

    return {'random_article_id': random.choice(arr)}