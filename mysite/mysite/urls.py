from django.urls import path
from django.views import generic
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from mysite.office import views as office_views
from mysite.office import forms

urlpatterns = [
	url(r'^$', office_views.home, name='home'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    	url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
	url(r'^signup/$', office_views.signup, name='signup'),

	#New contact
	url(r'^contact/add/$', generic.FormView.as_view(form_class=forms.ContactForm, template_name="contact.html")),
]
