from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from accounts.models import Account, Director, StaffProfile
from .forms import LeaveForm, NewDepartmentForm
from .models import Department, Leave
from django.contrib import messages, auth
from django.db.models import Q
import datetime


@login_required(login_url='login')
def dashboard(request):
    if request.user.has_perm("is_admin"):
        employees = StaffProfile.objects.filter(staff__is_director=False, staff__is_es=False,
                                                staff__is_dhr=False).order_by('staff__first_name')
        departments = Department.objects.all()
        employees_count = employees.count()
        departments_count = departments.count()
        directors = Director.objects.all()
        user = StaffProfile.objects.get(staff=request.user)
        all_staffs = StaffProfile.objects.all()
        context = {
            'employees_count': employees_count,
            'departments_count': departments_count,
            'directors': directors,
            'user': user,
            'all_staffs': all_staffs
        }

        return render(request, 'department/admin-dashboard.html', context)
    elif request.user.is_dhr:
        employees = StaffProfile.objects.filter(staff__is_director=False, staff__is_es=False, staff__is_dhr=False)
        departments = Department.objects.all()
        employees_count = employees.count()
        departments_count = departments.count()
        directors = Director.objects.all()
        try:
            leave = Leave.objects.filter(status='SENT TO DHR', sent_to_DHR=True)
        except Leave.DoesNotExist:
            leave = None
        user = StaffProfile.objects.get(staff=request.user)
        context = {
            'employees_count': employees_count,
            'departments_count': departments_count,
            'directors': directors,
            'leave': leave,
            'user': user
        }

        return render(request, 'department/dhr_dashboard.html', context)
    elif request.user.is_director:
        director = Director.objects.get(staff=request.user)
        department = Department.objects.get(name=director.staff.department)
        try:
            staffs = Account.objects.filter(department=department, is_director=False)
        except Account.DoesNotExist:
            staffs = None
        try:
            staff_profile = StaffProfile.objects.filter(staff__in=staffs)
        except StaffProfile.DoesNotExist:
            staff_profile = None
        try:
            leave = Leave.objects.filter(status='PENDING', applicant__department=department)
        except Leave.DoesNotExist:
            leave = None
        user = StaffProfile.objects.get(staff=request.user)
        context = {
            'department': department,
            'director': director,
            'staffs': staffs,
            'staff_profile': staff_profile,
            'leave': leave,
            'user': user
        }
        return render(request, 'department/director_dashboard.html', context)
    else:
        staff = StaffProfile.objects.get(staff=request.user)
        try:
            director = Director.objects.get(staff__department=staff.staff.department)
        except Director.DoesNotExist:
            director = None
        try:
            director_profile = StaffProfile.objects.get(staff=director.staff)
        except StaffProfile.DoesNotExist:
            director_profile = None
        try:
            leave = Leave.objects.get((~Q(status='DECLINED') or (Q(status='SENT TO DHR'))), applicant=request.user, completed=False)
            if datetime.date.today() >= leave.end_time:
                leave.completed = True
                leave.save()
        except Leave.DoesNotExist:
            leave = None
        try:
            previous_applications = Leave.objects.filter((~Q(status='PENDING') and (~Q(status='SENT TO DHR'))), applicant=request.user).order_by(
                '-date_applied')
        except Leave.DoesNotExist:
            previous_applications = None
        previous = previous_applications.count()
        user = StaffProfile.objects.get(staff=request.user)
        context = {
            'staff': staff,
            'director': director,
            'director_profile': director_profile,
            'leave': leave,
            'previous_applications': previous_applications,
            'previous': previous,
            'user': user

        }
        return render(request, 'department/employee_dashboard.html', context)


@login_required(login_url='login')
def leave(request):
    if request.method == 'POST':
        staff = StaffProfile.objects.get(staff=request.user)
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave_purpose = form.cleaned_data['leave_purpose']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            additional_note = form.cleaned_data['additional_note']

            data = Leave()
            data.leave_purpose = leave_purpose
            data.start_time = start_time
            data.end_time = end_time
            data.additional_note = additional_note
            data.applicant = staff.staff
            data.save()
            messages.success(request, 'Your leave application has been received and is being reviewed, check the status'
                                      ' on your dashboard ')
            return redirect('dashboard')
        else:
            messages.error(request, 'Application Failed, please check all fields and try again')
            form = LeaveForm()
            user = StaffProfile.objects.get(staff=request.user)
            context = {
                'form': form,
                'user': user
            }
            return render(request, 'department/leave.html', context)
    else:
        form = LeaveForm()
        user = StaffProfile.objects.get(staff=request.user)
    context = {
        'form': form,
        'user': user
    }
    return render(request, 'department/leave.html', context)


