from django.contrib import admin  
from django.urls import path  
from employee import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  #navigate based on id
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  