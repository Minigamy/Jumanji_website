from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from django import forms
from django.contrib.auth.models import User

from job.models import Application, Company, Vacancy


class LogInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')

    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'Логин',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.label_class = 'text-muted'
        self.helper.add_input(Submit('submit', 'Войти', css_class='btn btn-primary btn-lg btn-block'))
        self.fields['username'].help_text = None


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',

        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.label_class = 'text-muted'
        self.helper.add_input(Submit('submit', 'Зарегистрироваться', css_class='btn btn-primary btn-lg btn-block'))
        self.fields['username'].help_text = None
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']
        labels = {
            'written_username': 'Вас зовут',
            'written_phone': 'Ваш телефон',
            'written_cover_letter': 'Сопроводительное письмо',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'post'
        self.helper.label_class = 'mb-1'
        self.helper.add_input(Submit('submit', 'Записаться на пробный урок', css_class='btn btn-primary mt-4 mb-2'))
        self.helper.layout = Layout(
            Row(
                Column('written_username'),
            ),
            Row(
                Column('written_phone'),
            ),
            Row(
                Column('written_cover_letter'),
            ),
        )


class EditCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'logo', 'description', 'employee_count']
        labels = {
            'name': 'Название компании',
            'location': 'География',
            'logo': 'Логотип',
            'description': 'Информация о компании',
            'employee_count': 'Количество человек в компании',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.label_class = 'mb-2 text-dark'
        self.helper.add_input(Submit('submit', 'Сохранить', css_class='btn btn-info'))
        self.helper.layout = Layout(
            Row(
                Column('name'), Column('logo'),
            ),
            Row(
                Column('employee_count'), Column('location'),
            ),
            Row(
                Column('description'),
            ),
        )


class EditVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max']
        labels = {
            'title': 'Название вакансии',
            'specialty': 'Специализация',
            'salary_min': 'Зарпалата от',
            'salary_max': 'Зарплата до',
            'skills': 'Требуемые навыки',
            'description': 'Описание вакансии',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.label_class = 'mb-2 text-dark'
        self.helper.add_input(Submit('submit', 'Сохранить', css_class='btn btn-info'))
        self.helper.layout = Layout(
            Row(Column('title'), Column('specialty')),
            Row(Column('salary_min'), Column('salary_max')),
            Row(Column('skills')),
            Row(Column('description')),
        )
