from django.db import models

# Create your models here.
class Event(models.Model):
    img=models.ImageField(upload_to="pic")
    img_second=models.ImageField(upload_to="pic")


    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Booking(models.Model):
    cus_name=models.CharField(max_length=50)
    cus_ph=models.CharField(max_length=12)
    cus_email = models.EmailField()
    name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

class Contact(models.Model):
    c_name = models.CharField(max_length=250)
    c_email = models.EmailField()
    c_subject = models.TextField()

    def __str__(self):
        return 'Name  :' + self.c_name + '         Email  :' + self.c_email
