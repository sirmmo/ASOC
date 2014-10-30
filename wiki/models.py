from django.db import models

from core.models import *

class Wiki(models.Model):
	team = models.ForeignKey(Team, unique=True)

class Page(models.Model):
	wiki = models.ForeignKey(Wiki, related_name="pages")
	title = models.CharField(max_length=300)
	slug = models.CharField(max_length=300)

	@property
	def content(self):
		return self.pages.all().first()

	def __str__(self):
		return self.title

class PageRevision(models.Model):
	page = models.ForeignKey(Page, related_name="revisions")
	date = models.DateTimeField(auto_now=True)
	content = models.TextField()
	author = models.ForeignKey(User)
	comment = models.Textfield()

	class Meta:
		order_by=["date"]


class PageLock(models.Model):
	page = models.ForeignKey(Page, unique=True)
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now=True)

