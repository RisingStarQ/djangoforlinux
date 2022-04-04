from django.db import models

# Create your models here.

#继承models.Model 固定写法
class userInfo(models.Model):

	user = models.CharField(max_length = 32)
	pwd = models.CharField(max_length = 32)

	def __str__(self):
		return self.user