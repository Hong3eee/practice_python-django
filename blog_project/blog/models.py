from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
	title = models.CharField('Title',max_length=50)
	slug = models.SlugField('Slug',unique=True,allow_unicode=True,help_text='one word for title alias.')
	description = models.CharField('Description',max_length=100,blank=True,help_text='simple description text.')
	content = models.TextField('Content')
	create_date = models.DateTimeField('Create Date',auto_now_add=True)
	modify_date = models.DateTimeField('Modify Date',auto_now=True)

	class Meta:
		verbose_name = 'post'
		verbose_name_plural = 'post'
		db_table = 'my_post'
		ordering = ('-modify_date',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:post_detail',args=(self.slug)) #, not here
	
	def get_previous_post(self):
		return self.get_previous_by_modify_date()
	
	def get_next_post(self):
		return self.get_next_by_modify_date()

