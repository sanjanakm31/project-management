from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

PRIORITY_CHOICES = [('High','High'),('Low','Low'),('R&D','R&D')]

class Project(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    project_name = models.CharField(max_length=200)
    customer = models.CharField(max_length=200, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    quantity = models.CharField(max_length=100, blank=True)
    subtask = models.CharField(max_length=300, blank=True)
    remarks = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    completion = models.PositiveIntegerField(default=0)  # percentage 0-100
    delay_remarks = models.TextField(blank=True)

    @property
    def delay(self):
        if self.due_date and self.completion < 100:
            today = timezone.now().date()
            delta = (today - self.due_date).days
            return delta if delta > 0 else 0
        return 0

    def __str__(self):
        return f"{self.project_name} - {self.employee}"
