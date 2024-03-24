from django.db import models
from django.contrib.auth.models import User


class DailyReport(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.manager} - {self.date}"
