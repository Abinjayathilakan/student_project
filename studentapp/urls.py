from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('add_student',views.add_student,name='add_student'),
    path('show_students',views.show_students,name='show_students'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('edit_student_details/<int:pk>',views.edit_student_details,name='edit_student_details'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    
    path('linkpage', views.linkpage, name='linkpage'),
    path('link_student/<int:pk>', views.link_student, name='link_student'),
    
]
