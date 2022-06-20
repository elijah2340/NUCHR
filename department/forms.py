from django import forms
from .models import Leave, Department
from tempus_dominus.widgets import DatePicker


class LeaveForm(forms.ModelForm):
    start_time = forms.DateField(
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
    end_time = forms.DateField(
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
        model = Leave
        fields = ['leave_purpose', 'start_time', 'end_time', 'additional_note']

    def __init__(self, *args, **kwargs):
        super(LeaveForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(LeaveForm, self).clean()


class NewDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(NewDepartmentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(NewDepartmentForm, self).clean()