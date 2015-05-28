from blog.models import Articles
import random
import ipdb


def related_articles(request):
    '''
    :param request:
    :return: returns 4 random articles from published articles
    '''
    no_of_articles = Articles.objects.count()

    # checking if we have enough number of articles, else randomize the available articles

    if no_of_articles > 4:
        list_of_ids = random.sample(range(1, no_of_articles), 4)
    else:
        list_of_ids = random.sample(range(1, no_of_articles), no_of_articles)

    return {'related_articles': Articles.objects.filter(pk__in=list_of_ids)}

