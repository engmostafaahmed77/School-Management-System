from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView, SubjectViewSet, ClassRoomViewSet, 
    ScheduleViewSet, GradeViewSet, AttendanceViewSet, ActivityLogViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'classes', ClassRoomViewSet, basename='class')
router.register(r'schedules', ScheduleViewSet, basename='schedule')
router.register(r'grades', GradeViewSet, basename='grade')
router.register(r'attendances', AttendanceViewSet, basename='attendance')
router.register(r'logs', ActivityLogViewSet, basename='log')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]