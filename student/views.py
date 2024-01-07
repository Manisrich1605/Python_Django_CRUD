from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect  
from student.forms import StudentForm  
from student.models import Student  
 
def create(request):  
    if request.method == "POST":  
        form = StudentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/leaveindex')  
            except:  
                pass  
    else:  
        form = StudentForm()  
    return render(request,'indexnew.html',{'form':form})  
def leaveindex(request):  
    students = Student.objects.all()  
    return render(request,"leaveindex.html",{'students':students})  
def editty(request, id):  
    student = Student.objects.get(id=id)  
    return render(request,'editty.html', {'student':student})  
def updatety(request, id):  
    student = Student.objects.get(id=id)  
    form = StudentForm(request.POST, instance = student)  
    if form.is_valid():  
        form.save()  
        return redirect("/leaveindex")  
    return render(request, 'editty.html', {'student': student})  
def destroyty(request, id):  
   student = get_object_or_404(Student, id=id)  
   student.delete()  
   return redirect("/leaveindex")