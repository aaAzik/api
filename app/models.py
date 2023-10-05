from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.username
    
class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    members = models.ManyToManyField(User, related_name="members_project")

    def __str__(self):
        return self.title
    
class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    deadline_date = models.DateField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    asigned_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title