from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from app_boilerplate.views import Token

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'auth/', include('knox.urls')),
    url(r'auth/token/', Token.as_view()),
    url(r'app_boilerplate/', include('app_boilerplate.urls'))
]
