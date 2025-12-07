from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # URL Homepage
    path('home/', views.home, name='home'),
    
    # URL buat Hapus Data
    path('hapus/<int:id>/', views.hapus_data, name='hapus_data'),

    # Untuk edit value
    path('edit/<int:id>/', views.edit_data, name='edit_data'),

    # Untuk menambah value 
    path('tambah/', views.tambah_data, name='tambah_data'),
]