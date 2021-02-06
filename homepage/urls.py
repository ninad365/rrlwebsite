from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='nHomepage'),
    path('bio/',views.bio, name='nBio'),
    path('publications/',views.publications, name='nPublications'),
    path('research/',views.research, name='nResearch'),
    path('students/',views.students, name='nStudents'),
    path('courses/',views.courses, name='nCourses'),
]