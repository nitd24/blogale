from django.db import models
from django_elasticsearch.models import EsIndexable

#from simple_elasticsearch.mixins import ElasticsearchIndexMixin
#from django.db.models.signals import post_save, pre_delete

#, ElasticsearchIndexMixin

class Articles(EsIndexable, models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    category = models.CharField(max_length=100)
    hero_img = models.ImageField(upload_to='hero_images')
    secondary_img = models.ImageField(upload_to='secondary_images', blank=True)
    description = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Elasticsearch(EsIndexable.Elasticsearch):
        mappings = {'title': {'boost': 2.0}}
        fields = {
            'title': {type: 'string'},
            'description': {type: 'string'},
            'category': {type: 'string'},
        }

#     @classmethod
#     def get_queryset(cls):
#         return Articles.objects.all().select_related('blog')
#
#     @classmethod
#     def get_index_name(cls):
#         return 'blog'
#
#     @classmethod
#     def get_type_name(cls):
#         return ''
#
#     @classmethod
#     def get_type_mapping(cls):
#         return {
#             "properties": {
#                 "title": {
#                     "type": "string"
#                 },
#                 "description": {
#                     "type": "string"
#                 },
#                 "category": {
#                     "type": "string"
#                 }
#             }
#         }
#
#     @classmethod
#     def get_document(cls, obj):
#         return {
#             'title': obj.title,
#             'description': obj.description,
#             'category': obj.category
#         }
#
#
# post_save.connect(Articles.save_handler, sender=Articles)
# pre_delete.connect(Articles.delete_handler, sender=Articles)