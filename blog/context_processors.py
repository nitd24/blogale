from blog.models import Articles
import random


def related_articles(request):
    # last = Articles.objects.count() - 1
    # index1 = random.randint(0, last)
    # index2 = random.randint(0, last - 1)
    # if index2 == index1: index2 = last
    #
    # MyObj1 = Articles.objects.all()[index1]
    # MyObj2 = Articles.objects.all()[index2]
    return {'related_articles': Articles.objects.all().order_by('?')[:4]}