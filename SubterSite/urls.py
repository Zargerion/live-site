from django.contrib import admin, auth
from django.urls import path
from django.urls.conf import re_path, include
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

from Main.views import *
from Main.tries import *
from Main.helps import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('', mainview, name='main'),
    path('she_was_here', RinaView.as_view(), name='rina'),
    re_path(r'^favicon\.ico$', favicon_view),
    path('try', TemplateView.as_view(template_name='try.html', extra_context={
        'TitleOfTryPage': 'Try Mode Page',
        'Welcoming': 'Welcome to Try Mode Page',
        'Outputs': outputs
    }), name='secret'),
    path('accounts/registration', registration, name='registration'),
    path('hello', login_required(AfterLogin.as_view()), name='really_main_page'),
    #path('back_to_future', casino, name='casino'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

handler404 = custom_handler404

handler403 = custom_handler403

handler500 = custom_handler500
