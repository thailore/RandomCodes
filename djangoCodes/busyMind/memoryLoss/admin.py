from django.contrib import admin

from .models import Topic, Link

class LinkInLine(admin.TabularInline):
	model = Link
	extra = 10

class TopicAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['topic_title']}),
		]
	inlines = [LinkInLine]

admin.site.register(Topic, TopicAdmin)

# Register your models here.
