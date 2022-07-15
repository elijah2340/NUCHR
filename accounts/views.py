from django.contrib.auth.decorators import login_required
import requests
from django.shortcuts import render,  redirect
from .models import Account, Director, StaffProfile

# registration view imports
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib import messages, auth
from .forms import StaffRegistrationForm, StaffProfileForm


def registerview(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST, request.FILES)
        profile_form = StaffProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            title = form.cleaned_data['title']
            first_name = form.cleaned_data['first_name']
            surname = form.cleaned_data['surname']
            middle_name = form.cleaned_data['middle_name']
            email = form.cleaned_data['email']
            staff_no = form.cleaned_data['staff_no']
            ipps_no = form.cleaned_data['ipps_no']
            date_of_birth = form.cleaned_data['date_of_birth']
            gender = form.cleaned_data['gender']
            grade_level = form.cleaned_data['grade_level']
            step = form.cleaned_data['step']
            date_of_first_appointment = form.cleaned_data['date_of_first_appointment']
            date_of_first_appointment_nuc = form.cleaned_data['date_of_first_appointment_nuc']
            date_of_present_appointment = form.cleaned_data['date_of_present_appointment']
            date_of_present_posting = form.cleaned_data['date_of_present_posting']
            state = form.cleaned_data['state']
            department = form.cleaned_data['department']
            job_title = form.cleaned_data['job_title']
            employment_description = form.cleaned_data['employment_description']
            employment_type = form.cleaned_data['employment_type']
            staff_category = form.cleaned_data['staff_category']
            cadre = form.cleaned_data['cadre']
            is_director = form.cleaned_data['is_director']
            is_dhr = form.cleaned_data['is_dhr']
            is_es = form.cleaned_data['is_es']
            password = form.cleaned_data['password']
            phone_number = profile_form.cleaned_data['phone_number']
            user = Account.objects.create_user(
                first_name=first_name,
                surname=surname,
                email=email,
                password=password
            )
            user.title = title
            user.middle_name = middle_name
            user.staff_no = staff_no
            user.ipps_no = ipps_no
            user.date_of_birth = date_of_birth
            user.gender = gender
            user.grade_level = grade_level
            user.step = step
            user.date_of_first_appointment = date_of_first_appointment
            user.date_of_first_appointment_nuc = date_of_first_appointment_nuc
            user.date_of_present_appointment = date_of_present_appointment
            user.date_of_present_posting = date_of_present_posting
            user.staff_category = staff_category
            user.cadre = cadre
            user.state = state
            user.department = department
            user.job_title = job_title
            user.employment_description = employment_description
            user.employment_type = employment_type
            user.is_director = is_director
            user.is_dhr = is_dhr
            user.is_es = is_es
            user.save()

            # # user profile creation
            profile = StaffProfile()
            profile.user_id = user.id
            profile.staff = user
            profile.phone_number = phone_number
            profile.save()

            # user activation mail
            current_site = get_current_site(request)
            mail_subject = 'Please Activate Your Account'
            message = render_to_string('accounts/admin_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            return redirect('/accounts/login/?command=verification&email=' + email)
    else:
        form = StaffRegistrationForm()
        profile_form = StaffProfileForm()
    context = {
        'form': form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/register.html', context)


def staff_registerview(request):
    all_staffs = StaffProfile.objects.all()
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST, request.FILES)
        profile_form = StaffProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            title = form.cleaned_data['title']
            first_name = form.cleaned_data['first_name']
            surname = form.cleaned_data['surname']
            middle_name = form.cleaned_data['middle_name']
            email = form.cleaned_data['email']
            staff_no = form.cleaned_data['staff_no']
            ipps_no = form.cleaned_data['ipps_no']
            date_of_birth = form.cleaned_data['date_of_birth']
            gender = form.cleaned_data['gender']
            grade_level = form.cleaned_data['grade_level']
            step = form.cleaned_data['step']
            date_of_first_appointment = form.cleaned_data['date_of_first_appointment']
            date_of_first_appointment_nuc = form.cleaned_data['date_of_first_appointment_nuc']
            date_of_present_appointment = form.cleaned_data['date_of_present_appointment']
            date_of_present_posting = form.cleaned_data['date_of_present_posting']
            state = form.cleaned_data['state']
            department = form.cleaned_data['department']
            job_title = form.cleaned_data['job_title']
            employment_description = form.cleaned_data['employment_description']
            employment_type = form.cleaned_data['employment_type']
            staff_category = form.cleaned_data['staff_category']
            cadre = form.cleaned_data['cadre']
            is_director = form.cleaned_data['is_director']
            is_dhr = form.cleaned_data['is_dhr']
            is_es = form.cleaned_data['is_es']
            password = form.cleaned_data['password']
            phone_number = profile_form.cleaned_data['phone_number']
            user = Account.objects.create_user(
                first_name=first_name,
                surname=surname,
                email=email,
                password=password
            )
            user.title = title
            user.middle_name = middle_name
            user.staff_no = staff_no
            user.ipps_no = ipps_no
            user.date_of_birth = date_of_birth
            user.gender = gender
            user.grade_level = grade_level
            user.step = step
            user.date_of_first_appointment = date_of_first_appointment
            user.date_of_first_appointment_nuc = date_of_first_appointment_nuc
            user.date_of_present_appointment = date_of_present_appointment
            user.date_of_present_posting = date_of_present_posting
            user.staff_category = staff_category
            user.cadre = cadre
            user.state = state
            user.department = department
            user.job_title = job_title
            user.employment_description = employment_description
            user.employment_type = employment_type
            user.is_director = is_director
            user.is_dhr = is_dhr
            user.is_es = is_es
            user.save()

            # # user profile creation
            profile = StaffProfile()
            profile.user_id = user.id
            profile.staff = user
            profile.phone_number = phone_number
            profile.save()

            if user.is_director:
                director = Director()
                director.staff = user
                director.save()
            # user activation mail
            current_site = get_current_site(request)
            mail_subject = 'Please Activate Your Account'
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'password': password,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'Employee successfully registered, waiting for employee to confirm account ')
            return redirect('staffs')
        else:
            messages.error(request, 'Staff Registration Failed, Please Check All The Fields And Try Again ')
            context = {
                'form': form,
                'profile_form': profile_form,
                'all_staffs': all_staffs
            }
            return render(request, 'accounts/staffs.html', context)
    else:
        form = StaffRegistrationForm()
        profile_form = StaffProfileForm()
    context = {
        'form': form,
        'profile_form': profile_form,
        'all_staffs': all_staffs
    }
    return render(request, 'accounts/staffs.html', context)


