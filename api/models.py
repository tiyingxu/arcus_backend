from django.db import models

# Create your models here.
class Post(models.Model):
    picture = models.ImageField(default = None)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Translation(models.Model):
    from_word = models.CharField(max_length = 100)
    from_lang = models.CharField(max_length = 100)
    other_word = models.CharField(max_length = 100)
    other_lang = models.CharField(max_length = 100)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)