from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def appointments_page(request):
    appointments = [
        {"id": 2001, "customer": "Juan Dela Cruz", "date": "2026-09-28", "time": "10:00 AM", "status": "Confirmed"},
    ]
    return render(request, 'appointment_list.html', {"appointments": appointments})

def support_page(request):
    tickets = [
        {"id": 3001, "customer": "Maria Santos", "issue": "Login not working", "priority": "High", "status": "Open"},
    ]
    return render(request, 'support_list.html', {"tickets": tickets})