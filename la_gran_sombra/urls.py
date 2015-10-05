from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.timer, name='timer'),
	url(r'^create$', views.form, name='create'),
	# url(r'^list$', views.list, name='list'),
]
