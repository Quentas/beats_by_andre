from django.db import models
import datetime
from django.utils import timezone


class New_Text(models.Model):
	title = models.CharField('TITLE', max_length = 50)
	content = models.TextField('TEXT', max_length = 1000)
	date = models.DateTimeField('DATE')

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 1))

	class Meta:
		verbose_name = 'Announcements'
		verbose_name_plural = 'Announcements'
		
	def __str__(self):
		return self.title
		

class New_Track(models.Model):
	title = models.CharField('TITLE', max_length = 50)
	date = models.DateTimeField('DATE')
	content = models.FileField(upload_to = 'tracks')

	def __str__(self):
		return self.title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 1))

	class  Meta:
		verbose_name = 'Tracks'
		verbose_name_plural = 'Tracks'


class New_Video(models.Model):
	title = models.CharField('TITLE', max_length = 50)
	date = models.DateTimeField('DATE')
	content = models.CharField('LINK', max_length = 1000)

	def __str__(self):
		return self.title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 1))

	class  Meta:
		verbose_name = 'Videos'
		verbose_name_plural = 'Videos'

		
class Track(models.Model):
	title = models.CharField('TITLE', max_length = 50)
	date = models.DateTimeField('DATE')
	duration = models.IntegerField('DURATION')
	likes = models.IntegerField('LIKES')

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 1))
		

class Author(models.Model):
	author_pseudo = models.CharField('AUTHOR PSEUDO', max_length = 50)
	author_name = models.CharField('AUTHOR NAME', max_length = 50)
	author_photo = models.ImageField(upload_to = 'images')
	author_text = models.TextField('TEXT', max_length = 5000)
	author_links = models.TextField('LINKS (separate with \';;\')', max_length = 2000)

	class Meta:
		verbose_name = 'Author'
		verbose_name_plural = 'Authors'
		
	def __str__(self):
		title = self.author_pseudo + " // " + self.author_name
		return title