from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.http import HttpResponse
import csv

User = get_user_model()

class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.employee == request.user

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.select_related('employee').all().order_by('-id')
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ['list_all','export_csv']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Project.objects.select_related('employee').all()
        return Project.objects.filter(employee=user)

    def perform_create(self, serializer):
        # If employee provided (admin), use it; else set to request.user
        if self.request.user.is_staff and serializer.validated_data.get('employee'):
            serializer.save()
        else:
            serializer.save(employee=self.request.user)

    @action(detail=False, methods=['get'])
    def list_all(self, request):
        # admin-only endpoint
        queryset = Project.objects.select_related('employee').all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def export_csv(self, request):
        qs = Project.objects.select_related('employee').all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="projects_export.csv"'
        writer = csv.writer(response)
        writer.writerow(['Employee','Project','Customer','Priority','Quantity','Subtask','Remarks','Due Date','Completion','Delay','Delay Remarks'])
        for p in qs:
            writer.writerow([p.employee.username, p.project_name, p.customer, p.priority, p.quantity, p.subtask, p.remarks, p.due_date, p.completion, p.delay, p.delay_remarks])
        return response
