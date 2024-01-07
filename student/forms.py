from django import forms  
from student.models import Student
from django.forms import fields

class StudentForm(forms.ModelForm):  #class inherit forms.ModelForm(allow form automatically generate Emp model)
    class Meta:  #to provide meta data from the form
        model = Student  #specify model
        fields = "__all__"  #include all firlds from model