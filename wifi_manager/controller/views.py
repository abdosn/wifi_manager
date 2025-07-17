from django.shortcuts import render, redirect
from .wifi import scan_networks, connect_to_wifi

def index(request):
    networks = scan_networks()
    return render(request, 'controller/index.html', {'networks': networks})

def connect(request):
    if request.method == "POST":
        ssid = request.POST.get("ssid")
        password = request.POST.get("password")
        success, message = connect_to_wifi(ssid, password)
        return render(request, 'controller/result.html', {'success': success, 'message': message})
    return redirect('/')

