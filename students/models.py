from django.db import models

# Create your models here.
class Schools(models.Model):
    school_name = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    schoolLogo = models.FileField(upload_to='images/', null=True)

    def __str__(self):
        return self.school_name

class Students(models.Model):
    firstname =models.CharField(max_length=200, null=False)
    lastname =models.CharField(max_length=200, null=False)
    about = models.TextField(max_length=1000, null=False)
    course = models.CharField(max_length=100, null=False)
    parents_name = models.CharField(max_length=100)
    district = models.CharField(max_length=100, null=False)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname