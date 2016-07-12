from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Topic, Link


class IndexView(generic.ListView):
	template_name = 'links/index.html'
	context_object_name = 'topic_list'

	def get_queryset(self):
		return Topic.objects.all()
	
class TopicView(generic.DetailView):
	model = Topic
	template_name = 'links/topic_view.html'
	
def view_links(request, topic_id):
	topic = get_object_or_404(Topic, pk=topic_id)
	try:
		selected_link = topic.link_set.get(pk=request.POST['link'])
	except (KeyError, Link.DoesNotExist):
		return render(request, 'links/topic_view.html', {
			'topic':topic,
			'error_message': "Link does not exist yet",
		})
	else:
		return HttpResponseRedirect(reverse('links:link_itself', args=(topic.id,)))
	
class LinkItselfView(generic.DetailView):
	model = Topic
	template_name = 'links/link_itself.html'

