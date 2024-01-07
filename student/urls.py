from django.contrib import admin  
from django.urls import path  
from student import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('create', views.create),  
    path('leaveindex',views.leaveindex),  
    path('editty/<int:id>', views.editty),  #navigate based on id
    path('updatety/<int:id>', views.updatety),  
    path('deletety/<int:id>', views.destroyty),  
]  