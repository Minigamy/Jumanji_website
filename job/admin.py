from django.contrib import admin
from .models import Company, Vacancy, Application, Specialty


class VacancyAdmin(admin.ModelAdmin):
    fields = ('title', 'specialty', 'company', 'skills', 'description', 'salary_min', 'salary_max', 'published_at')


class CompanyAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'logo', 'description', 'employee_count', 'owner')


class ApplicationAdmin(admin.ModelAdmin):
    fields = ('written_username', 'written_phone', 'written_cover_letter', 'vacancy', 'user')


class SpecialtyAdmin(admin.ModelAdmin):
    fields = ('code', 'title', 'picture')


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
