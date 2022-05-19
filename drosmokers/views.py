from django.shortcuts import render


def index_view(request):
    return render(request, "index.html")


def success_view(request):
    return render(request, "success.html")
