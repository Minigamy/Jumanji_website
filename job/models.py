from django.db import models
from django.contrib.auth.models import User

from conf.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Company(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR)
    description = models.CharField(max_length=100)
    employee_count = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f'name={self.name}'


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return f'code={self.code}'


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies', null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=64)
    description = models.CharField(max_length=32)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(max_length=32, null=True)


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=64)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, related_name='applications', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)


class Resume(models.Model):
    STATUS_CHOICES = [
        ('looking_for_a_job', 'Ищу работу'),
        ('open_to_suggestions', 'Открыт к предложениям'),
        ('not_looking_for_a_job', 'Не ищу работу'),
    ]
    GRADE_CHOICES = [
        ('junior', 'Младший (junior)'),
        ('middle', 'Средний (middle)'),
        ('senior', 'Страший (senior)')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    status = models.CharField(max_length=64, choices=STATUS_CHOICES)
    salary = models.IntegerField()
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='resume')
    grade = models.CharField(max_length=64, choices=GRADE_CHOICES)
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.URLField()


