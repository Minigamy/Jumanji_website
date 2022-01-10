# Туту будут вьюхи для Моей компании и Резюме
import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

from job.forms import EditCompanyForm, EditVacancyForm, EditResumeForm
from job.models import Company, Vacancy, Application, Resume


@method_decorator(login_required, name='dispatch')
class MyCompanyView(View):
    def get(self, request):
        if not Company.objects.filter(owner_id=request.user.id).exists():
            return render(request, 'job/company-create.html')
        company = Company.objects.get(owner_id=request.user.id)
        context = {
            'form': EditCompanyForm(instance=company),
        }
        return render(request, 'job/company-edit.html', context)

    def post(self, request):
        if not Company.objects.filter(owner_id=request.user.id).exists():
            return render(request, 'job/company-create.html')
        instance = Company.objects.get(owner_id=request.user.id)
        form = EditCompanyForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Информация о компании обновлена')
            return redirect('my_company')
        return render(request, 'job/company-edit.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class MyCompanyCreateView(View):
    def get(self, request):
        if Company.objects.filter(owner_id=request.user.id).exists():
            return redirect('my_company')
        context = {
            'form': EditCompanyForm,
        }
        messages.add_message(request, messages.INFO, 'Создание новой компании')
        return render(request, 'job/company-edit.html', context)

    def post(self, request):
        if not Company.objects.filter(owner_id=request.user.id).exists():
            return render(request, 'job/company-create.html')
        form = EditCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = User.objects.get(id=request.user.id)
            company.save()
            messages.add_message(request, messages.INFO, 'Компания успешно создана')
            return redirect('my_company')
        return render(request, 'job/company-edit.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class MyCompanyVacanciesView(View):
    def get(self, request):
        if not Company.objects.filter(owner__id=request.user.id):
            return redirect('my_company')
        vacancies = Vacancy.objects.filter(company_id=request.user.company.id) \
            .values('id', 'title', 'salary_min', 'salary_max') \
            .annotate(applications_count=Count('applications'))
        context = {
            'vacancies': vacancies
        }
        return render(request, 'job/vacancy-list.html', context)


@method_decorator(login_required, name='dispatch')
class MyCompanyVacancyView(View):
    def get(self, request, vacancy_id):
        if not Company.objects.filter(owner_id=request.user.id).exists():
            return render(request, 'job/company-create.html')
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        applications = Application.objects.filter(vacancy_id=vacancy_id)
        context = {
            'form': EditVacancyForm(instance=vacancy),
            'applications': applications,
        }
        return render(request, 'job/vacancy-edit.html', context)

    def post(self, request, vacancy_id):
        if not Company.objects.filter(owner_id=request.user.id).exists():
            return render(request, 'job/company-create.html')
        instance = Vacancy.objects.get(id=vacancy_id)
        form = EditVacancyForm(request.POST, instance=instance)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = Company.objects.get(id=request.user.company.id)
            vacancy.published_at = datetime.date.today()
            vacancy.save()
            messages.add_message(request, messages.INFO, 'Информация о вакансии обновлена')
            return redirect('vacancy_edit')


@method_decorator(login_required, name='dispatch')
class MyCompanyVacancyCreate(View):
    def get(self, request):
        if not Company.objects.filter(owner_id=request.user.id).exists():
            return render(request, 'job/company-create.html')
        context = {
            'form': EditVacancyForm,
        }
        messages.add_message(request, messages.INFO, 'Создание новой вакансии')
        return render(request, 'job/vacancy-edit.html', context)

    def post(self, request):
        if not Company.objects.filter(owner_id=request.user.id).exists():
            return render(request, 'job/company-create.html')
        form = EditVacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = Company.objects.get(id=request.user.company.id)
            vacancy.published_at = datetime.date.today()
            vacancy.save()
            messages.add_message(request, messages.INFO, 'Вакансия добавлена')
            return redirect('vacancy_edit')
        return render(request, 'job/vacancy-edit.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ResumeView(View):
    def get(self, request):
        if not Resume.objects.filter(user__id=request.user.id).exists():
            return render(request, 'job/resume-create.html')
        resume = Resume.objects.get(user__id=request.user.id)
        context = {
            'form': EditResumeForm(instance=resume),
        }
        return render(request, 'job/resume-edit.html', context)

    def post(self, request):
        resume = Resume.objects.get(user__id=request.user.id)
        form = EditResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Резюме обновлено')
            return redirect('resume')
        return render(request, 'job/resume-edit.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ResumeCreateView(View):
    def get(self, request):
        if Resume.objects.filter(user__id=request.user.id).exists():
            return redirect('resume')
        context = {
            'form': EditResumeForm,
        }
        messages.add_message(request, messages.INFO, 'Создание нового резюме')
        return render(request, 'job/resume-edit.html', context)

    def post(self, request):
        form = EditResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = User.objects.get(id=request.user.id)
            resume.save()
            messages.add_message(request, messages.INFO, 'Резюме создано')
            return redirect('resume')
        return render(request, 'job/resume-edit.html', {'form': form})
