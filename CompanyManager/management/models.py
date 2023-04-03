from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    user = models.OneToOneField(User, related_name='company', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20,unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Device(models.Model):
    DEVICE_TYPES = (
        ('phone', 'Phone'),
        ('tablet', 'Tablet'),
        ('laptop', 'Laptop'),
        # Add more types as needed
    )
    device_type = models.CharField(max_length=10, choices=DEVICE_TYPES)
    serial_number = models.CharField(max_length=255, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.serial_number

class CheckOut(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField()
    expected_return_date = models.DateTimeField()
    def __str__(self):
        return f'{self.device} {self.employee}'

class CheckIn(models.Model):
    CONDITION_CHOICES = (
        ('good', 'Good'),
        ('damaged', 'Damaged'),
        ('lost', 'Lost'),
        # Add more choices as needed
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checkin_date = models.DateTimeField()
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    notes = models.TextField(blank=True)
    def __str__(self):
        return f'{self.device} {self.employee}'
    def save(self, *args, **kwargs):
        try:
            checkout = CheckOut.objects.get(device=self.device)
        except CheckOut.DoesNotExist:
            checkout = None

        super().save(*args, **kwargs)

        #super(CheckIn, self).save(*args, **kwargs)
        try:
            device_log = DeviceLog.objects.get(device=self.device)
            device_log.condition = self.condition
            device_log.event_date = self.checkin_date
            device_log.notes = self.notes
            device_log.save()
        except DeviceLog.DoesNotExist:
            pass
        if checkout:
            checkout.delete()


class DeviceLog(models.Model):
    CONDITION_CHOICES = (
        ('good', 'Good'),
        ('damaged', 'Damaged'),
        ('lost', 'Lost'),
    )
    device = models.OneToOneField(Device, on_delete=models.CASCADE)
    event_date = models.DateTimeField()
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.device} {self.condition}'