from django.shortcuts import render
from django.views.generic import TemplateView


def mainview(request):
    return render(request, 'Main/Templates/main.html')


class RinaView(TemplateView):
    template_name = "Main/Templates/rina.html"


# errors requests in views
def custom_handler404(request, exception):
    return render(request, 'Errors/Templates/404.html')


def custom_handler403(request, exception):
    return render(request, 'Errors/Templates/403.html')


def custom_handler500(request):
    return render(request, 'Errors/Templates/500.html')