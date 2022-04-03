from django.db import models
import datetime
from django.utils import timezone

class Article(models.Model):
    title = models.CharField("Название статьи",max_length=100)
    text = models.TextField("Текст статьи")
    pub_date = models.DateTimeField("Дата публикации", default=timezone.now())

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("Имя автора", max_length=50)
    comment_text = models.CharField("Текст комментария", max_length=350)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
