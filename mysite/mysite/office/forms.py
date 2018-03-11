from django.template import Template
from material import Layout, Row, Column, Fieldset, Span2, Span3, Span5, Span6, Span10

from . import basematerial as forms

class ContactForm(forms.Form):
	email = forms.EmailField(label="Email Address")
	layout = Layout('email')
