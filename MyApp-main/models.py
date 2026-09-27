from django.db import models

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    patient_id = models.DecimalField(max_digits=10, decimal_places=2)
    appointment_date = models.DateTimeField()
    time_slot = models.CharField(max_length=100)
    purpose = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    date_submitted = models.DateTimeField(auto_now_add=True)
    
class Support(models.Model):
    full_name = models.CharField(max_length=100)
    student_employment_id = models.EmailField()
    number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.full_name