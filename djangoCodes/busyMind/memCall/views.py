from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Topic, Link
from .forms import TopicForm, LinkForm, UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
	template_name = 'memCall/index.html'
	context_object_name = 'topic_list'


	def get_queryset(self):
		user = self.request.user
		return Topic.objects.filter(user=user.id)

	
class TopicView(generic.DetailView):
	model = Topic
	template_name = 'memCall/topic_view.html'
	
def view_links(request, topic_id):
	topic = get_object_or_404(Topic, pk=topic_id)
	try:
		selected_link = topic.link_set.get(pk=request.POST['link'])
	except (KeyError, Link.DoesNotExist):
		return render(request, 'memCall/topic_view.html', {
			'topic':topic,
			'error_message': "Link does not exist yet",
		})
	else:
		return HttpResponseRedirect(reverse('memCall:link_itself', args=(topic.id,)))
	
class LinkItselfView(generic.DetailView):
	model = Topic
	template_name = 'memCall/link_itself.html'

@login_required
def add_topic(request):
	
	if request.method == 'POST':
		form = TopicForm(request.POST, user=request.user)
		
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect('/memCall/')


		else:
			print(form.errors)
	else:
		form = TopicForm(user=request.user)

	return render(request, 'memCall/add_topic.html', {'form': form})

@login_required
def add_link(request):
	
	if request.method == 'POST':
		form = LinkForm(request.POST)	
		if form.is_valid():
			link = form.save(commit=False)
			link.save()
			returnLink = "/memCall/"+request.POST.get("topic","")
			return HttpResponseRedirect(returnLink)
		else:
			print(form.errors)

	else:
		form = LinkForm()

	return render(request, 'memCall/add_link.html', {'form': form})


def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request, 'memCall/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user:

			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/memCall/')
			else:
				return HttpResponse("Your account is disabled")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied")

	else:
		return render(request, 'memCall/login.html', {})

@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/memCall/')

def delete_topic(request, pk):
	topic = get_object_or_404(Topic, pk=pk).delete()
	return HttpResponseRedirect('/memCall/')

"""
def delete_link(request, pk):
	link = get_object_or_404(Link, pk=pk).delete()
	relink = "/memcall/{}".format(pk)
	return HttpResponseRedirect(relink)
"""





