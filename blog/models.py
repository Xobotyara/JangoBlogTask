from django.db import models
from django.utils.text import slugify

# Create your models here.

class Blogger(models.Model):
    name = models.CharField(max_length=50)
    sirname = models.CharField(max_length=50)
    birth_date = models.DateField()
    
    def get_absolute_url(self):
        return reverse("blogger_detail_url", kwargs={"pk": self.pk})
    
    def __str__(self):
        return '{0}, {1}'.format(self.sirname, self.name)


class Post(models.Model):
    slug = models.SlugField(primary_key=True, max_length=150, unique=True)
    title = models.CharField(max_length=150, db_index=True)
    body = models.TextField(blank=True, db_index=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    blogger = models.ForeignKey('Blogger', default=1, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post_detail_url', args=[self.slug])
    
    def __str__(self):
        return self.title