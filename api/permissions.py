from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        
        elif request.method == 'POST':
            return request.user.is_authenticated

class UserDetailPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated

class TaskPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        
        elif request.method == 'POST':
            return request.user.is_authenticated

class TaskDetailPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated

class ProjectPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        
        elif request.method == 'POST':
            return request.user.is_authenticated

class ProjectDetailPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_authenticated
