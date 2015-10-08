from django.conf.urls import include, url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'easy_ecom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/$', views.loginView, name= "login"),
    url(r'^logout/$', views.logoutView, name= "logout"),
    url(r'^$', views.dashboardView, name= "dashboard"),
    url(r'^verify/(?P<username>[\w]*)/(?P<verification_code>[a-z0-9]*)/$', views.emailVerificationCheckView, name= "verify"),
    url(r'^troubleLogin/$', views.troubleLoginView, name= "trouble_login"),
    url(r'^forgetPassword/$', views.forgetPasswordView, name= "forget_password"),
    url(r'^forgetPassword/reset/$', views.forgotPasswordCheckView, name= "forget_password_check"),
    url(r'^resendVerificationEmail/$', views.resendVerificationEmailView, name= "resend_verification_email"),
    url(r'^changePassword/$', views.changePasswordView, name= "change_password"),

    url(r'^newAddress/$', views.newAddress, name= "new_address"),

]
