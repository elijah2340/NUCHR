from django.urls import path
from django.views.generic.base import RedirectView
from .views import *
urlpatterns = [
    path('',  RedirectView.as_view(url='/dashboard/')),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/es-query/', es_pending_query, name='es_pending_query'),
    path('dashboard/es-query/<int:id>/', es_query_details, name='es_query_details'),
    path('dashboard/es-query/<int:id>/sanction-staff', sanction_staff, name='sanction_staff'),
    path('dashboard/query/<int:id>/', employe_response_query, name='employee_query'),
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
    path('department/department_query/', department_query, name='department_query'),
    path('department/query/', all_query, name='all_query'),
    path('department/pending_query/', pending_query, name='pending_query'),
    path('department/pending_query/<int:id>/', issue_query, name='issue_query'),
    path('department/responded_query/', responded_query, name='responded_query'),
    path('department/responded_query/<int:id>', responded_query_details, name='responded_query_details'),
    path('department/responded_query/forward/<int:id>/', forward_query_to_es, name='forward_query_to_es'),
    path('department/responded_query/warn_staff/<int:id>/', warn_staff, name='warn_staff'),

]
