from rest_framework import serializers 
from .models import Login
# serializers ==> convert data from data format to json 
class loginserializers(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=('email','password')
class signupserializers(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=('l_name','number','f_name','email','password')