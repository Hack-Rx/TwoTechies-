from django.conf.urls import url
from home.views import home_view, home_form

urlpatterns = [
    url(r'^$', home_form, name="home_form"),
    url(r'^result$', home_view, name="home_view"),
]
