from django.db import models
from django.db.models.deletion import SET_NULL
# Create your models here.
class citizen(models.Model):
    first_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)
    profile_photo = models.ImageField(default = False)
    username = models.TextField(max_length=40)
    age = models.IntegerField()
    phone_number = models.IntegerField(unique=True)
    aadhar = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    isolation = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    def __str__(self):
        return self.last_name

    # def __str__(self):
    #     return self.

class hospital(models.Model):
    hospital_name = models.TextField(max_length=30)
    test_taken = models.BooleanField(default=True)
    address = models.TextField(max_length=30)
    hospital_phone = models.IntegerField()
    hospital_email = models.CharField(max_length=30)
    oxygen = models.BooleanField(default=True)
    blood = models.BooleanField(default=True)
    total_beds = models.IntegerField()
    cosultation_avail = models.BooleanField()
    fees = models.IntegerField()

    def __str__(self):
        return self.hospital_name

    def __str__(self):
        return self.test_taken

    def __unicode__(self):
        return self.hospital_phone
    
    def __str__(self):
        return self.hospital_email

class Self_Assesment_test(models.Model):
    age = models.IntegerField()
    vaccine = models.BooleanField()
    if vaccine == True:
        type_vaccine = models.CharField()
        dose_count = models.IntegerField()
    past_covid = models.BooleanField()
    roaming = models.BooleanField()
    user = models.ForeignKey(citizen,on_delete=SET_NULL,null=True)

    def __bool__(self):
        return self.vaccine
    


    
