from django.db import models
from datetime import datetime, timedelta


# Create your models here.
class Victim(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    mukim = models.CharField(max_length=50, verbose_name='MUKIM', blank=False)
    name = models.CharField(max_length=50, verbose_name='NAMA', blank=False)
    phone_no = models.CharField(max_length=11, verbose_name='NO TELEFON', blank=False)
    ic_no = models.CharField(primary_key=True, max_length=12, verbose_name='NO IC')
    no_rumah = models.CharField(max_length=50, verbose_name='NO RUMAH', blank=False)
    jalan_lrg = models.CharField(max_length=50, verbose_name='JALAN/LRG', blank=False)
    kg_tmn = models.CharField(max_length=50, verbose_name='KG/TMN', blank=False)
    kerja = models.CharField(max_length=50, verbose_name='PEKERJAAN', blank=False)
    tanggungan = models.CharField(max_length=50, verbose_name='TANGGUNGAN', blank=False)
    sebab = models.CharField(max_length=50, verbose_name='SEBAB MOHON', blank=False)
    pendapatan = models.CharField(max_length=50, verbose_name='PENDAPATAN', blank=False)
    bantuan = models.CharField(max_length=50, verbose_name='BANTUAN', blank=False)

    @property
    def calculate_age(self):
        birthday = self.ic_no[:6]
        date_time_obj = datetime.strptime(birthday, '%y%m%d')
        if date_time_obj > datetime.today():
            date_time_obj -= timedelta(weeks=5124, days=2)
            age = datetime.today() - date_time_obj
            return int(age.days / 365)
        else:
            age = datetime.today() - date_time_obj
            return int(age.days / 365)

class Request(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    mukim = models.CharField(max_length=50, verbose_name='MUKIM', blank=False)
    name = models.CharField(max_length=50, verbose_name='NAMA', blank=False)
    phone_no = models.CharField(max_length=11, verbose_name='NO TELEFON', blank=False)
    ic_no = models.CharField(primary_key=True, max_length=12, verbose_name='NO IC')
    no_rumah = models.CharField(max_length=50, verbose_name='NO RUMAH', blank=False)
    jalan_lrg = models.CharField(max_length=50, verbose_name='JALAN/LRG', blank=False)
    kg_tmn = models.CharField(max_length=50, verbose_name='KG/TMN', blank=False)
    kerja = models.CharField(max_length=50, verbose_name='PEKERJAAN', blank=False)
    tanggungan = models.CharField(max_length=50, verbose_name='TANGGUNGAN', blank=False)
    sebab = models.CharField(max_length=50, verbose_name='SEBAB MOHON', blank=False)
    pendapatan = models.CharField(max_length=50, verbose_name='PENDAPATAN', blank=False)
    bantuan = models.CharField(max_length=50, verbose_name='BANTUAN', blank=False)

    @property
    def calculate_age(self):
        birthday = self.ic_no[:6]
        date_time_obj = datetime.strptime(birthday, '%y%m%d')
        if date_time_obj > datetime.today():
            date_time_obj -= timedelta(weeks=5124, days=2)
            age = datetime.today() - date_time_obj
            return int(age.days / 365)
        else:
            age = datetime.today() - date_time_obj
            return int(age.days / 365)

class Decline(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    mukim = models.CharField(max_length=50, verbose_name='MUKIM', blank=False)
    name = models.CharField(max_length=50, verbose_name='NAMA', blank=False)
    phone_no = models.CharField(max_length=11, verbose_name='NO TELEFON', blank=False)
    ic_no = models.CharField(primary_key=True, max_length=12, verbose_name='NO IC')
    no_rumah = models.CharField(max_length=50, verbose_name='NO RUMAH', blank=False)
    jalan_lrg = models.CharField(max_length=50, verbose_name='JALAN/LRG', blank=False)
    kg_tmn = models.CharField(max_length=50, verbose_name='KG/TMN', blank=False)
    kerja = models.CharField(max_length=50, verbose_name='PEKERJAAN', blank=False)
    tanggungan = models.CharField(max_length=50, verbose_name='TANGGUNGAN', blank=False)
    sebab = models.CharField(max_length=50, verbose_name='SEBAB MOHON', blank=False)
    pendapatan = models.CharField(max_length=50, verbose_name='PENDAPATAN', blank=False)
    bantuan = models.CharField(max_length=50, verbose_name='BANTUAN', blank=False)


    @property
    def calculate_age(self):
        birthday = self.ic_no[:6]
        date_time_obj = datetime.strptime(birthday, '%y%m%d')
        if date_time_obj > datetime.today():
            date_time_obj -= timedelta(weeks=5124, days=2)
            age = datetime.today() - date_time_obj
            return int(age.days / 365)
        else:
            age = datetime.today() - date_time_obj
            return int(age.days / 365)

class Receive(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    mukim = models.CharField(max_length=50, verbose_name='MUKIM', blank=False)
    name = models.CharField(max_length=50, verbose_name='NAMA', blank=False)
    phone_no = models.CharField(max_length=11, verbose_name='NO TELEFON', blank=False)
    ic_no = models.CharField(primary_key=True, max_length=12, verbose_name='NO IC')
    no_rumah = models.CharField(max_length=50, verbose_name='NO RUMAH', blank=False)
    jalan_lrg = models.CharField(max_length=50, verbose_name='JALAN/LRG', blank=False)
    kg_tmn = models.CharField(max_length=50, verbose_name='KG/TMN', blank=False)
    kerja = models.CharField(max_length=50, verbose_name='PEKERJAAN', blank=False)
    tanggungan = models.CharField(max_length=50, verbose_name='TANGGUNGAN', blank=False)
    sebab = models.CharField(max_length=50, verbose_name='SEBAB MOHON', blank=False)
    pendapatan = models.CharField(max_length=50, verbose_name='PENDAPATAN', blank=False)
    bantuan = models.CharField(max_length=50, verbose_name='BANTUAN', blank=False)


    @property
    def calculate_age(self):
        birthday = self.ic_no[:6]
        date_time_obj = datetime.strptime(birthday, '%y%m%d')
        if date_time_obj > datetime.today():
            date_time_obj -= timedelta(weeks=5124, days=2)
            age = datetime.today() - date_time_obj
            return int(age.days / 365)
        else:
            age = datetime.today() - date_time_obj
            return int(age.days / 365)




