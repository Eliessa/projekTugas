from django.shortcuts import render
from dashboard.forms import FormBarang
from dashboard.models import Barang, Transaksi 

def tambah_barang(request):
    form=FormBarang()
    konteks={
        'form':form,
    }
    return render(request, 'tambah_barang.html', konteks)

def  product(request):
    titlee="Product"
    trs=Transaksi.objects.all()
    konteks={
        'titel':titlee,
        'trs':trs,
    }
    return render(request,'product.html', konteks)
def Barang_view(request):
    barangs=Barang.objects.all()
    konteks={
        'barangs':barangs  
    }
    return render(request,'tampil_brg.html',konteks)

def trsn(request):
    trs=Transaksi.objects.all()
    konteks={
        'trs':trs
    }
    return render(request,'tampil_transaksi.html',konteks)
    
# Create your views here.
