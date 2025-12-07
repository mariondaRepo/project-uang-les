from django.contrib import admin
from django.urls import path, include  # <-- Pastikan ada 'include'
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='login/')),
    path('', include('accounts.urls')), 
]