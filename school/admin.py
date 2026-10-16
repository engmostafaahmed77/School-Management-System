from django.contrib import admin
from .models import User, Subject, ClassRoom, Schedule, Grade, Attendance, ActivityLog

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(ClassRoom)
admin.site.register(Schedule)
admin.site.register(Grade)
admin.site.register(Attendance)
admin.site.register(ActivityLog)
