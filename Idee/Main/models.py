from django.db import models
from django.contrib.auth.models import User

#models

class Idea(models.Model):
	content = models.CharField('idea', max_length=64, blank=True)
	username = models.ForeignKey(User)
	positive_votes = models.IntegerField()
	negative_votes = models.IntegerField()
	post_date = models.DateTimeField(auto_now=True, blank=True)

	def __unicode__(self):
		return "%s" % (self.content)


class Tags(models.Model):
	tag = models.ManyToManyField('self', related_name='tags', symmetrical=False)
	idea = models.ForeignKey(Idea)

	def __unicode__(self):
		return self.tag