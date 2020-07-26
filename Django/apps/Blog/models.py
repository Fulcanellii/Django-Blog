from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=64, validators=[
        MinLengthValidator(limit_value=5, message='Минимальная длина текста 5 символов')])
    content = models.TextField('Описание', validators=[
        MaxLengthValidator(limit_value=250, message='Максимальная длина текста 250 символов')])
    date_posted = models.DateTimeField('Дата публикации', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья',
        verbose_name_plural = 'Статьи'
