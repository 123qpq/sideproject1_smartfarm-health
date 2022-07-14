from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import healthserializer
from .models import healthdata
from pyfcm import FCMNotification

API_KEY = "your api key"

class gethealthdata(APIView):
    TOKEN = ""
    APIKEY = API_KEY
    def post(self, request):
        health_serial = healthserializer(data = request.data)
        if health_serial.is_valid():
            health_serial.save()
            temp = health_serial.data['temperature']
            print(temp)
            if float(temp) < 60:
                print("messaging", temp)
                push_service = FCMNotification(api_key=gethealthdata.APIKEY)
                push_service.notify_single_device(registration_id=gethealthdata.TOKEN, message_title="맥박 이상!", message_body="현재 맥박 : "+temp, time_to_live=86400)
            return Response(health_serial.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(health_serial.data, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, **kwargs):
        healthname = kwargs.get('username')
        if healthname is None or len(healthname) < 10:
            seriallizer = healthserializer(healthdata.objects.all(), many=True)
            return Response(seriallizer.data, status=status.HTTP_200_OK)
        else:
            gethealthdata.TOKEN = healthname
            return Response(status=status.HTTP_200_OK)

