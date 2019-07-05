from django.shortcuts import render


def home(request):
    data = {'user': request.user}
    return render(request, 'admin/home.html', data)
