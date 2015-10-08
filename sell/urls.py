from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'easy_ecom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.dashboardView, name= "dashboard"),
    url(r'^edit/$', views.editView, name= "edit"),

    url(r'^new/$', views.newView, name= "new"),
    url(r'^new/inventory/$', views.newInventory, name= "newInventory"),
    url(r'^new/book/addAuthor$', views.newAuthor, name= "newAuthor"),
    url(r'^new/book/addPublisher$', views.newPublisher, name= "newPublisher"),
    url(r'^new/book/(?P<isbn>[0-9]*)/$', views.addNewBook, name= "newBook"),
    url(r'^new/book/$', views.addNewBookPKCheck, name= "newBookCheck"),


]
