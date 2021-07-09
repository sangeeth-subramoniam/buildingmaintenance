from django.shortcuts import render,redirect
from structure.models import MeterMaster
from .forms import MeterMasterForm

# Create your views here.
def home(request):

    form = MeterMasterForm()
    if(request.method == 'POST'):
        form = MeterMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/metermaster')

    meter = MeterMaster.objects.all().order_by('MeterNo')

    context = {
        'form' : form,
        'meter' : meter
    }
    return render(request,'metermaster/home.html' , context)

def updatemeterForm(request , pk):
    meter = MeterMaster.objects.get(id = pk)
    form = MeterMasterForm( instance=meter)

    if(request.method == 'POST'):
        #print('Contents' , request.POST)
        if 'submit' in request.POST:
            form = MeterMasterForm(request.POST , instance=meter)
            if form.is_valid():
                form.save()
                return redirect('/metermaster')
        else:
            return redirect('/metermaster')
    
    context = {
        'form' : form
    }

    return render(request,'metermaster/update_form.html',context)

def deletemeterForm(request, pk):

    meter = MeterMaster.objects.get(id = pk)

    if(request.method == 'POST'):
        meter.delete()
        return redirect('/metermaster')


    context = {
        'mm' : meter
    }

    return render(request, 'metermaster/delete_form.html' , context)