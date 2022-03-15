from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_categories/', views.all_categories, name='all_categories'),
    path('all_questions/', views.all_questions, name='all_questions'),
    path('all_categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_question/', views.add_question, name='add_question'),
]
