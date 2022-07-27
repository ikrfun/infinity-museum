from django.db import models
# from pyxel import input_keys, input_text

# Create your models here.
class Image(models.Model):
	input_text = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	image = models.ImageField()
	def __str__(self):
		return self.input_text