def department_leave(request):
    user = StaffProfile.objects.get(staff=request.user)
    director = Director.objects.get(staff=request.user)
    department = Department.objects.get(name=director.staff.department)
    pending_leave = Leave.objects.filter(status='PENDING', applicant__department=department)
    awaiting_dhr = Leave.objects.filter(status='SENT TO DHR', applicant__department=department)
    approved_leave = Leave.objects.filter(status='APPROVED', applicant__department=department, approved_by_DHR=True)
    declined_leave = Leave.objects.filter(status='DECLINED', applicant__department=department)
    all_leave = Leave.objects.filter(applicant__department=department).order_by('-date_applied')
    for leave in all_leave:
        if datetime.date.today() >= leave.end_time:
            leave.completed = True
            leave.save()
    context = {
        'pending_leave': pending_leave,
        'approved_leave': approved_leave,
        'declined_leave': declined_leave,
        'all_leave': all_leave,
        'awaiting_dhr': awaiting_dhr,
        'user': user
    }

    return render(request, 'department/department_leave.html', context)


def all_leave(request):
    user = StaffProfile.objects.get(staff=request.user)
    pending_leave = Leave.objects.filter(status='SENT TO DHR')
    approved_leave = Leave.objects.filter(status='APPROVED', approved_by_DHR=True)
    declined_leave = Leave.objects.filter(status='DECLINED')
    all_leave = Leave.objects.all().order_by('-date_applied')
    for leave in all_leave:
        if datetime.date.today() >= leave.end_time:
            leave.completed = True
            leave.save()
    context = {
        'pending_leave': pending_leave,
        'approved_leave': approved_leave,
        'declined_leave': declined_leave,
        'all_leave': all_leave,
        'user': user
    }

    return render(request, 'department/all_leave.html', context)


def director_approve_leave(request, id):
    try:
        applicant_leave = Leave.objects.get(applicant__id=id, status='PENDING', sent_to_DHR=False)
    except Leave.DoesNotExist:
        applicant_leave = None
    applicant_leave.sent_to_DHR = True
    applicant_leave.status = 'SENT TO DHR'
    applicant_leave.save()
    messages.success(request, 'Leave Status Successfully Updated')
    return redirect('department_leave')

def dhr_approve_leave(request, id):
    try:
        applicant_leave = Leave.objects.get(applicant__id=id, status='SENT TO DHR', sent_to_DHR=True,approved_by_DHR=False)
    except Leave.DoesNotExist:
        applicant_leave = None
    applicant_leave.status = 'APPROVED'
    applicant_leave.sent_to_DHR = True
    applicant_leave.approved_by_DHR = True
    applicant_leave.save()
    messages.success(request, 'Leave Status Successfully Updated')
    return redirect('all_leave')


def decline_leave(request, id):
    try:
        leave_to_decline = Leave.objects.get(applicant__id=id, status='PENDING')
    except Leave.DoesNotExist:
        leave_to_decline = None
    leave_to_decline.status = 'DECLINED'
    leave_to_decline.save()
    messages.success(request, 'Leave Status Successfully Updated')
    if request.user.is_dhr:
        return redirect('all_leave')
    else:
        return redirect('department_leave')


def dhr_decline_leave(request, id):
    try:
        leave_to_decline = Leave.objects.get(applicant__id=id, status='SENT TO DHR')
    except Leave.DoesNotExist:
        leave_to_decline = None
    leave_to_decline.status = 'DECLINED'
    leave_to_decline.save()
    messages.success(request, 'Leave Status Successfully Updated')
    if request.user.is_dhr:
        return redirect('all_leave')
    else:
        return redirect('department_leave')


def allDepartments(request):
    departments = Department.objects.all().order_by('name')
    user = StaffProfile.objects.get(staff=request.user)
    if request.user.has_perm("is_admin"):
        if request.method == 'POST':
            form = NewDepartmentForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                department = Department()
                department.name = name
                department.save()
            else:
                messages.error(request, 'Failed to add new department, please check all fields and try again')
                form = NewDepartmentForm()
                return redirect('all_departments')
        else:
            form = NewDepartmentForm()

        context = {
            'departments': departments,
            'form': form,
            'user': user
        }
        return render(request, 'department/department.html', context)
    context = {
        'departments': departments,
        # 'form': form,
        'user': user
    }
    return render(request, 'department/department.html', context)


def allDirectors(request):
    if request.user.is_dhr or request.user.has_perm("is_admin"):
        user = StaffProfile.objects.get(staff=request.user)
        directors = Director.objects.all().order_by('-staff__first_name')
        context = {
            'directors': directors,
            'user': user
        }
        return render(request, 'department/directors.html', context)


def allEmployees(request):
    if request.user.is_dhr or request.user.has_perm("is_admin"):
        user = StaffProfile.objects.get(staff=request.user)
        employees = StaffProfile.objects.filter(staff__is_director=False, staff__is_es=False, staff__is_dhr=False).order_by('staff__first_name')
        context = {
            'employees': employees,
            'user': user
        }
        return render(request, 'department/employees.html', context)