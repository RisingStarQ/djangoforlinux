from django.db import models

# Create your models here.

#继承models.Model 固定写法
class userInfo(models.Model):

	user = models.CharField(max_length = 32)
	pwd = models.CharField(max_length = 32)

	def __str__(self):
		return self.user

'''
多对多练习
'''
class Person(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Group(models.Model):
	name = models.CharField(max_length=128)
	members = models.ManyToManyField(
		Person,
		through='Membership',
		through_fields=('group','person'),
	)

	def __str__(self):
		return self.name

class Membership(models.Model):
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	inviter = models.ForeignKey(
		Person,
		on_delete=models.CASCADE,
		related_name="membership_invites",
	)
	invite_reason = models.CharField(max_length=64)

'''
字段参数的练习
'''
class Student(models.Model):
	FRESHMAN = 'FR'
	SOPHOMORE = 'SO'
	JUNIOR = 'JR'
	SENIOR = 'SR'
	YEAR_IN_SCHOOL_CHOICES = (
		(FRESHMAN, 'Freshman'),
		(SOPHOMORE, 'Sophomore'),
		(JUNIOR, 'Junior'),
		(SENIOR, 'Senior'),
	)
	name = models.CharField(max_length = 10)
	year_in_school = models.CharField(
		max_length = 2,
		choices=YEAR_IN_SCHOOL_CHOICES,
		default=FRESHMAN,
	)

	def is_upperclass(self):
		return self.year_in_school in (self.JUNIOR, self.SENIOR)

	def __str__(self):
		return self.name