from django.db import models
from django.contrib.auth.models import User

# models

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	following = models.ManyToManyField('self', related_name='follows', symmetrical=False)

