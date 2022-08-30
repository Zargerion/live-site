from django.contrib.auth import authenticate, login
from django.core.handlers import exception
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.template.response import TemplateResponse
from .forms import *


favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)


def mainview(request):
    return TemplateResponse(request, 'main.html')


class RinaView(TemplateView):
    template_name = "rina.html"


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('main')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

# errors requests in views
def custom_handler404(request, exception):
    return render(request, '404.html')


def custom_handler403(request, exception):
    return render(request, '403.html')


def custom_handler500(request):
    return render(request, '500.html')

# train_view
# class TryCodeView(TemplateView):
    # template_name = 'try.html'
    # extra_context = {"TitleOfTryPage": "123"}
