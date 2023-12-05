from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Doctor, Appointment

class AppointmentView(View):
    @method_decorator(login_required(login_url="login"))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            'doctors': Doctor.objects.all()
        }
        return render(request, "appointment/index.html", context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time = request.POST.get('time')
        note = request.POST.get('note')

        doctor = None  # Initialize doctor variable

        if doctor_id:
            doctor = get_object_or_404(Doctor, id=doctor_id)

        if name and phone and email and doctor and date and time:
            Appointment.objects.create(
                name=name, phone=phone, email=email, doctor=doctor, date=date, time=time, note=note)
            messages.success(request, 'Appointment done successfully')

        return redirect('appointment')
