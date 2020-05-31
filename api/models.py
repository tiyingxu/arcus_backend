from django.db import models

# Create your models here.
class Post(models.Model):
    picture = models.ImageField(default = None)
    
class Translation(models.Model):
    LANGUAGES = [
        ('FR', 'French'),
        ('CH', 'Chinese'),
        ('SP', 'Spanish')
    ]
    english = models.CharField(max_length = 100)
    other = models.CharField(max_length = 100)
    other_lang = models.CharField(max_length = 100, choices = LANGUAGES)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)