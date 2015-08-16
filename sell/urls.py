from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'easy_ecom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.dashboardView, name= "dashboard"),
    url(r'^new/', views.newView, name= "new"),
    url(r'^edit/', views.editView, name= "edit"),

]