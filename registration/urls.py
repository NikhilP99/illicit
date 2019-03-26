from django.urls import path,include
from . import views

app_name='registration'

urlpatterns = [
    path('',views.reg_forms,name='acc_forms'),
    path('signup/',views.signup_user,name='signup'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
]
