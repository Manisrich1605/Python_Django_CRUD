from django.db import models  
class Student(models.Model):  
    eid = models.CharField(max_length=20)  #define all the fileds req
    eleavetype = models.CharField(max_length=100)  
    edefaultdays = models.CharField(max_length=100)  
 

    def __str__(self):#method called automatically when converting instance of class to string
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "student"  #dbase table name