from django import forms
from .models import Topic, Link
from datetime import datetime
from .models import UserProfile
from django.contrib.auth.models import User

class TopicForm(forms.ModelForm):
	topic_title = forms.CharField(max_length=200, help_text="Enter Topic")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	#user = forms.IntegerField(widget=forms.HiddenInput(), initial=9)
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')	
		super(TopicForm, self).__init__(*args, **kwargs)
	

	class Meta:
		model = Topic
		fields =('topic_title','views','user')

class LinkForm(forms.ModelForm):
	topic = forms.ModelChoiceField(queryset = Topic.objects.order_by('topic_title'),empty_label="(Choose Topic)")
	link_description = forms.CharField(max_length=200, help_text="Enter Link Description")
	link_url = forms.URLField(max_length=1000, help_text="Enter URL")
	add_date = forms.DateTimeField(widget=forms.HiddenInput(),initial = datetime.now())
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		model = Link
		fields = ('link_description', 'link_url', 'add_date','topic','views')


class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Please enter a username.")
	email = forms.CharField(help_text="Please enter your email.")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

	class Meta:
		model = User
		fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
	picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

	class Meta:
		model = UserProfile
		fields = ('picture',)


