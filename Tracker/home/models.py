from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.TextField()
    contact = models.Integer(max_length=200, null=True)
    address = models.TextField(max_length=200, null=True)
    symptoms = models.TextField()
    
    def __str__(self):
        return 'User #{}'.format(self.id)
    
    class Meta:
        verbose_name_plural = 'users'