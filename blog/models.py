from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    category = models.CharField(max_length=100)
    hero_img = models.ImageField(upload_to='hero_images')
    secondary_img = models.ImageField(upload_to='hero_images', blank=True)
    description = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
