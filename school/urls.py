from django.urls import path
from . import views

urlpatterns = [
    path('', views.school, name='school'),
    path('create_school/', views.create_school, name='create_school'), 
    path('school_desc/<int:school_id>/', views.school_desc, name='school_desc'),
    path('school_students/<int:school_id>/', views.school_students, name='school_students'),
    path('school_add_student/<int:school_id>/', views.add_student, name='add_student'),
    path('search', views.search, name='search'),
    path('all_schools', views.all_schools, name='all_schools'),


    # path('add_school', views.add_school, name='add_school'),
]
