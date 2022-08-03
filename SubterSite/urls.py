from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path
from Main import tries


from Main.views import *


urlpatterns = [
    path('admin', admin.site.urls),
    path('', mainview, name='main'),
    path('hello', RinaView.as_view(), name='rina'),
    re_path(r'^favicon\.ico$', favicon_view),
    path('123', TemplateView.as_view(template_name='try.html', extra_context={
        'TitleOfTryPage': 'Try Mode Page',
        'Welcoming': 'Welcome to Try Mode Page',
        'Outputs': str(outputs())
    }))
]

handler404 = custom_handler404

handler403 = custom_handler403

handler500 = custom_handler500
