
from django.contrib import admin
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^master/', admin.site.urls),
    url(r'^login/', include('login.urls')),
    url(r'^$',views.index),

]
