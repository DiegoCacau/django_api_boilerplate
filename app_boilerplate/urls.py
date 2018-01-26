from django.conf.urls import url
from app_boilerplate.views import ViewBoilerplate

urlpatterns = [
    url(r'^endpoint_boilerplate/$', ViewBoilerplate.as_view())
]
