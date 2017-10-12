from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$' , views.login , name='login'),
    url(r'^getAdminLogin/$' , views.getAdminLogin , name='getAdminLogin'),
    url(r'^admin_logout/$' , views.admin_logout , name='admin_logout'),
    url(r'^displayAdminFinal/$' , views.displayAdminFinal , name='displayAdminFinal'),
    url(r'^displayAdminIntern/$' , views.displayAdminIntern , name='displayAdminIntern'),
    url(r'^callAddMember/$' , views.callAddMember , name='callAddMember'),
    url(r'^addPcm/$' , views.addPcm, name='addPcm'),
    url(r'^backToLogin/$' , views.backToLogin, name='backToLogin')
]

