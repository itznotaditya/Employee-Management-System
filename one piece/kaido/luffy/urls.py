from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from .views import login_view, landing_page

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'), 
    path('employee_list/', views.employee_list, name='employee_list'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
