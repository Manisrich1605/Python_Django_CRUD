from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  #define all the fileds req
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)
 

    def __str__(self):#method called automatically when converting instance of class to string
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "employee"  #dbase table name