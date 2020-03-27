from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 200, null = True)
    content = models.TextField( null = True)
    date = models.DateTimeField( null = True)
    author = models.CharField(max_length = 50,  null = True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name='comments')
    name = models.CharField(max_length = 50, default="???",  null = True)
    comment = models.TextField( null = True)
    date = models.DateTimeField( null = True)

    def __str__(self):
        return self.comment

class Likes(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name='likes')
    counter = models.IntegerField(default = 0,  null = True)

