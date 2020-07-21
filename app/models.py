from django.db import models

# Create your models here.
class Entery(models.Model):
	face_id = models.CharField(max_length=3)
	name = models.CharField(max_length=50)
	card_no = models.CharField(max_length=16)
	pin = models.CharField(max_length=4)

	def __str__(self):
		return self.name

class Balance(models.Model):
	Entery = models.ForeignKey(Entery,on_delete=models.CASCADE)
	balance = models.CharField(max_length=100000)
