from django.urls import path
from django.views.generic.base import RedirectView
from .views import *
urlpatterns = [
    path('',  RedirectView.as_view(url='/dashboard/')),
    path('dashboard/', dashboard, name='dashboard'),
    path('department/leave/', leave, name='leave'),
    path('department/department_leave/', department_leave, name='department_leave'),
    path('department/all-leaves/', all_leave, name='all_leave'),
    path('department/approve_leave/<int:id>', director_approve_leave, name='director_approve_leave'),
    path('department/dhr-approve-leave/<int:id>', dhr_approve_leave, name='dhr_approve_leave'),
    path('department/decline_leave/<int:id>', decline_leave, name='decline_leave'),
    path('department/dhr-decline-leave/<int:id>', dhr_decline_leave, name='dhr_decline_leave'),
    path('department/departments/', allDepartments, name='all_departments'),
    path('department/directors/', allDirectors, name='directors'),
    path('department/employees/', allEmployees, name='employees'),
]
