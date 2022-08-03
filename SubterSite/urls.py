from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path


from Main.views import *


urlpatterns = [
    path('admin', admin.site.urls),
    path('', mainview, name='main'),
    path('hello', RinaView.as_view(), name='rina'),
    re_path(r'^favicon\.ico$', favicon_view),
    path('123', TryCodeView.as_view(), name='Training code page')
]

handler404 = custom_handler404

handler403 = custom_handler403

handler500 = custom_handler500
