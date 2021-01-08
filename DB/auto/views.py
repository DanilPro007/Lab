from django.shortcuts import render
def registerPage(request):
    context = {}
    return render(request, 'auto/register.html', context)
def loginPage(request):
    context = {}
    return render(request, 'auto/login.html', context)
