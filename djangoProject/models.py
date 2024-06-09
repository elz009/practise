from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=22)



class lesson(models.Model):
    name = models.CharField(max_length=22)

class students(models.Model):
    name =models.Value(max(100))

class scheduale(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    )

class group(models.Model):
    name = models.CharField(max_length=20)