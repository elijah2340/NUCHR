from django import forms
from django.forms import RadioSelect

from .models import Account, StaffProfile
from django.contrib.auth.password_validation import validate_password
from tempus_dominus.widgets import DatePicker


class StaffRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Your Password',
        'class': 'form-control'
    }), validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'confirm Your Password',
        'class': 'form-control'
    }), validators=[validate_password])
    date_of_birth = forms.DateField(
        required=True,
        widget=DatePicker(
            options={
                'minDate': '1990-01-10',
                'useCurrent': True,
                'collapse': True,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )
    date_of_first_appointment = forms.DateField(
        required=True,
        widget=DatePicker(
            options={
                'minDate': '1990-01-10',
                'useCurrent': True,
                'collapse': True,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )
    date_of_first_appointment_nuc = forms.DateField(
        required=True,
        widget=DatePicker(
            options={
                'minDate': '1990-01-10',
                'useCurrent': True,
                'collapse': True,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )
    date_of_present_appointment = forms.DateField(
        required=True,
        widget=DatePicker(
            options={
                'minDate': '1990-01-10',
                'useCurrent': True,
                'collapse': True,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )
    date_of_present_posting = forms.DateField(
        required=True,
        widget=DatePicker(
            options={
                'minDate': '1990-01-10',
                'useCurrent': True,
                'collapse': True,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        ),
    )
    class Meta:
        model = Account
        fields = ['title', 'first_name', 'surname', 'middle_name', 'email', 'staff_no', 'ipps_no', 'date_of_birth',
                  'gender', 'grade_level', 'step', 'date_of_first_appointment', 'date_of_first_appointment_nuc',
                  'date_of_present_appointment', 'date_of_present_posting', 'state', 'job_title',
                  'employment_description', 'department', 'employment_type', 'staff_category', 'cadre', 'is_director',
                  'is_dhr', 'is_es', 'password']

    def __init__(self, *args, **kwargs):
        super(StaffRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter Staff Firstname'
        self.fields['surname'].widget.attrs['placeholder'] = 'Enter Staff Surname'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Staff Email Address'
        self.fields['date_of_first_appointment'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['date_of_first_appointment_nuc'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['date_of_present_appointment'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['date_of_present_posting'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['is_director'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_dhr'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_es'].widget.attrs['class'] = 'form-check-input'


    def clean(self):
        cleaned_data = super(StaffRegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Submitted Passwords Don\'t match, please try again')


class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['phone_number']

    def __init__(self, *args, **kwargs):
        super(StaffProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
