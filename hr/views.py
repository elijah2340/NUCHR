from django.shortcuts import render


def showhome(request):

    return render(request, 'admin-dashboard.html')