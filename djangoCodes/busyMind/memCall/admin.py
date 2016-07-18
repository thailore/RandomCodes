from django.contrib import admin

from .models import Topic, Link
from .models import UserProfile

class LinkInLine(admin.TabularInline):
	model = Link
	extra = 10

class TopicAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['topic_title']}),
		]
	inlines = [LinkInLine]

admin.site.register(Topic, TopicAdmin)
admin.site.register(UserProfile)

# Register your models here.
