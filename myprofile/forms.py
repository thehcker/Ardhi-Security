from django import forms
from myprofile.models import Person

class Personform(forms.ModelForm):
	"""docstring for Person"""
	class Meta:
		model = Person
		fields = ('name','age','picture')