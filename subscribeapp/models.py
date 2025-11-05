from django.db import models
from userapp.models import User
from planapp.models import Plan

# Create your models here.
class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    used_credits = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.user.username} - {self.plan.name if self.plan else 'No plan'}"