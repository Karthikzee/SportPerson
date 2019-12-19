from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
import smtplib
import sports


def homepage(request):
	return render(request=request,
				  template_name="main/frontpage.html")

def cricket(request):
	if request.user.is_authenticated:
		return render(request, template_name="main/cricket.html",
			context={"cricket": sports.get_sport(sports.CRICKET)})
	else:
		return redirect("main:login")

def football(request):
	if request.user.is_authenticated:
		return render(request, template_name="main/football.html",
			context={"football": sports.get_sport(sports.SOCCER)})
	else:
		return redirect("main:login")

def basketball(request):
	if request.user.is_authenticated:
		return render(request, template_name="main/basketball.html",
			context={"basketball": sports.get_sport(sports.BASKETBALL)})
	else:
		return redirect("main:login")

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
 

	form = NewUserForm
	return render(request,
				  "main/register.html",
				  context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				messages.error(request, "Invalid username or password")

		else:
			messages.error(request, "Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				  "main/login.html",
				  {"form":form})


def profile(request):
	return render(request=request,
				  template_name="main/profile.html")