#include <SoftwareSerial.h> 

SoftwareSerial GPRS(7, 8);
unsigned char buffer[64];
String longitude = "";
String latitude = "";
String latitudeLongitude ="";
String domain = "http://282f85fc.ngrok.io/";
String completeUrl= domain + "insere_coordenada/veiculo/";
String fullUrl = "";
int leitura = 0;
const int ledPinGreen = 12;
const int ledPinRed = 13;
const int portaStatus = 11;
int count =0;

void setup()
{
  GPRS.begin(9600);               // the GPRS baud rate   
  Serial.begin(9600);             // the Serial port of Arduino baud rate.     
  pinMode(portaStatus, INPUT);
  pinMode(ledPinGreen, OUTPUT);
  pinMode(ledPinRed, OUTPUT);
  initDefaultConfig();
}

void loop()
{
leitura = digitalRead(portaStatus);
if (leitura == 0 )
{
  digitalWrite(ledPinGreen,HIGH);
  digitalWrite(ledPinRed,LOW);
}
else
{
  digitalWrite(ledPinGreen,LOW);
  digitalWrite(ledPinRed,HIGH);
  GPRS.println("AT+CIPGSMLOC=1,1\r\n");
  delay(5000);
  String gsm_input="";
  while(GPRS.available()!=0) 
  {
    gsm_input+= (char (GPRS.read()));
  }
  latitudeLongitude = "";
  latitude = "";
  longitude = "";
  String latitude = getValue(gsm_input, ',', 3);
  String longitude = getValue(gsm_input, ',', 2);
  String latitudeLongitude = latitude +"/"+ longitude;
  String fullUrl = completeUrl +latitudeLongitude+"/1/";
  String command_httppara ="AT+HTTPPARA=\"URL\"";
  String command_complete = command_httppara + ",\"" + fullUrl +"\"";
  char *command_at = const_cast<char*>(command_complete.c_str());
  Serial.println(command_complete);
  Serial.println(command_at);
  GPRS.println(command_at);
  delay(500);
  ShowSerialData();
  GPRS.println("AT+HTTPACTION=0");
  delay(5000);
  ShowSerialData();
  sendSMS();
}
}
void initDefaultConfig()
{
  GPRS.println("AT+CSQ"); 
  delay(1000);
  ShowSerialData();
  GPRS.println("AT+CGATT?");
  delay(1000);
  ShowSerialData();
  GPRS.println("AT+SAPBR=3,1,\"Contype\",\"GPRS\"");
  delay(1000);
  ShowSerialData();
  GPRS.println("AT+SAPBR=3,1,\"APN\",\"www\"");
  delay(4000);
  ShowSerialData();
  GPRS.println("AT+SAPBR=1,1");
  delay(2000);
  ShowSerialData();
  GPRS.println("AT+SAPBR=2,1");
  delay(2000);
  ShowSerialData();
  GPRS.println("AT+HTTPSSL=0");
  delay(2000);
  ShowSerialData();
  GPRS.println("AT+HTTPINIT");
  delay(2000);
  ShowSerialData();
  GPRS.println("AT+HTTPPARA=\"CID\",1");
  delay(2000);
  ShowSerialData();
}

void sendSMS()
{
  GPRS.println("AT+CMGF=1\r");
  delay(500);
  ShowSerialData();
  GPRS.println("AT+CMGS=\"+5511967635977\"");
  delay(500);
  ShowSerialData();
  GPRS.println("Temos uma ocorrencia no transporte por favor acesse: www.lit-river-31314.herokuapp.com");
  delay(500);
  ShowSerialData();
  GPRS.println((char)26);
  delay(500);
  ShowSerialData();
  delay(500);
  Serial.println("Mensagem SMS enviada");
}

void ShowSerialData()
{
  while(GPRS.available()!=0)
    Serial.write(char (GPRS.read()));
}

String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}
