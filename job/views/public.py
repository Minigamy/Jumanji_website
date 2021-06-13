from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.views import View

from job.forms import ApplicationForm
from job.models import Vacancy, Company, Specialty, Application


class MainView(View):
    def get(self, request):
        specialties = Specialty.objects.all()
        companies = Company.objects.all()
        return render(request, 'job/index.html', context={
            'specialties': specialties,
            'companies': companies
        })


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
        try:
            vacancies = Vacancy.objects.filter(specialty__code=category)
            for_header = Specialty.objects.get(code=category)
        except Specialty.DoesNotExist:
            raise Http404
        for vacancy in vacancies:
            vacancy.skills = vacancy.skills.split(', ')
        context = {
            'vacancies': vacancies,
            'count': vacancies.count(),
            'header': for_header
        }
        return render(request, 'job/vacancies.html', context)


class CompanyCardView(View):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(pk=company_id)
            vacancies = Vacancy.objects.filter(company__name=company.name)
        except Company.DoesNotExist:
            raise Http404
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
        try:
            vacancy = Vacancy.objects.get(pk=vacancies_id)
            vacancy.skills = vacancy.skills.split(', ')
        except Vacancy.DoesNotExist:
            raise Http404
        context = {
            'vacancy': vacancy,
        }
        if request.user.is_authenticated:
            context['form'] = ApplicationForm
        return render(request, 'job/vacancy.html', context)

    def post(self, request, vacancies_id):
        # form = ApplicationForm(request.POST)
        # if form.is_valid():
        #     application = form.save(commit=False)
        #     application.vacancy = Vacancy.objects.get(id=vacancies_id)
        #     application.user_id = request.user.id
        #     print(application.user_id)
        #     application.save()
        #     return render(request, 'job/sent.html', {'vacancy_id': vacancies_id})
        form = ApplicationForm(request.POST)
        vacancy = Vacancy.objects.get(id=vacancies_id)
        if form.is_valid():
            form_data = form.cleaned_data
            Application.objects.create(
                written_username=form_data['written_username'],
                written_phone=form_data['written_phone'],
                written_cover_letter=form_data['written_cover_letter'],
                vacancy=vacancy,
                user=User.objects.get(username=request.user)
            )
        return redirect('send', vacancies_id)


class SentView(View):
    def get(self, request, vacancy_id):
        return render(request, 'job/sent.html', context={
            'vacancy_id': vacancy_id,
        })


class MyCompanyView(View):
    def get(self, request):
        return render(request, 'job/company-edit.html', )


class MyCompanyVacanciesView(View):
    def get(self, request):
        return render(request, 'job/vacancy-list.html', )


class MyCompanySingleVacancyView(View):
    def get(self, request, vacancy_id):
        return render(request, 'job/vacancy-edit.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('404 Страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
