from django.shortcuts import render,redirect
from .models import Plants, Irrigation,Firms,Worker, Decorator,Time
from .forms import PlantsForm, IrrigationForm,FirmsForm,WorkerForm, DecoratorForm,TimeForm
from django.views.generic import UpdateView, DeleteView, DetailView

def plants_home(request):
    plants = Plants.objects.all()
    return render(request, 'plants/plants.html', {'plants':plants})

class plantsUpdateView(UpdateView):
    model = Plants
    template_name = 'plants/create.html'
    form_class = PlantsForm
class plantsDeleteView(DeleteView):
    model = Plants
    success_url = '/plants'
    template_name = 'plants/delete.html'
class plantsViewView(DetailView):
    model = Plants
    template_name = 'plants/update.html'
    context_object_name = 'plants'
def createpl (request):
    error=''
    if request.method =='POST':
        form = PlantsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plt')
        else:
            error = 'Форма была неверной'
    form =PlantsForm()
    data={
        'form':form,
        'error':error
    }
    return render(request,'plants/create.html',data)

def irrigation_home(request):
    irrigation = Irrigation.objects.all()
    return render(request, 'irrigation/irrigation.html', {'irrigation':irrigation})
def createir (request):
    error=''
    if request.method =='POST':
        form = IrrigationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('irr')
        else:
            error = 'Форма была неверной'
    form =IrrigationForm()
    data={
        'form':form,
        'error':error
    }
    return render(request,'irrigation/create.html',data)


class irrigationUpdateView(UpdateView):
    model = Irrigation
    template_name = 'irrigation/create.html'
    form_class = IrrigationForm
class irrigationDeleteView(DeleteView):
    model = Irrigation
    success_url = '/irrigation'
    template_name = 'irrigation/delete.html'
class irrigationViewView(DetailView):
    model = Irrigation
    template_name = 'irrigation/update.html'
    context_object_name = 'irrigation'


def firms_home(request):
    firms = Firms.objects.all()
    return render(request, 'firms/firms.html', {'firms':firms})


def createfrm (request):
    error=''
    if request.method =='POST':
        form = FirmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frm')
        else:
            error = 'Форма была неверной'
    form =FirmsForm()
    data={
        'form':form,
        'error':error
    }
    return render(request,'firms/create.html',data)

class firmsUpdateView(UpdateView):
    model = Firms
    template_name = 'firms/create.html'
    form_class = FirmsForm
class firmsDeleteView(DeleteView):
    model = Firms
    success_url = '/firms'
    template_name = 'firms/delete.html'

class firmsViewView(DetailView):
    model = Firms
    template_name = 'firms/update.html'
    context_object_name = 'firms'


def worker_home(request):
    worker = Worker.objects.all()
    return render(request, 'worker/worker.html', {'worker':worker})


def createwrk(request):
    error=''

    if request.method =='POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wrk')
        else:
            error = 'Форма была неверной'
    form =WorkerForm()
    data={
        'form':form,
        'error':error
    }
    return render(request,'worker/create.html',data)


class workerUpdateView(UpdateView):
    model = Worker
    template_name = 'worker/create.html'
    form_class = WorkerForm
class workerDeleteView(DeleteView):
    model = Worker
    success_url = '/worker'
    template_name = 'worker/delete.html'

class workerViewView(DetailView):
    model = Worker
    template_name = 'worker/update.html'
    context_object_name = 'worker'

def decorator_home(request):
    decorator = Decorator.objects.all()
    return render(request, 'decorator/decorator.html', {'decorator':decorator})


def createdcr(request):
    error=''
    if request.method =='POST':
        form = DecoratorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dcr')
        else:
            error = 'Форма была неверной'
    form =DecoratorForm()
    data={
        'form':form,
        'error':error
    }
    return render(request,'decorator/create.html',data)

class decoratorUpdateView(UpdateView):
    model = Decorator
    template_name = 'decorator/create.html'
    form_class = DecoratorForm
class decoratorDeleteView(DeleteView):
    model = Decorator
    success_url = '/decorator'
    template_name = 'decorator/delete.html'
class decoratorViewView(DetailView):
    model = Decorator
    template_name = 'decorator/update.html'
    context_object_name = 'decorator'

def time_home(request):
    time = Time.objects.order_by('-date')
    return render(request, 'time/time.html', {'time':time})


def createtm(request):
    error=''
    if request.method =='POST':
        form = TimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tm')
        else:
            error = 'Форма была неверной'
    form =TimeForm()
    data={
        'form':form,
        'error':error
    }
    return render(request,'time/create.html',data)

class timeUpdateView(UpdateView):
    model = Time
    template_name = 'time/create.html'
    form_class = TimeForm
class timeDeleteView(DeleteView):
    model = Time
    success_url = '/time'
    template_name = 'time/delete.html'

class timeViewView(DetailView):
    model = Time
    template_name = 'time/update.html'
    context_object_name = 'time'