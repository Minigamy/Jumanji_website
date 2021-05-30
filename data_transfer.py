import os

import django

os.environ["DJANGO_SETTINGS_MODULE"] = "conf.settings"
django.setup()

from job.data import jobs, companies, specialties
from job.models import Company, Specialty, Vacancy

if __name__ == "__main__":
    Specialty.objects.all().delete()
    Company.objects.all().delete()
    Vacancy.objects.all().delete()

    for company in companies:
        Company.objects.create(
            id=company.get('id'),
            name=company.get('title'),
            location=company.get('location'),
            description=company.get('description'),
            employee_count=company.get('employee_count'),
        )

    for specialty in specialties:
        Specialty.objects.create(
            code=specialty.get('code'),
            title=specialty.get('title'),
        )

    for job in jobs:
        Vacancy.objects.create(
            id=job.get('id'),
            title=job.get('title'),
            specialty=Specialty.objects.get(code=job.get('specialty')),
            company=Company.objects.get(id=job.get('company')),
            skills=job.get('skills'),
            description=job.get('description'),
            salary_min=float(job.get('salary_from')),
            salary_max=float(job.get('salary_to')),
            published_at=job.get('posted'),
        )
