from rest_framework.permissions import BasePermission

class IsNotPatientForDoctorAccess(BasePermission):
    def has_permission(self, request, view):
        try:
            model_name = view.get_queryset().model.__name__
        except Exception:
            return True

        if model_name in ['Doctor', 'AppointmentHistory', 'Bill']:
            return getattr(request.user, 'role', None) != 'Пациент'
        return True