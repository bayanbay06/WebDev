from django.urls import path
from api.views import company_list, company_detail, vacancy_list, vacancy_detail, company_vacancies, top_ten_vacancies

urlpatterns = [
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies/', company_vacancies),
    path('vacancies/top_ten/', top_ten_vacancies)
]