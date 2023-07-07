from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import JsonResponse
from .models import School
from users.models import SuperManagerUser
from django.db.models import OuterRef, Subquery

from .serializers import SchoolSerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    

    def create(self, request):
       
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check for duplicate entry
        name = serializer.validated_data.get('name')
        phoneNumber  = serializer.validated_data.get('phoneNumber')

        if School.objects.filter(name=name).exists():
            # return Response({'detail': 'School name is taken.'}, status=status.HTTP_409_CONFLICT)
            return JsonResponse({'bool':False, 'msg':'School name is taken.'}) 
        
        if School.objects.filter(phoneNumber= phoneNumber).exists():
            # return Response({'detail': 'School name is taken.'}, status=status.HTTP_409_CONFLICT)
            return JsonResponse({'bool':False, 'msg':'Your tel number  is taken.'}) 
        
        serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'bool':True, 'msg':'Your school registered successfully.'}) 
    

    def retrieve(self, request, pk=None):
        try:
            obj = self.queryset.get(pk=pk)
            serializer = self.serializer_class(obj)
            return Response(serializer.data)
        except School.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=404)
        

    def update(self, request, pk=None):
        try:
            obj = self.queryset.get(pk=pk)
            serializer = self.serializer_class(obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except School.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=404)   


    def partial_update(self, request, pk=None):
        try:
            obj = self.queryset.get(pk=pk)
            serializer = self.serializer_class(obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except School.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=404)  
        

    def destroy(self, request, pk=None):
        try:
            obj = self.queryset.get(pk=pk)
            obj.delete()
            return Response(status=204)
        except School.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=404)    
        

    def schools_without_headmaster(self, request):

        schools_without_headmaster = School.objects.exclude(
            id__in=Subquery(
                SuperManagerUser.objects.values('school_id')
            )
        )

     # Serialize the schools without headmaster
        serialized_schools = [{'id': school.id, 'name': school.name} for school in schools_without_headmaster]

        return Response(serialized_schools)


