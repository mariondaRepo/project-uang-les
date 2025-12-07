from django.db import models
import datetime

class DataLaporan(models.Model):
    # Opsi Pilihan (Dropdown)
    OPSI_STATUS = [
        ('', 'None'),    # Default kosong, tampilannya 'None'
        ('Sudah', 'Sudah'),
        ('Belum', 'Belum'),
    ]

    # Kita set default tahun ke tahun sekarang
    tahun_sekarang = datetime.date.today().year

    # Kolom Tahun (Baru)
    tahun = models.IntegerField(default=tahun_sekarang)
    
    # Kolom Nama (Wajib)
    kolom_1 = models.CharField(max_length=100, verbose_name="Nama Siswa")

    # Kolom Bulan (Sekarang pakai choices)
    kolom_2 = models.CharField(max_length=10, choices=OPSI_STATUS, blank=True, null=True, default='', verbose_name="Januari")
    kolom_3 = models.CharField(max_length=10, choices=OPSI_STATUS, blank=True, null=True, default='', verbose_name="Februari")
    kolom_4 = models.CharField(max_length=10, choices=OPSI_STATUS, blank=True, null=True, default='', verbose_name="Maret")
    kolom_5 = models.CharField(max_length=10, choices=OPSI_STATUS, blank=True, null=True, default='', verbose_name="April")
    kolom_6 = models.CharField(max_length=10, choices=OPSI_STATUS, blank=True, null=True, default='', verbose_name="Mei")
    kolom_7 = models.CharField(max_length=10, choices=OPSI_STATUS, blank=True, null=True, default='', verbose_name="Juni")
    kolom_8 = models.CharField(max_length=10, choices=OPSI_STATUS, blank=True, null=True, default='', verbose_name="Juli")
    kolom_9 = models.CharField(max_length=10, choices=OPSI_STATUS, blank=True, null=True, default='', verbose_name="Agustus")
    kolom_10 = models.CharField(max_length=10, choices=OPSI_STATUS, blank=True, null=True, default='', verbose_name="September")
    kolom_11 = models.CharField(max_length=10, choices=OPSI_STATUS, blank=True, null=True, default='', verbose_name="Oktober")
    kolom_12 = models.CharField(max_length=10, choices=OPSI_STATUS, blank=True, null=True, default='', verbose_name="November")
    kolom_13 = models.CharField(max_length=10, choices=OPSI_STATUS, blank=True, null=True, default='', verbose_name="Desember")
    
    def __str__(self):
        return f"{self.kolom_1} ({self.tahun})"