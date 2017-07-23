from django.conf.urls import url

from . import views

app_name = 'adcalendar'

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url('index.html',  views.index, name='index'),
	url(r'^viewCase$' , views.viewCase , name = 'viewCase'),
	url(r'^addCase$' , views.addCase , name = 'addCase'),
	url(r'^update$', views.update , name = 'update'),
	url(r'^updateCase$', views.updateCase , name = 'updateCase'),
]



