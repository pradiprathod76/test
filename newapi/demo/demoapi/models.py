from django.db import models

# Create your models here.
sub = (
    ('yearly', 'YEARLY'),
    ('monthly', 'MONTHLY'),
)
class Category(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    des = models.TextField()


    def __str__(self):
        return self.name


class Audio(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    des = models.TextField()
    audio = models.FileField(upload_to='audio/')
    cg = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='cg_audio', null=True, blank=True)
    sub = models.CharField(max_length=10, choices=sub, default='MONTHLY')
    date = models.DateField()
    def __str__(self):
        return self.name