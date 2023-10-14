from django.db import models

# Create your models here.


class Schools(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='photo/%Y/%m/%d/', null=True, blank=None)

    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Student(models.Model):
    first_name = models.CharField('First Name', max_length=32, blank=True,)
    last_name = models.CharField("Last Name", max_length=64,blank=False )
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=25)
    # address = models.ForeignKey(Schools, on_delete=models.CASCADE )
    school = models.ForeignKey(Schools, on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return self.first_name