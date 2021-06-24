#include <SoftwareSerial.h>

SoftwareSerial mySerial(2,3); //RX, TX

String ssid = "201212";
String PASSWORD = "03010305";
String host = "118.67.131.29";

void connectWifi()
{ 
    String join ="AT+CWJAP=\""+ssid+"\",\""+PASSWORD+"\"";

    mySerial.println("AT+CWJAP?");
    if(mySerial.find("No Ap"))    
    {
        mySerial.println(join);
    }
    else if(mySerial.find("WIFI CONNECTED")) 
    {
        Serial.print("WIFI connect\n"); 
    } 
    delay(1000); 
} 

 void httpclient()
{ 
    delay(100); Serial.println("connect TCP..."); 
    mySerial.println("AT+CIPSTART=\"TCP\",\""+host+"\",5000"); 
    delay(500); 
    if(Serial.find("ERROR")) 
        return; 
    Serial.println("Send data..."); 
    
    String cmd="GET /farm/farm1/state HTTP/1.1"; 
    mySerial.print("AT+CIPSEND="); 
    mySerial.println(cmd.length()+4); 
    Serial.print("AT+CIPSEND="); 
    Serial.println(cmd.length()+4); 

    if(mySerial.find(">")) 
    { 
        Serial.print(">"); 
    }
    else 
    { 
        mySerial.println("AT+CIPCLOSE"); 
        Serial.println("connect timeout"); 
        delay(1000); 
        return; 
    } 
    delay(500);
    mySerial.println(cmd); 
    Serial.println(cmd); 
    mySerial.println();
    //mySerial.println();
    String temp = ""; // 읽어오는 값 저장소
    for (int i=0; i<3000; i=i+1){
      if (mySerial.available()) { 
        temp += char(mySerial.read());
      }
    }

    //int toggle = temp.indexOf("toggle"); //문자열 적당히 자르기
    //String state = temp.substring(toggle+8, toggle+9); //true면 t만 false면 f만 받아옴
    
    if (temp.indexOf("200")>0){
      Serial.println("스프링쿨러 on!"); //여기에 ledon 적용
    }
    else if (temp.indexOf("204")>0)
    {
      Serial.println("스프링쿨러 off!"); //여기에 ledoff 적용
    }
    if(Serial.find("ERROR"))
        return; 
    mySerial.println("AT+CIPCLOSE"); 
}  

 void posting(){
    delay(100); Serial.println("connect TCP..."); 
    mySerial.println("AT+CIPSTART=\"TCP\",\""+host+"\",5000"); 
    delay(500); 
    if(Serial.find("ERROR")) 
        return; 
    Serial.println("Send data..."); 
    
    //json 문자열 수정해주시면 됩니다.
    String json="{\"farmid\": \"farm1\", \"moisture\": \"44.00\", \"temperature\": \"221.00\", \"humidity\": \"111.00\", \"barometric\": \"99.00\", \"altitude\": \"99.00\", \"datetime\": \"\"}";
    int jsonlen = json.length();
    
    mySerial.print("AT+CIPSEND="); 
    mySerial.println(jsonlen+112); 
    Serial.print("AT+CIPSEND="); 
    Serial.println(jsonlen+112); 

    if(mySerial.find(">")) 
    { 
        Serial.print(">"); 
    }
    else 
    { 
        mySerial.println("AT+CIPCLOSE"); 
        Serial.println("connect timeout"); 
        delay(1000); 
        return; 
    } 
    delay(500);

    mySerial.println("POST /farm/post/ HTTP/1.1");
    mySerial.println("Accept: application/json");
    mySerial.println("Content-Type: application/json");
    mySerial.print("Content-Length: ");
    mySerial.println(json.length());
    mySerial.println();

    mySerial.println(json);
    mySerial.println();
    mySerial.println();
    Serial.println("데이터 전송 완료");
 }
/*void displaySensorDetails(void)
{
  sensor_t sensor;
  bmp.getSensor(&sensor);
  Serial.println("------------------------------------");
  Serial.print  ("Sensor:       "); Serial.println(sensor.name);
  Serial.print  ("Driver Ver:   "); Serial.println(sensor.version);
  Serial.print  ("Unique ID:    "); Serial.println(sensor.sensor_id);
  Serial.print  ("Max Value:    "); Serial.print(sensor.max_value); Serial.println(" hPa");
  Serial.print  ("Min Value:    "); Serial.print(sensor.min_value); Serial.println(" hPa");
  Serial.print  ("Resolution:   "); Serial.print(sensor.resolution); Serial.println(" hPa");  
  Serial.println("------------------------------------");
  Serial.println("");
  delay(500);
}*/

void setup(void) 
{
  Serial.begin(9600);
  mySerial.begin(9600);

  connectWifi(); 
  delay(500);
  //displaySensorDetails();
}

void loop(void) 
{
    posting();
    httpclient(); 

     //Serial.find("+IPD"); 
    Serial.println("\n==================================\n");
    delay(2000); 

  
}
  