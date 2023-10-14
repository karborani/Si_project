from django import forms
from .models import Schools,Student

class SchoolForm(forms.ModelForm):
    class Meta:
        model = Schools
        fields = ['name','phone','email','description']


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['first_name','last_name','phone','date_of_birth','school']
