from django.contrib import admin
from CoviSafe.models import *

# Register your models here.

class citizenAdmin(admin.ModelAdmin):
    list_display = ('username','phone_number')
    list_filter = ('age','blood_group','isolation')

class hospitalAdmin(admin.ModelAdmin):
    list_display = ('hospital_name','test_taken','hospital_phone')
    list_filter = ('test_taken','fees')

class assessmentAdmin(admin.ModelAdmin):
    list_display = ('age','vaccine','past_covid')
    list_filter = ('past_covid','age')

admin.site.register(hospital,hospitalAdmin)
admin.site.register(citizen,citizenAdmin)
admin.site.register(Self_Assesment_test,assessmentAdmin)
admin.site.register(avail_slot)