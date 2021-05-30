
from django.contrib import admin
from django.urls import path

from job.views import MainView, VacanciesListView, SpecializationView, CompanyCardView, VacancyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('vacancies/', VacanciesListView.as_view(), name='all_vacancies'),
    path('vacancies/cat/<str:category>/', SpecializationView.as_view(), name='vacancy_by_specialisation'),
    path('companies/<int:company_id>/', CompanyCardView.as_view(), name='company'),
    path('vacancies/<int:vacancies_id>/', VacancyView.as_view(), name='vacancy'),

]
