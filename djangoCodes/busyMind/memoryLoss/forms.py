from django import forms
from .models import Topic, Link
from datetime import datetime

class TopicForm(forms.ModelForm):
	topic_title = forms.CharField(max_length=200, help_text="Enter Topic")
	
	class Meta:
		model = Topic
		fields =('topic_title',)

class LinkForm(forms.ModelForm):
	link_description = forms.CharField(max_length=200, help_text="Enter Link Description")
	link_url = forms.CharField(max_length=1000, help_text="Enter URL")
	add_date = forms.DateTimeField(widget=forms.HiddenInput(),initial = datetime.now())

	class Meta:
		model = Link
		fields = ('link_description', 'link_url', 'add_date',)

