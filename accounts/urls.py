from django.urls import path
from .views import *

urlpatterns = [
    path('staffs/', staff_registerview, name='staffs'),
    path('admin-register/', registerview, name='register'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('activate/<uidb64>/<token>/', staffactivate, name='staff_activate'),
    path('admin-activate/<uidb64>/<token>/', activate, name='admin_activate'),
    path('resetpassword_validate/<uidb64>/<token>/', resetpassword_validateview, name='resetpassword_validate'),
    path('forgotpassword/', forgotpasswordview, name='forgotpassword'),
    path('reset-password/', resetpasswordview, name='reset-password'),
    path('change-password/', changepasswordview, name='change_password'),

]
