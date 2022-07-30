from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addbook/', views.addbook, name='addbook'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updatebook/<int:id>', views.updatebook, name='updatebook'),
    path('delete/<int:id>', views.delete, name='delete'),
]
