from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from .models import farmdata, farminfo
from .serializers import farmserializer, checkserializer
from pyfcm import FCMNotification
# Create your views here.

API_KEY = "your api key"

class appcheck(APIView): #앱은 json 던짐
    def get(self, request, **kwargs):
        farm = farminfo.objects.get(farmid = kwargs.get('farmid'))
        seriallizer = checkserializer(farminfo.objects.get(farmid=farm))
        temp = seriallizer.data.get('toggle')
        if temp == True:
            return Response(seriallizer.data, status=status.HTTP_200_OK)
        else:
            return Response(seriallizer.data, status=status.HTTP_201_CREATED)

class check(APIView):
    def get(self, request, **kwargs):
        check = kwargs.get('check')
        farm = farminfo.objects.get(farmid = kwargs.get('farmid'))
        if check:
            if check == 'on':
                farm.toggle = True
                farm.save()
                return Response(status=status.HTTP_200_OK)
            elif check == 'off':
                farm.toggle = False
                farm.save()
                return Response(status=status.HTTP_200_OK)
            elif check == 'state':
                seriallizer = checkserializer(farminfo.objects.get(farmid=farm))
                temp = seriallizer.data.get('toggle')
                print(seriallizer.data)
                if temp == True:
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
        

class getfarmdata(APIView):
    TOKEN = ""
    APIKEY = API_KEY
    def post(self, request):
        farm_serial = farmserializer(data = request.data)
        if farm_serial.is_valid():
            farm_serial.save()
            mois = farm_serial.data['moisture']
            if float(mois) < 60:
                print("messaging", mois)
                push_service = FCMNotification(api_key=getfarmdata.APIKEY)
                push_service.notify_single_device(registration_id=getfarmdata.TOKEN, message_title="수분부족 감지!", message_body="현재 수분량 : "+mois, time_to_live=86400)
            return Response(farm_serial.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(farm_serial.data, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, **kwargs):
        farmname = kwargs.get('farmid')
        if farmname == None or len(farmname) < 10:
            seri = farmdata.objects.filter(farmid=farmname).order_by('-datetime') #데이터 하나만 가져옴
            #serializer = farmserializer(seri[0]) #many 어떡할지 결정하기
            serializer = farmserializer(farmdata.objects.all(), many=True)
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            getfarmdata.TOKEN = farmname
            return Response(status=status.HTTP_200_OK)

