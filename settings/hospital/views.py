from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from .filter import DoctorsSpecialityFilterSet
from .permissions import IsNotPatientForDoctorAccess
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = JsonResponse({'detail': 'Successfully registered.'})
        response.set_cookie(
            key='auth_token',
            value=user.token,
            httponly=True,
            secure=False,
            samesite='Lax'
        )
        return response


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        response = JsonResponse({'detail': 'Successfully logged in.'})

        response.set_cookie(
            key='auth_token',
            value=user.token,
            httponly=True,
            secure=False,
            samesite='Lax'
        )
        return response


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = JsonResponse({'detail': 'Successfully logged out.'})
        response.delete_cookie('auth_token')
        return response


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, IsNotPatientForDoctorAccess]
    filterset_class = DoctorsSpecialityFilterSet

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class AppointmentHistoryViewSet(viewsets.ModelViewSet):
    queryset = AppointmentHistory.objects.all()
    serializer_class = AppointmentHistorySerializer
    permission_classes = [IsNotPatientForDoctorAccess, IsAuthenticated]

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsNotPatientForDoctorAccess ,IsAuthenticated]