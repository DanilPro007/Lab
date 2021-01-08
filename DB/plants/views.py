from django.shortcuts import render,redirect
from .models import Articles, Irrigation,Firms,Worker, Decorator,Time
from .forms import ArticlesForm, IrrigationForm,FirmsForm,WorkerForm, DecoratorForm,TimeForm
from django.views.generic import UpdateView, DeleteView

def plants_home(request):
    plants = Articles.objects.all()
    return render(request, 'plants/plants.html', {'plants':plants})

class plantsUpdateView(UpdateView):
    model = Articles
    template_name = 'plants/create.html'
    form_class = ArticlesForm
class plantsDeleteView(DeleteView):
    model = Articles
    success_url = '/plants'
    template_name = 'plants/delete.html'
def createpl (request):
    error=''
    if request.method =='POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plt')
        else:
            error = 'Форма была неверной'
    form =ArticlesForm()
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
    template_name = 'irrigation/update.html'
    form_class = IrrigationForm
class irrigationDeleteView(DeleteView):
    model = Irrigation
    success_url = '/irrigation'
    template_name = 'irrigation/delete.html'



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