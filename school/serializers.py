from rest_framework import serializers
from .models import User, Subject, ClassRoom, Schedule, Grade, Attendance, ActivityLog

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    def validate(self, data):
        teacher = data.get('teacher')
        day = data.get('day_of_week')
        start = data.get('start_time')
        end = data.get('end_time')

        if start and end:
            overlap = Schedule.objects.filter(
                teacher=teacher, day_of_week=day, start_time__lt=end, end_time__gt=start
            ).exists()
            if overlap:
                raise serializers.ValidationError("Schedule conflict: The teacher has another class during this time.")
        return data

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'
        read_only_fields = ['status'] 

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'