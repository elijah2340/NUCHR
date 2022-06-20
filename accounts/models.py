from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from department.models import Department
from hr import settings


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, surname, email, password=None):
        if not email:
            raise ValueError('user must have an email')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            surname=surname,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, first_name, surname, email, password):
        user = self.create_user(email=self.normalize_email(email),
                                password=password,
                                first_name=first_name,
                                surname=surname
                                )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self.db)
        return user


class Account(AbstractBaseUser):
    CHOICE = (('MR', 'MR'), ('MRS', 'MRS'))
    GENDER = (('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER'))

    title = models.CharField(choices=CHOICE, max_length=5)
    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    staff_no = models.CharField(max_length=50)
    ipps_no = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(choices=GENDER, max_length=10)
    grade_level = models.IntegerField(null=True)
    step = models.IntegerField(null=True)
    date_of_first_appointment = models.DateField(null=True)
    date_of_first_appointment_nuc = models.DateField(null=True)
    date_of_present_appointment = models.DateField(null=True)
    date_of_present_posting = models.DateField(null=True)
    state = models.CharField(max_length=50)
    job_title = models.CharField(max_length=255)
    employment_description = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=255)
    staff_category = models.CharField(max_length=255)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    cadre = models.CharField(max_length=255)
    is_director = models.BooleanField(default=False)
    is_dhr = models.BooleanField(default=False)
    is_es = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'surname']

    def __str__(self):
        return f'{self.first_name} | {self.surname}'

    def full_name(self):
        return f'{self.first_name} {self.surname}'

    def has_perm(self, perm, obj=None):
        return self.is_superadmin

    def has_module_perms(self, add_label):
        return True

    objects = MyAccountManager()


class Director(models.Model):
    staff = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.staff.first_name} - {self.staff.surname} | {self.staff.email}'

    def director_department(self):
        return self.staff.department


class StaffProfile(models.Model):
    profile_picture = models.ImageField(default='default.jpg', upload_to='staff/profile_picture')
    phone_number = models.IntegerField(blank=True)
    staff = models.OneToOneField(Account, on_delete=models.CASCADE)


    def __str__(self):
        return self.staff.first_name

    def full_name(self):
        return f'{self.staff.first_name} {self.staff.surname}'
