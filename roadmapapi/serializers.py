from rest_framework import serializers
from django.contrib.auth.models import User
from roadmapapi.models import Project, assignment
from roadmapapi.models import Assignment

# *** Users ***
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

# *** Projects ***
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

# *** Assignments ***
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'project', 'user', 'role']