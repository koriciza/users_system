from django.urls import include, path
from rest_framework import routers
from .views import (
    SuperManagerUserViewSet,
      SuperAdminUserViewSet, 
      StudentUserViewSet,
      ParentUserViewSet,
      EmployeeUserViewSet,
      SchoolEmployeesViewSet,
      UserCheckingViewSet
      )

router = routers.DefaultRouter()

router.register(r'super-admin-users', SuperAdminUserViewSet)
router.register(r'super-manager-users', SuperManagerUserViewSet)
router.register(r'student-users', StudentUserViewSet)
router.register(r'parent-users', ParentUserViewSet)
router.register(r'employee-users', EmployeeUserViewSet)
# router.register(r'school-employee-list/<int:school>/', SchoolEmployeesViewSet, basename='school_employee_list')

urlpatterns = [
    path('', include(router.urls)),
    path(r'school-employee-list/<int:school>/', SchoolEmployeesViewSet.as_view({'get': 'school_employee_list'})),
    path(r'check-user-username/<username>/', UserCheckingViewSet.as_view({'get': 'checkUsername'})),
    path(r'check-user-email/<email>/', UserCheckingViewSet.as_view({'get': 'checkUserEmail'})),
    path(r'check-superManagerUser-phone/<phone_number>/', UserCheckingViewSet.as_view({'get': 'checkSuperManagerUserPhone'})),
]