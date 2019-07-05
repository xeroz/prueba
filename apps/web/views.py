from django.shortcuts import render


def home(request):
    data = {'user': request.user}
    return render(request, 'home.html', data)
