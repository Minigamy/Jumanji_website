from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=32)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.CharField(max_length=100)
    employee_count = models.IntegerField()


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=50)
    picture = models.URLField(default='https://place-hold.it/100x60')


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies', null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=64)
    description = models.CharField(max_length=32)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(max_length=32, null=True)
