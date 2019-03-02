from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'signup/',views.signup,name='signup'),
    url(r'login/',views.login,name='login'),
    url(r'home/',views.home,name='home'),
    url(r'employeepopup/',views.employeepopup,name='employeepopup'),
    url(r'merchantspopup/',views.merchantspopup,name='merchantspopup'),
    url(r'merchant1/',views.merchant1,name='merchant1'),
    url(r'merchant2/',views.merchant2,name='merchant2'),
    url(r'women1/',views.merchant1,name='women1'),
    url(r'womenupload/',views.merchant1,name='womenupload'),


]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)