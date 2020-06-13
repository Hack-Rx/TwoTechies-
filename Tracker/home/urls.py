from django.conf.urls import url
from home.views import home_view, home_form,home, facts

urlpatterns = [
    #url(r'^$', home_form, name="home_form"),
    url(r'^$', home, name="home"),
    url(r'^form$', home_form, name="home_form"),
    url(r'^result$', home_view, name="home_view"),
    url(r'^facts$', facts, name="facts"),

]
