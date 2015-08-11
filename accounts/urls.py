from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'easy_ecom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', views.loginView, name= "login"),
    url(r'^logout/$', views.logoutView, name= "logout"),
    url(r'^$', views.dashboardView, name= "dashboard"),

]
