from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50)
    available_quantity = models.IntegerField()

    def __str__(self):
        return self.name

from django.contrib.auth.models import User

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ← this line is important
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    rental_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)




class MaintenanceLog(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    issue_reported = models.TextField()
    date_reported = models.DateField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.equipment.name} - {'Resolved' if self.resolved else 'Pending'}"
