from django.contrib import admin
from .models import userInfo, Person, Group, Membership, Student

# Register your models here.
#若要在后台系统看到用户应用，必须先在admin中进行注册，告诉admin站点，请将userinfo的模型加入站点内，接受站点的管理。
admin.site.register(userInfo)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Student)