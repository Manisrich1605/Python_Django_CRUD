from django import forms  
from employee.models import Employee
from django.forms import fields

class EmployeeForm(forms.ModelForm):  #class inherit forms.ModelForm(allow form automatically generate Emp model)
    class Meta:  #to provide meta data from the form
        model = Employee  #specify model
        fields = "__all__"  #include all firlds from model