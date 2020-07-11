from django.db import models
from django.utils import timezone

# Create your models here.

class OnerSignup(models.Model):
    oner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(upload_to="media")
    contact = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class UserSingup(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    user_image = models.ImageField(upload_to="media")
    user_address = models.CharField(max_length=200)
    user_city = models.CharField(max_length=200)
    user_state = models.CharField(max_length=200)
    user_email = models.EmailField()
    user_contact = models.IntegerField()
    password = models.CharField(max_length=200)
    STATUS=(("1","active"),("0","deactive"))
    user_status=models.CharField(max_length=20,choices=STATUS)


    def __str__(self):
        return self.user_name

class Bus(models.Model):
    bus_id = models.AutoField(primary_key=True)
    bus_name = models.CharField(max_length=200)
    bus_form_city = models.CharField(max_length=200)
    bus_to_city = models.CharField(max_length=200)
    bus_arival_time = models.TimeField()
    bus_rant = models.IntegerField()
    bus_distance = models.IntegerField()
    bus_trival_time = models.IntegerField()
    bus_oner_id = models.ForeignKey(OnerSignup,on_delete= models.CASCADE)
    STATUS=(("1","active"),("0","deactive"))
    bus_status=models.CharField(max_length=20,choices=STATUS)

    def __str__(self):
        return self.bus_name

class BusBooking(models.Model):
    book_id = models.AutoField(primary_key=True)
    bus_id = models.ForeignKey(Bus,on_delete=models.CASCADE)
    user_book_id = models.ForeignKey(UserSingup,on_delete=models.CASCADE)
    STATUS = (("0", "Free"), ("1", "Booked"))
    order_status = models.CharField(max_length=20, choices=STATUS)
    order_time = models.DateTimeField(default=timezone.now)







