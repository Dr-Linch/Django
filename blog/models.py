from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='слаг')
    content = models.TextField(max_length=500, verbose_name='содержимое')
    preview = models.ImageField(upload_to = 'blogapp', verbose_name='превью', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_publication = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'