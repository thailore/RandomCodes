from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_picture', blank=True)

	def __unicode__(self):
		return self.user.username

class Topic(models.Model):
	topic_title = models.CharField(max_length=200, primary_key = True)
	views = models.IntegerField(default=0)	
	user = models.ForeignKey(UserProfile, to_field="user", on_delete=models.CASCADE, default=1)
	def __str__(self):
		return self.topic_title	

class Link(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #under which topic it falls
	link_description = models.CharField(max_length=200, unique = True) #description of what link is for
	link_url = models.CharField(max_length=1000, unique=True)
	add_date = models.DateTimeField('date_added')
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.link_description




