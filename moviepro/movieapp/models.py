from django.db import models

# Create your models here.
class Load(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField()
    year=models.DateField()
    img=models.ImageField(upload_to='gallary')
    def __str__(self):
        return self.name