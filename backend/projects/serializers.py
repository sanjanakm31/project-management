from rest_framework import serializers
from .models import Project
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','is_staff']

class ProjectSerializer(serializers.ModelSerializer):
    employee = UserSerializer(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='employee', write_only=True, required=False)
    delay = serializers.IntegerField(read_only=True)

    class Meta:
        model = Project
        fields = ['id','employee','employee_id','project_name','customer','priority','quantity','subtask','remarks','due_date','completion','delay','delay_remarks']
