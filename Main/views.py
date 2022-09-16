from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.core.handlers import exception

#from .casino import call_casino
from .forms import *
from .models import Creation

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

#def casino(request):
#    call_casino(request)
#    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

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
            return redirect('really_main_page')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

class AfterLogin(LoginRequiredMixin, TemplateView):
    template_name = "after_login.html"
    login_url = '/account/login/'
    creation = Creation.objects.all()
    extra_context = {
        'creation': creation
    }

# errors requests in views
def custom_handler404(request, exception):
    return render(request, '404.html')


def custom_handler403(request, exception):
    return render(request, '403.html')


def custom_handler500(request):
    return render(request, '500.html')

