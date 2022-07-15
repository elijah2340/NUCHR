from django.db import models
from unidecode import unidecode
from django.template.defaultfilters import slugify
from hr.settings import AUTH_USER_MODEL


class Department(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=1000, unique=True, null=False)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(unidecode(value))
        super(Department, self).save(*args, **kwargs)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Leave(models.Model):
    STATUS = (('APPROVED', 'APPROVED'), ('PENDING', 'PENDING'), ('SENT TO DHR', 'SENT TO DHR'), ('DECLINED', 'DECLINED'))
    purpose = (('ANNUAL LEAVE', 'ANNUAL LEAVE'), ('CASUAL LEAVE', 'CASUAL LEAVE'), ('SICK LEAVE', 'SICK LEAVE'), ('MATERNITY LEAVE', 'MATERNITY LEAVE'), ('OTHERS', 'OTHERS'))
    applicant = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_applied = models.DateTimeField(auto_now_add=True)
    start_time = models.DateField()
    end_time = models.DateField()
    no_of_days = models.CharField(max_length=15, blank=True, null=True)
    status = models.CharField(max_length=255, choices=STATUS, default='PENDING')
    leave_purpose = models.CharField(max_length=255, choices=purpose, default='ANNUAL')
    additional_note = models.TextField(blank=True, null=True, max_length=10000)
    sent_to_DHR = models.BooleanField(default=False)
    approved_by_DHR = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)


class Query(models.Model):
    STATUS = (('SENT TO DHR', 'SENT TO DHR'), ('SENT TO ES', 'SENT TO ES'),
              ('QUERY ISSUED', 'QUERY ISSUED'), ('STAFF RESPONDED', 'STAFF RESPONDED'), ('RESOLVED', 'RESOLVED'))
    staff = models.ForeignKey("accounts.StaffProfile", on_delete=models.CASCADE)
    subject = models.CharField(max_length=10000)
    details = models.TextField()
    staff_response = models.TextField(blank=True)
    recommendation_to_es = models.TextField(blank=True)
    sanction_or_warning = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default='SENT TO DHR', max_length=255)
