from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from healthcare.views import PatientViewSet, DoctorViewSet, MappingViewSet, RegisterView, LoginView

router = DefaultRouter()
router.register('patients', PatientViewSet, basename='patients')
router.register('doctors', DoctorViewSet, basename='doctors')
router.register('mappings', MappingViewSet, basename='mappings')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
]
