#include <ESP8266WiFi.h>
#include <DHT.h>         // For DHT22 sensor
#include <Wire.h>
#include <Adafruit_BMP085.h> // For BMP180 pressure sensor
#include <MPU6050.h>      // For accelerometer and gyroscope
#include <MQ135.h>        // For air quality sensor (CO2 levels)

// Wi-Fi credentials
const char* ssid = "Your_SSID";
const char* password = "Your_Password";

// Server URL
const char* server = "http://your-backend-server.com/data";

// Sensor pins
#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
Adafruit_BMP085 bmp;
MPU6050 mpu;
MQ135 gasSensor(A0);

WiFiClient client;

void setup() {
  Serial.begin(115200);
  
  // Initialize sensors
  dht.begin();
  bmp.begin();
  mpu.initialize();
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  // Read sensor data
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  float pressure = bmp.readPressure();
  float vibration = mpu.getAccelerationX(); // Simplified example (X-axis vibration)
  float airQuality = gasSensor.getPPM(); // CO2 level
  
  // Check Wi-Fi connection and send data
  if (WiFi.status() == WL_CONNECTED) {
    if (client.connect(server, 80)) {
      String data = "temperature=" + String(temperature) + 
                    "&humidity=" + String(humidity) + 
                    "&pressure=" + String(pressure) + 
                    "&vibration=" + String(vibration) + 
                    "&airQuality=" + String(airQuality);
                    
      client.println("POST /data HTTP/1.1");
      client.println("Host: your-backend-server.com");
      client.println("Content-Type: application/x-www-form-urlencoded");
      client.println("Content-Length: " + String(data.length()));
      client.println();
      client.println(data);
      client.stop();
    }
  }

  delay(10000); // Send data every 10 seconds
}
