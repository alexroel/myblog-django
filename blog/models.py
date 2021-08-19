from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to = 'blog')
    title = models.CharField(max_length=300)
    desc =  models.TextField()
    content = RichTextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created']

    def __str__(self):
        return self.title
