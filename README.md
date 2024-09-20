# IoT-Based Smart Maintenance System with Predictive Maintenance

This repository contains the source code for a **Smart Maintenance System** built using IoT technologies. It monitors sensor data (temperature, humidity, pressure, vibration, and air quality) and predicts maintenance needs using machine learning algorithms. The system integrates IoT devices, cloud computing, and a predictive maintenance algorithm for real-time data monitoring and analytics.

## Project Overview

This project is designed to:
- Collect real-time sensor data using **DHT22**, **BMP180**, **MPU6050**, and **MQ-135** sensors.
- Transmit data wirelessly using **ESP8266** to a Spring Boot backend.
- Process and store data on the backend and display it in a real-time **React Dashboard**.
- Implement a **Predictive Maintenance Model** using a **Random Forest Classifier** to predict when maintenance is required.
- Integrate with **AWS IoT Core** for cloud-based data storage and analysis.

### Components

#### **1. Hardware (Arduino-based IoT System)**

- **DHT22**: Measures temperature and humidity.
  - Pin Configuration: VCC -> 3.3V, Data -> GPIO 2, GND -> Ground
- **BMP180**: Measures atmospheric pressure.
  - Pin Configuration: VCC -> 3.3V, SDA -> GPIO 4, SCL -> GPIO 5, GND -> Ground
- **MPU6050**: Measures vibration via accelerometer and gyroscope.
  - Pin Configuration: VCC -> 3.3V, SDA -> GPIO 4, SCL -> GPIO 5, GND -> Ground (shared I2C with BMP180)
- **MQ-135**: Measures air quality (e.g., CO2 levels).
  - Pin Configuration: VCC -> 5V, Analog Out -> A0 (analog input pin on ESP8266)

- **ESP8266**: Wi-Fi module for wireless data transmission.
  - Pin Configuration: TX -> RX, RX -> TX, VCC -> 3.3V, GND -> Ground

#### **2. Backend (Spring Boot Application)**
The backend receives sensor data via HTTP, processes it, and stores it in a database. It also provides APIs for the real-time dashboard to display the data.

Key Features:
- **Repository Class**: Handles database interaction for sensor data.
- **Controller Class**: Exposes REST endpoints to accept incoming data.
  - Example Endpoint: `/data` (POST request to receive sensor data)

#### **3. Real-Time Monitoring Dashboard (React Application)**
A dashboard built using **React** displays real-time sensor data from the backend.
- **Features**:
  - Displays temperature, humidity, pressure, vibration, and air quality in tabular form.
  - Auto-refreshes every 30 seconds for real-time monitoring.
  - Error handling and loading states for smooth user experience.

##### Example Sensor Table (from the dashboard):
```
| Temperature (°C) | Humidity (%) | Pressure (Pa) | Vibration (g) | Air Quality (ppm) | Timestamp               |
|------------------|--------------|---------------|---------------|-------------------|-------------------------|
| 24.5°C           | 60.3%        | 101325        | 0.5           | 400               | 2024-09-18 12:34:56     |
| 24.6°C           | 60.5%        | 101300        | 0.6           | 450               | 2024-09-18 12:35:06     |
```

#### **4. Machine Learning Predictive Maintenance**
The **Random Forest Classifier** is used to predict whether maintenance is needed based on the sensor data.

##### **Algorithm**:
- **Input Features**:
  - Temperature, Vibration, Pressure, Air Quality
- **Target**:
  - Maintenance Needed (1 for Yes, 0 for No)
- **Steps**:
  - Train/test split (80/20).
  - Model training with a Random Forest Classifier.
  - Evaluate model accuracy and generate a classification report.

##### **Model Output Example**:
```
Accuracy: 92.5%
```

#### **5. AWS IoT Core Integration**
Sensor data is integrated with **AWS IoT Core** for cloud-based analysis and storage. The data structure follows the below JSON format:

```json
{
  "temperature": 24.5,
  "humidity": 60.3,
  "pressure": 101325,
  "vibration": 0.5,
  "airQuality": 400,
  "timestamp": "2024-09-18T12:34:56Z"
}
```

### System Flow

1. **Data Collection**: IoT sensors collect data (temperature, humidity, pressure, vibration, air quality).
2. **Transmission**: Data is transmitted via ESP8266 to the backend.
3. **Backend Processing**: Spring Boot application logs and stores data.
4. **Dashboard Monitoring**: React dashboard visualizes real-time sensor data.
5. **Predictive Maintenance**: Machine learning model predicts maintenance needs.
6. **Cloud Storage**: AWS IoT Core stores and processes the sensor data for cloud-based analytics.

### Pin Configuration Summary

| Sensor     | Pins Used                  |
|------------|----------------------------|
| DHT22      | VCC -> 3.3V, Data -> GPIO 2 |
| BMP180     | VCC -> 3.3V, SDA -> GPIO 4, SCL -> GPIO 5 |
| MPU6050    | VCC -> 3.3V, SDA -> GPIO 4, SCL -> GPIO 5 |
| MQ-135     | VCC -> 5V, Analog Out -> A0 |

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/smart-maintenance-system.git
   cd smart-maintenance-system
   ```

2. **Install Backend Dependencies**:
   ```bash
   cd backend
   mvn clean install
   ```

3. **Install Frontend Dependencies**:
   ```bash
   cd frontend
   npm install
   ```

4. **Deploy Arduino Code**:
   - Open `arduino_code.ino` in the Arduino IDE and upload to your ESP8266.

5. **Run the Backend**:
   ```bash
   mvn spring-boot:run
   ```

6. **Run the React Dashboard**:
   ```bash
   npm start
   ```

7. **Model Training (Optional)**:
   If you want to retrain the predictive maintenance model, run the `predictive_maintenance.py` file.
   ```bash
   python predictive_maintenance.py
   ```

### Output

**Arduino Serial Monitor**:
```
Connecting to WiFi...
Sending data: Temperature = 24.5°C, Humidity = 60.3%, Pressure = 101325 Pa, Vibration = 0.5 g, Air Quality = 400 ppm
```

**Spring Boot Logs**:
```
2024-09-18 12:34:56 INFO  Temperature: 24.5°C, Humidity: 60.3%, Pressure: 101325 Pa, Vibration: 0.5 g, Air Quality: 400 ppm
```

**AWS IoT Core Output**:
```json
{
  "temperature": 24.5,
  "humidity": 60.3,
  "pressure": 101325,
  "vibration": 0.5,
  "airQuality": 400,
  "timestamp": "2024-09-18T12:34:56Z"
}
```

---

### Conclusion
Feel free to fork this repository and submit pull requests. Contributions are welcome! If you have suggestions or improvements, please let me know and researchers are requested to use this block of code in their respective projects. Feel free to customize the script according to your requirements, especially the credentials and other API details. I hope this helps, thank you.



---

