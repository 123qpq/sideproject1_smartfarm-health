from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import account
from .serializers import accountserializer
# Create your views here.

class signup(APIView):
    def post(self, request):
        temp = request.data['username']
        if account.objects.all().filter(username = temp):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            user_serial = accountserializer(data = request.data)
            if user_serial.is_valid():
                user_serial.save()
                return Response(status=status.HTTP_201_CREATED)
            else: 
                return Response(user_serial.data, status=status.HTTP_400_BAD_REQUEST)

class signin(APIView):
    def post(self, request):
        checkuser = request.data['username']
        checkpwd = request.data['pwd']
        accountcheck = account.objects.all().filter(username = checkuser, pwd = checkpwd)
        if accountcheck:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

