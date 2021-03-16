from django.contrib import admin
from django.urls import path


from Main.views import mainview
from Main.views import custom_handler404
from Main.views import custom_handler403
from Main.views import custom_handler500
from Main.views import RinaView

urlpatterns = [
    path('admin', admin.site.urls),
    path('', mainview, name='main'),
    path('renata', RinaView.as_view()),
]

handler404 = custom_handler404

handler403 = custom_handler403

handler500 = custom_handler500