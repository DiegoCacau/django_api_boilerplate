from django.conf.urls import url
from myapp.views import MyView

urlpatterns = [
    url(r'^example/$', MyView.as_view())
]
