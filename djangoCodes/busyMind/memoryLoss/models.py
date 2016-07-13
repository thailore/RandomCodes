from django.db import models

# Create your models here.

class Topic(models.Model):
	topic_title = models.CharField(max_length=200, primary_key = True)
	
	def __str__(self):
		return self.topic_title	

class Link(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #under which topic it falls
	link_description = models.CharField(max_length=200, unique = True) #description of what link is for
	link_url = models.CharField(max_length=1000, unique=True)
	add_date = models.DateTimeField('date_added')

	def __str__(self):
		return self.link_description
