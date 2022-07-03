from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):
    declines = Decline.objects.count()
    receives = Receive.objects.count()
    requests = Request.objects.count()
    victimsnum = Victim.objects.count()
    victims = Receive.objects.filter(bantuan= 'Bantuan Baik Pulih').count
    victims1 = Receive.objects.filter(bantuan='Bantuan Rumah Baru').count
    victims2 = Receive.objects.filter(bantuan='Bantuan Bulanan').count
    victims3 = Receive.objects.filter(bantuan='Bantuan Bekalan Makanan').count
    return render(request,"App_PKOB/home.html", {'victimsnum': victimsnum,'victims': victims, 'victims1': victims1, 'victims2': victims2, 'victims3': victims3, 'requests': requests, 'declines': declines, 'receives': receives})

def index(request):
    victims = Victim.objects.all()
    paginator = Paginator(victims, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'App_PKOB/index.html', context={'victims': victims, 'page_obj': page_obj})

def index2(request):
    reqs = Request.objects.all()
    paginator = Paginator(reqs, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'App_PKOB/index2.html', context={'reqs': reqs, 'page_obj': page_obj})

def index3(request):
    declines = Decline.objects.all()
    paginator = Paginator(declines, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'App_PKOB/index3.html', context={'declines': declines, 'page_obj': page_obj})

def index4(request):
    receives = Receive.objects.all()
    paginator = Paginator(receives, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'App_PKOB/index4.html', context={'receives': receives, 'page_obj': page_obj})

def add_detail(request):
    if request.method == 'POST':
        upload = VictimCreate(request.POST, request.FILES)
        if upload.is_valid():
            messages.success(request, "MAKLUMAT MANGSA BERJAYA DIDAFTAR !")
            upload.save()
            return redirect('add_detail')
        else:
            messages.error(request, "MAKLUMAT MANGSA TIDAK BERJAYA DIDAFTAR ! Nombor IC Tersebut Telah Digunakan Untuk Mendaftar Bantuan.")
            return redirect('add_detail')
    else:
        return render(request, 'App_PKOB/add_detail.html')

def request(request):
    if request.method == 'POST':
        req = RequestCreate(request.POST, request.FILES)
        if req.is_valid():
            req.save()
            messages.success(request, "PENDAFTARAN BANTUAN TELAH BERJAYA DIHANTAR !")
            return render(request, 'App_PKOB/request.html')
        else:
            messages.error(request, "PENDAFTARAN BANTUAN TIDAK BERJAYA DIHANTAR! Nombor IC Anda Telah Digunakan Untuk Mendaftar Bantuan.")
            return render(request, 'App_PKOB/request.html')
    else:
        return render(request, 'App_PKOB/request.html')

def delete_detail(request, ic_no):
    victim = Victim.objects.get(ic_no = ic_no)
    victim.delete()
    messages.success(request, "MAKLUMAT BERJAYA DIPADAMKAN !")
    return redirect('report')

def delete_request(request, ic_no):
    decline = Decline.objects.get(ic_no = ic_no)
    decline.delete()
    messages.success(request, "MAKLUMAT PENDAFTARAN DITOLAK INI BERJAYA DIPADAMKAN!")
    return redirect('reportdecline')

def deletereq_detail(request, ic_no):
    req = Request.objects.get(ic_no = ic_no)
    req.delete()
    messages.success(request, "MAKLUMAT PENDAFTARAN INI BERJAYA DIPADAMKAN!")
    return redirect('reportrequest')

def edit_detail(request, ic_no):
    victim_info = Victim.objects.get(pk=ic_no)
    return render(request, 'App_PKOB/add_detail.html', context={'victim_info': victim_info})

def receivereq_detail(request, ic_no):
    victim_info = Victim.objects.get(pk=ic_no)
    return render(request, 'App_PKOB/requestReceive.html', context={'victim_info': victim_info})

def acceptreq_detail(request, ic_no):
    req_info = Request.objects.get(pk=ic_no)
    return render(request, 'App_PKOB/request.html', context={'req_info': req_info})

def notacceptreq_detail(request, ic_no):
    req_info = Request.objects.get(pk=ic_no)
    return render(request, 'App_PKOB/requestDecline.html', context={'req_info': req_info})


def update_detail(request, ic_no):
    victim = Victim.objects.get(pk=ic_no)
    victim.ic_no = request.POST['ic_no']
    victim.name = request.POST['name']
    victim.phone_no = request.POST['phone_no']
    victim.mukim = request.POST['mukim']
    victim.no_rumah = request.POST['no_rumah']
    victim.jalan_lrg = request.POST['jalan_lrg']
    victim.kg_tmn = request.POST['kg_tmn']
    victim.kerja = request.POST['kerja']
    victim.tanggungan = request.POST['tanggungan']
    victim.sebab = request.POST['sebab']
    victim.pendapatan = request.POST['pendapatan']
    victim.bantuan = request.POST['bantuan']
    victim.save()
    messages.success(request, "MAKLUMAT MANGSA BERJAYA DIKEMASKINIKAN !")
    return redirect('report')

def updatereq_detail(request, ic_no):
    if request.method == 'POST':
        victim = VictimCreate(request.POST, request.FILES)
        if victim.is_valid():
            victim.save()
            req = Request.objects.get(ic_no=ic_no)
            req.delete()
            messages.success(request, "PENDAFTARAN TELAH BERJAYA DITERIMA!")

        else:
            messages.error(request, "PENDAFTARAN TIDAK BERJAYA DITERIMA ! Nombor IC tersebut telah didaftarkan. Anda boleh padamkan pendaftaran ini")

    else:
        pass
    return redirect('reportrequest')

def declinereq_detail(request, ic_no):
    if request.method == 'POST':
        decline = DeclineCreate(request.POST, request.FILES)
        if decline.is_valid():
            decline.save()
            req = Request.objects.get(ic_no=ic_no)
            req.delete()
            messages.success(request, "PENDAFTARAN TELAH BERJAYA DITOLAK !")

        else:
            messages.error(request, "PENDAFTARAN TIDAK BERJAYA DITOLAK ! Nombor IC tersebut telah mendaftar dan ditolak. Anda boleh padamkan pendaftaran ini.")

    else:
        pass
    return redirect('reportrequest')

def receive_detail(request, ic_no):
    if request.method == 'POST':
        receive = ReceiveCreate(request.POST, request.FILES)
        if receive.is_valid():
            receive.save()
            victim = Victim.objects.get(ic_no=ic_no)
            victim.delete()
            messages.success(request, "BANTUAN TELAH BERJAYA DITERIMA!")

        else:
            messages.error(request, "BANTUAN TIDAK BERJAYA DITERIMA ! Nombor IC tersebut telah menerima bantuan.")

    else:
        pass
    return redirect('report')

def victim_detail(request, ic_no):
    victim = Victim.objects.get(pk=ic_no)     # pk='primary key'
    return render(request, 'App_PKOB/victim_detail.html', context={'victim': victim})

def viewreceive_detail(request, ic_no):
    receive = Receive.objects.get(pk=ic_no)     # pk='primary key'
    return render(request, 'App_PKOB/detail_receive.html', context={'receive': receive})

def viewdecline_detail(request, ic_no):
    decline = Decline.objects.get(pk=ic_no)     # pk='primary key'
    return render(request, 'App_PKOB/detail_decline.html', context={'decline': decline})

def request_detail(request, ic_no):
    req = Request.objects.get(pk=ic_no)     # pk='primary key'
    return render(request, 'App_PKOB/request_detail.html', context={'req': req})