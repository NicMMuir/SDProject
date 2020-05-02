from django.urls import path

from . import views

app_name = 'student_predictor'
urlpatterns = [
    path('Showall', views.ShowAllStudentsView.as_view(), name='show_all_students'),
    path('<int:pk>/', views.ShowStudentView.as_view(), name='show_student'),
    path('predict', views.PredictStudentView.as_view(), name='predict_student'),
]