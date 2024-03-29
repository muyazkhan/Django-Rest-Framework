from django.contrib import admin
from .models import Appointment
# Register your models here.
class AppointmentModel(admin.ModelAdmin):
  list_display =["doctor_username","patient_username","appointment_type","appointment_status"]

  def doctor_username(self,obj):
    return obj.patient.user.username
  def patient_username(self,obj):
    return obj.doctor.user.username
admin.site.register(Appointment,AppointmentModel)