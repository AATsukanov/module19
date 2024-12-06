from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

'''
Не забыть смигрироваться:
python manage.py makemigrations
python manage.py migrate

Заполним через shell:
python manage.py shell

(InteractiveConsole)>>>>
from task5.models import Post
Post.objects.create(title='Article-1', content='Content of article-1, which is a Post #1, and created_at will be automatically added as "now".')
...
'''