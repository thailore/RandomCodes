from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Topic, Link
from .forms import TopicForm, LinkForm

class IndexView(generic.ListView):
	template_name = 'memoryLoss/index.html'
	context_object_name = 'topic_list'

	def get_queryset(self):
		return Topic.objects.all()
	
class TopicView(generic.DetailView):
	model = Topic
	template_name = 'memoryLoss/topic_view.html'
	
def view_links(request, topic_id):
	topic = get_object_or_404(Topic, pk=topic_id)
	try:
		selected_link = topic.link_set.get(pk=request.POST['link'])
	except (KeyError, Link.DoesNotExist):
		return render(request, 'memoryLoss/topic_view.html', {
			'topic':topic,
			'error_message': "Link does not exist yet",
		})
	else:
		return HttpResponseRedirect(reverse('memoryLoss:link_itself', args=(topic.id,)))
	
class LinkItselfView(generic.DetailView):
	model = Topic
	template_name = 'memoryLoss/link_itself.html'


def add_topic(request):
	
	if request.method == 'POST':
		form = TopicForm(request.POST)
		
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect('/memoryLoss/')


		else:
			print(form.errors)
	else:
		form = TopicForm()

	return render(request, 'memoryLoss/add_topic.html', {'form': form})
"""
def add_link(request):
	
	if request.method == 'POST':
		form = LinkForm(request.POST)

		if form.is_valid():
			page=form.save(commit=False)

		try:
			top = Topic.objects.get(name=topic_title)
"""
