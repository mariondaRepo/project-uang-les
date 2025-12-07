from .forms import DataLaporanForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DataLaporan
import datetime


@login_required # <-- Ini penjaga pintu, kalau belum login ditendang balik
def home(request):
    # Ambil semua data dari database
    data_tabel = DataLaporan.objects.all() 
    
    context = {
        'data_tabel': data_tabel
    }
    return render(request, 'home.html', context)

# Fungsi buat Hapus Data (Nanti kita pakai tombolnya)
@login_required
def hapus_data(request, id):
    data = DataLaporan.objects.get(id=id)
    data.delete()
    return redirect('home')

@login_required
def edit_data(request, id):
    # Cari data yang mau diedit berdasarkan ID
    data_yang_mau_diedit = DataLaporan.objects.get(id=id)
    
    if request.method == 'POST':
        # Kalau tombol Save ditekan, kita update datanya
        form = DataLaporanForm(request.POST, instance=data_yang_mau_diedit)
        if form.is_valid():
            form.save()
            return redirect('home') # Balik ke home kalau sukses
    else:
        # Kalau baru buka halaman, tampilkan data lama di form
        form = DataLaporanForm(instance=data_yang_mau_diedit)

    return render(request, 'edit_data.html', {'form': form})

# ... import yang sudah ada ...

@login_required
def tambah_data(request):
    if request.method == 'POST':
        # Kita isi form dengan data yang dikirim user
        form = DataLaporanForm(request.POST)
        if form.is_valid():
            form.save() # Simpan ke database
            return redirect('home') # Balik ke dashboard
    else:
        # Kalau baru buka, tampilkan form kosong
        form = DataLaporanForm()

    return render(request, 'tambah_data.html', {'form': form})

@login_required
def home(request):
    # 1. Cek apakah user lagi milih tahun tertentu di filter?
    tahun_ini = datetime.date.today().year
    tahun_dipilih = request.GET.get('tahun') # Ambil dari URL (?tahun=2024)

    # Kalau user belum milih (baru buka), pakai tahun sekarang
    if not tahun_dipilih:
        tahun_dipilih = tahun_ini
    
    # Pastikan jadi integer biar ga error pas query
    try:
        tahun_dipilih = int(tahun_dipilih)
    except ValueError:
        tahun_dipilih = tahun_ini

    # 2. Ambil data HANYA sesuai tahun yang dipilih
    data_tabel = DataLaporan.objects.filter(tahun=tahun_dipilih)
    
    # 3. Bikin list tahun buat dropdown (Misal: 2 tahun lalu s/d 2 tahun ke depan)
    list_tahun = range(tahun_ini - 2, tahun_ini + 3)

    context = {
        'data_tabel': data_tabel,
        'tahun_dipilih': tahun_dipilih,
        'list_tahun': list_tahun,
    }
    return render(request, 'home.html', context)