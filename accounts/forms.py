from django import forms
from .models import DataLaporan

class DataLaporanForm(forms.ModelForm):
    class Meta:
        model = DataLaporan
        fields = '__all__' # Ini ajaibnya, dia bakal ambil semua 13 kolom lu otomatis