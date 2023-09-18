from django.db import models

# Create your models here.
class MoM(models.Model):
 
    title = models.CharField(max_length = 80)
    pdf = models.FileField(upload_to='pdfs/')
 
    class Meta:
        ordering = ['title']
     
    def __str__(self):
        return f"{self.title}"

class Task(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    task = models.CharField(max_length=200)
    task_description = models.TextField()
    deadline = models.CharField(max_length=30)

    def __str__(self):
        return self.name