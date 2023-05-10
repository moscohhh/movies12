from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.movief,name='movief'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')
]