def staffactivate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, OverflowError, Account.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your Account Has Been Successfully Activated, Please Login')
        return redirect('login')
    else:
        messages.error(request, 'Invalid Activation Link, Please Contact The Management.')
        return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, OverflowError, Account.DoesNotExist):
        user=None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superadmin = True
        user.save()
        messages.success(request, 'Your Account Has Been Successfully Activated, Please Login')
        return redirect('login')
    else:
        messages.error(request, 'Invalid Activation Link, Please Register Again.')
        return redirect('login')

def loginview(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You Are Now Logged In')
            url = request.META.get('HTTP_REFERER')
            try:
                query = requests.utils.urlparse(url).query
                params = dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage = params['next']
                    return redirect(nextPage)
            except:
                return redirect('dashboard')

        else:
            messages.error(request, 'Invalid Login Credentials, Please Try Again')
            return redirect('login')
    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logoutview(request):
    auth.logout(request)
    messages.success(request, 'You Have Been Logged Out, Please Come Back Soon')
    return redirect('login')


# def activateview(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = Account._default_manager.get(pk=uid)
#     except (TypeError, OverflowError, Account.DoesNotExist):
#         user=None
#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         messages.success(request, 'Your Account Has Been Successfully Activated, Please Login')
#         return redirect('login')
#     else:
#         messages.error(request, 'Invalid Activation Link')
#         return redirect('login')

def forgotpasswordview(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__iexact=email)
            current_site = get_current_site(request)
            mail_subject = 'Reset Password Link'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(request, 'A mail with a password reset link has been sent to yur email address [' + email + ']' )
            return redirect('login')
        else:
            messages.error(request, 'Account with email ' + email + ' does not exist')
            return redirect('forgotpassword')
    return render(request, 'accounts/forgotpassword.html')


def resetpassword_validateview(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, OverflowError, Account.ObjectDoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Reset Your Password')
        return redirect('reset-password')
    else:
        messages.error(request, 'This link has expired please request another')
        return redirect('login')


def resetpasswordview(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'You have successfully reset your password , please login')
            return redirect('login')
        else:
            messages.error(request, 'passwords do not match')
            return redirect('reset-password')
    return render(request, 'accounts/reset-password.html')


@login_required(login_url='login')
def changepasswordview(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(email__exact=request.user.email)

        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Your password has been sucessfully updated')
                return redirect('dashboard')
            else:
                messages.error(request, 'Please enter the valid current password')
                return redirect('change_password')
        else:
            messages.error(request, 'passwords do not match')
            return redirect('change_password')
    return render(request, 'accounts/change_password.html')