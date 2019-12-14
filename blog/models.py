from django.db import models

# Create your models here.


class Post(models.Model):
    slug = models.SlugField(primary_key=True, max_length=150, unique=True)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    publish_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.slug])
    
    def __str__(self):
        return self.title
