from django.forms import ModelForm
from todoApp.models import todoModel
from django import forms

class todoModelForm(forms.ModelForm):
	class Meta:
		model=todoModel