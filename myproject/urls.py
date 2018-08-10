from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from myapp.views import Token

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'auth/', include('knox.urls')),
    url(r'auth/token/', Token.as_view()),
    url(r'/', include('myapp.urls'))
]
