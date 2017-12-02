#include <SoftwareSerial.h> 

SoftwareSerial GPRS(7, 8);
unsigned char buffer[64]; // buffer array for data recieve over serial port
int count=0;     // counter for buffer array 

void setup()
{
  GPRS.begin(9600);               // the GPRS baud rate   
  Serial.begin(9600);             // the Serial port of Arduino baud rate.     
  initDefaultConfig();
}

void loop()
{
      
}
void clearBufferArray()              // function to clear buffer array
{
  for (int i=0; i<count;i++)
    { buffer[i]=NULL;}                  
}

void initDefaultConfig()
{
  GPRS.println("AT+CSQ"); // Signal quality check

  delay(1000);
 
  ShowSerialData();// this code is to show the data from gprs shield, in order to easily see the process of how the gprs shield submit a http request, and the following is for this purpose too.
  
  GPRS.println("AT+CGATT?"); //Attach or Detach from GPRS Support
  delay(1000);
 
  ShowSerialData();
  
  GPRS.println("AT+SAPBR=3,1,\"Contype\",\"GPRS\"");//setting the SAPBR, the connection type is using gprs
  delay(1000);
 
  ShowSerialData();
 
  GPRS.println("AT+SAPBR=3,1,\"APN\",\"www\"");//setting the APN, Access point name string
  delay(4000);
 
  ShowSerialData();
 
  GPRS.println("AT+SAPBR=1,1");//setting the SAPBR
  delay(2000);

  ShowSerialData();
 
  GPRS.println("AT+SAPBR=2,1");//setting the SAPBR
  delay(2000);
  ShowSerialData();
  getLongLat();
}

void getLongLat()
{
  GPRS.println("AT+CIPGSMLOC=1,1");//setting the SAPBR
  delay(4000);
  ShowSerialData();
}

void ShowSerialData()
{
  while(GPRS.available()!=0)
    Serial.write(char (GPRS.read()));
}
