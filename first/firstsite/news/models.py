from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор статьи', blank=True, null=True)
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',
                              verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
        
        
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,
                             verbose_name='Категория')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Comment(models.Model):
    post = models.ForeignKey(News, related_name='comments_news', on_delete=models.PROTECT, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', blank=True, null=True)
    body = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
    