from django.shortcuts import render, redirect
from main.models import Idea
from user.forms import SignupForm, AuthenticateForm


# views

#TO DO: Votes/Time Logic


def ideas(request, auth_form=None, user_form=None):
	if request.user.is_authenticated():
		user = request.user
		top_ideas = Idea.objects.order_by('-top')[0]
		latest_ideas = Idea.objects.order_by('-id')[0]
		ideas = top_ideas | latest_ideas
		return render(request, 
			          'ideas.html',
			          {'user': user, 'ideas': ideas, })
	else:
		signup_form = SignupForm
		authenticate_form = AuthenticateForm
		return render(request,
            		'login.html',
            		{ 'signup_form': signup_form, 'authenticate_form': authenticate_form, })
