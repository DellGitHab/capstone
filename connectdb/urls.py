from django.urls import path
from .views import (
    PersonnelListView, PersonnelCreateView, PersonnelUpdateView, PersonnelDeleteView,
    VisitorsListView, VisitorsCreateView, VisitorsUpdateView, VisitorsDeleteView, EmployeeRegisterView, 
)

from .import views

urlpatterns = [

    # Employee Registration
    path('register/', EmployeeRegisterView.as_view(), name='employee_register'),

    # Personnel URLs
    path('personnel/', PersonnelListView.as_view(), name='personnel_list'),
    path('personnel/create/', PersonnelCreateView.as_view(), name='personnel_create'),
    path('personnel/update/<int:pk>/', PersonnelUpdateView.as_view(), name='personnel_update'),
    path('personnel/delete/<int:pk>/', PersonnelDeleteView.as_view(), name='personnel_delete'),

    # Visitors URLs
    path('visitors/', VisitorsListView.as_view(), name='visitors_list'),
    path('visitors/create/', VisitorsCreateView.as_view(), name='visitors_create'),
    path('visitors/update/<int:pk>/', VisitorsUpdateView.as_view(), name='visitors_update'),
    path('visitors/delete/<int:pk>/', VisitorsDeleteView.as_view(), name='visitors_delete'),

    path('api/login/', views.login_view, name='login'),
    path('api/create-user/', views.create_user_view, name='create_user'),
]
