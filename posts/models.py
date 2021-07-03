from django.db import models
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=200, verbose_name='Наименование')
	image = models.ImageField(verbose_name='Изображение')
	description = models.TextField(verbose_name='Сам текст')
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_detail', args=[self.slug])