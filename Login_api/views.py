from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from  .models import Login
from .serializers import loginserializers,signupserializers
from rest_framework.views import APIView
from django.contrib.auth.hashers import  make_password
# Create your views here.
# CLASS BASED VIEWS 
class login (APIView):
    def post(self,request):
        serializers=loginserializers(data=request.data)
        if serializers.is_valid():
            email=serializers.validated_data.get('email')
            password=serializers.validated_data.get('password')
            
            user=Login.objects.filter(email=email).first()
            if user is None:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            if user.password !=password:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            return Response({'massege':"login sucsses" },status=status.HTTP_200_OK)



class Signup(APIView):
    def post(self,request):
        serializers=signupserializers(data=request.data)

        if serializers.is_valid():
            email = serializers.validated_data.get('email')
            password=serializers.validated_data.get('password')
        
            if '@' not in email or'.com' not in email:
                return Response({"error":"invaild email"},status.HTTP_400_BAD_REQUEST)
            if len(password) < 8:
                return Response({"error":"Password must be at least 8 characters"}, status=status.HTTP_400_BAD_REQUEST)
            serializers.validated_data['password'] = make_password(password)
            serializers.save()
            return Response({"message":"Signup successful"}, status=status.HTTP_201_CREATED)


        


