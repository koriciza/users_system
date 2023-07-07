from django.urls import include, path
from rest_framework import routers
from school.views import SchoolViewSet

router = routers.DefaultRouter()
router.register(r'schools', SchoolViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path(r'schools-without-headmaster/', SchoolViewSet.as_view({'get': 'schools_without_headmaster'})),
]
