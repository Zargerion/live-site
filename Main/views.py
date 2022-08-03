from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.template.response import TemplateResponse


favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)


def mainview(request):
    return TemplateResponse(request, 'main.html')


class RinaView(TemplateView):
    template_name = "rina.html"


# errors requests in views
def custom_handler404(request, exception):
    return render(request, '404.html')


def custom_handler403(request, exception):
    return render(request, '403.html')


def custom_handler500(request):
    return render(request, '500.html')

#train_view
#class TryCodeView(TemplateView):
    #template_name = 'try.html'
    #extra_context = {"TitleOfTryPage": "123"}

