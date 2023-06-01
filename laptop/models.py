from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20, unique=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Laptop(models.Model):
    STATUS_CHOICES = [  
        ('available', 'Available'),
        ('assigned', 'Assigned'),
        ('decommissioned', 'Decommissioned')
    ]
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    PO_number = models.CharField(max_length=100, blank=True, null=True, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    current_user = models.ForeignKey(UserInfo, blank=True, null=True, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model


class DamagedUnit(models.Model):
    DAMAGE_TYPE_CHOICES = [
        ('minor', 'Minor'),
        ('major', 'Major'),
        ('severe', 'Severe')
        ]
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    damage_type = models.CharField(max_length=20, choices=DAMAGE_TYPE_CHOICES)
    description = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)