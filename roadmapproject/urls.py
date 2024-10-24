from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from roadmapapi.views.users import UserViewSet
from roadmapapi.views.projects import ProjectViewSet
from roadmapapi.views.assignments import AssignmentViewSet
from roadmapapi.views.milestones import MilestoneViewSet
from roadmapapi.views.goals import GoalViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, basename='user')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'assignments', AssignmentViewSet, basename='assignment')
router.register(r'milestones', MilestoneViewSet, basename='milestone')
router.register(r'goals', GoalViewSet, basename='goal')  

urlpatterns = [
    path('', include(router.urls)),
    path('login', UserViewSet.as_view({'post': 'user_login'}), name='login'),
    path('register', UserViewSet.as_view({'post': 'register_account'}), name='register'),

    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'register_account'})),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('projects/', ProjectViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('projects/<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('assignments/', AssignmentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('assignments/<int:pk>/', AssignmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('milestones/', MilestoneViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('milestones/<int:pk>/', MilestoneViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('goals/', GoalViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('goals/<int:pk>/', GoalViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
