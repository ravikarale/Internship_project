from django.conf.urls import url

from .import views


urlpatterns = [
	url(r'^$', views.company_home , name='company_home'),
	url(r'^call_company_reg/$',views.call_company_reg,name='call_company_reg'),
	url(r'^comp_criteria/$', views.comp_criteria, name='comp_criteria'),
    url(r'^desplayCompanyFinal/$', views.desplayCompanyFinal, name='desplayCompanyFinal'),
    url(r'^desplayCompanyIntern/$',views.desplayCompanyIntern, name='desplayCompanyIntern'),
    url(r'^company_registraion/$',views.company_registraion,name='company_registraion'),
]