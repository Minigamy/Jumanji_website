from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views import View

from job.models import Vacancy, Company


class MainView(View):
    def get(self, request):
        vacancies = Vacancy.objects.values('specialty__code', 'specialty__title', 'specialty__picture'). \
            annotate(count=Count('specialty__title'))
        companies = Vacancy.objects.values('company__id', 'company__logo').annotate(count=Count('company__name'))
        context = {
            'vacancies': vacancies,
            'companies': companies,
        }
        return render(request, 'job/index.html', context)


class VacanciesListView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')
        context = {
            'vacancies': vacancies,
            'count': vacancies.count(),
        }
        return render(request, 'job/vacancies.html', context)


class SpecializationView(View):
    def get(self, request, category):
        vacancies = Vacancy.objects.filter(specialty__code=category)
        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')
        context = {
            'vacancies': vacancies,
            'count': vacancies.count(),
        }
        return render(request, 'job/vacancies.html', context)


class CompanyCardView(View):
    def get(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        vacancies = Vacancy.objects.filter(company__name=company.name)
        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')
        context = {
            'company': company,
            'vacancies': vacancies,
            'count': vacancies.count(),
        }
        return render(request, 'job/company.html', context)


class VacancyView(View):
    def get(self, request, vacancies_id):
        vacancy = Vacancy.objects.get(pk=vacancies_id)
        vacancy.skills = vacancy.skills.split(', ')
        context = {
            'vacancy': vacancy,
        }
        return render(request, 'job/vacancy.html', context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('404 Страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
