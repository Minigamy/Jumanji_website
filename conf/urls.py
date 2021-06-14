from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from job.views.account import MyCompanyView, MyCompanyCreateView, MyCompanyVacancyCreate, MyCompanyVacanciesView, \
    MyCompanyVacancyView
from job.views.public import MainView, VacanciesListView, SpecializationView, CompanyCardView, VacancyView, \
    custom_handler404, custom_handler500, SentView
from job.views.authorization.authorization import RegisterView, LogInView, LogOutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),

    path('vacancies/', VacanciesListView.as_view(), name='all_vacancies'),
    path('vacancies/cat/<str:category>/', SpecializationView.as_view(), name='vacancy_by_specialisation'),
    path('vacancies/<int:vacancies_id>/', VacancyView.as_view(), name='vacancy'),
    path('vacancies/<int:vacancy_id>/send/', SentView.as_view(), name='send'),

    path('companies/<int:company_id>/', CompanyCardView.as_view(), name='company'),

    path('mycompany/create/', MyCompanyCreateView.as_view(), name='my_company_create'),
    path('mycompany/', MyCompanyView.as_view(), name='my_company'),
    path('mycompany/vacancies/', MyCompanyVacanciesView.as_view(), name='vacancy_edit'),
    path('mycompany/vacancies/create/', MyCompanyVacancyCreate.as_view(), name='vacancy_create'),
    path('mycompany/vacancies/<int:vacancy_id>/', MyCompanyVacancyView.as_view(), name='single_vacancy'),

    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

]

handler404 = custom_handler404
handler500 = custom_handler500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
