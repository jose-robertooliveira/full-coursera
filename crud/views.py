from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from rest_framework import viewsets
#from django.shortcuts import get_list_or_404

from .models import User, Instructor
from .serializers import UserSerializer, InstructorSerializer


class UserMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        return self.list(request, *args, **kwargs)

mixin_view = UserMixinView.as_view()

# class InstructorMixinView(mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Instructor.objects.all()
#     serializer_class = InstructorSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#mixin_view = InstructorMixinView.as_view()

#####################################################


# class UserListAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# user_list_view = UserListAPIView.as_view()

# @api_view(['GET'])
# def list_view(request, *args, **kwargs):
#     method = request.method
#     if method == "GET":
#         queryset = User.objects.all()
#         data = UserSerializer(queryset, many=True).data
#         return Response(data)




# class UserViewSet(viewsets.ViewSet):
#     """ 
#     A ViewSet for viewing all the datas 
#     """
#     queryset = User.objects.all()

#     def list(self, request):
#         serializer = UserSerializer(self.queryset, many=True)
#         return Response(serializer.data)
