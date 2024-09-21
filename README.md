# IoT-Based Smart Maintenance System with Predictive Maintenance for Airline Applications

This repository contains the source code for a **Smart Maintenance System** built using IoT technologies and machine learning for **aircraft maintenance** in the airline industry. The system monitors key sensor data related to **aircraft health** (temperature, pressure, vibration, and air quality). It uses predictive algorithms to foresee **maintenance needs**, preventing costly downtime or in-flight issues.

## Project Overview

This project is designed specifically to:
- **Monitor critical aircraft systems** in real-time using IoT sensors.
- Collect sensor data such as **temperature**, **vibration**, **pressure**, and **air quality** from different parts of an aircraft (e.g., engine, cabin, fuselage).
- **Predict potential maintenance issues** using machine learning algorithms before they become critical failures.
- **Transmit data wirelessly** to a backend system using the **ESP8266** Wi-Fi module and display the data in real-time on a **React Dashboard**.
- **Integrate with AWS IoT Core** to store and analyze data in the cloud for further insights and reporting.

This solution aims to improve **safety, efficiency**, and **maintenance scheduling** for airline operations, helping avoid unexpected downtime and ensuring the fleet's operational health.

### Example Use Case in the Airline Industry:

1. **Monitoring Aircraft Engines**:
   - By placing vibration and pressure sensors near the aircraft engines, the system can continuously monitor engine performance. Any **excessive vibrations** or abnormal temperature readings could indicate potential wear or mechanical issues.
   
2. **Cabin Air Quality Monitoring**:
   - Sensors like **MQ-135** monitor air quality in the cabin, ensuring that **CO2 levels** or other harmful gases do not exceed safe levels, improving passenger safety and comfort.
   
3. **Landing Gear Health**:
   - The system can be integrated with the **landing gear** to monitor its performance during take-off and landing, detecting any unusual vibrations or pressure changes that may point to future failures.

---

## Project Components

### **1. Hardware (Arduino-based IoT System)**

The IoT system utilizes the following hardware components for real-time data collection:
- **DHT22**: Measures temperature and humidity (used in engine and cabin monitoring).
  - Pin Configuration: VCC -> 3.3V, Data -> GPIO 2, GND -> Ground
- **BMP180**: Measures atmospheric pressure (useful for monitoring engine and cabin pressure changes).
  - Pin Configuration: VCC -> 3.3V, SDA -> GPIO 4, SCL -> GPIO 5, GND -> Ground
- **MPU6050**: Measures vibration via accelerometer and gyroscope (used in engine and landing gear monitoring).
  - Pin Configuration: VCC -> 3.3V, SDA -> GPIO 4, SCL -> GPIO 5, GND -> Ground (shared I2C with BMP180)
- **MQ-135**: Measures air quality and gas levels (e.g., CO2 levels inside the cabin).
  - Pin Configuration: VCC -> 5V, Analog Out -> A0 (analog input pin on ESP8266)

- **ESP8266**: Wi-Fi module used for wirelessly transmitting the sensor data to the backend system.
  - Pin Configuration: TX -> RX, RX -> TX, VCC -> 3.3V, GND -> Ground

### **2. Backend (Spring Boot Application)**

The backend processes the sensor data and stores it for real-time monitoring and predictive analysis. It serves as the central control for data collection, processing, and visualization.
- **Controller Class**: Receives sensor data via REST APIs.
- **Repository Class**: Manages the database interaction and stores the data.
- **Data Flow**: Data is processed and logged, with real-time alerts being sent in case any parameter exceeds its safety threshold.

### **3. Real-Time Aircraft Monitoring Dashboard (React Application)**

The **React-based dashboard** provides real-time visualizations of the sensor data collected from the aircraft. Airline maintenance teams can monitor:
- **Temperature**, **Vibration**, **Pressure**, and **Air Quality** across different parts of the aircraft.
- The dashboard auto-refreshes every 30 seconds, ensuring up-to-date information.
- Potential maintenance alerts are displayed based on thresholds set by the airline's maintenance team.

Example dashboard output:
```
| Temperature (°C) | Humidity (%) | Pressure (Pa) | Vibration (g) | Air Quality (ppm) | Timestamp               |
|------------------|--------------|---------------|---------------|-------------------|-------------------------|
| 24.5°C           | 60.3%        | 101325        | 0.5           | 400               | 2024-09-18 12:34:56     |
| 24.6°C           | 60.5%        | 101300        | 0.6           | 450               | 2024-09-18 12:35:06     |
```

### **4. Machine Learning Predictive Maintenance**

The system implements **predictive maintenance** using a **Random Forest Classifier**. By analyzing historical sensor data, the system predicts whether maintenance is required, allowing airlines to:
- Avoid unscheduled maintenance by predicting issues ahead of time.
- **Optimize fleet availability** by scheduling maintenance at the right time.
- Ensure **safety compliance** by identifying issues before they turn into critical problems.

### **5. AWS IoT Core Integration**

AWS IoT Core is used for cloud storage and processing, allowing airlines to **analyze large volumes of aircraft data**. The data is transmitted in JSON format and stored for real-time or historical analysis. This can be used for generating maintenance reports, compliance checks, and ensuring the overall health of the fleet.

Example JSON data sent to AWS IoT Core:
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

## Project Flow for Airline Maintenance

1. **Data Collection**:
   - IoT sensors are deployed across critical components of the aircraft, such as engines, cabin, and landing gear.
   
2. **Data Transmission**:
   - The **ESP8266 Wi-Fi module** transmits real-time data to the backend system.

3. **Backend Processing**:
   - The Spring Boot backend processes and stores the data. In the event of abnormal readings (e.g., high engine vibrations or poor air quality), alerts are triggered and displayed on the dashboard.
   
4. **Real-Time Monitoring**:
   - The **React Dashboard** displays the data to the maintenance team, helping them track the aircraft's operational health. Any potential failures are flagged in real time.

5. **Predictive Maintenance**:
   - The machine learning model predicts potential failures based on historical data, allowing airlines to schedule maintenance at the optimal time, avoiding unplanned repairs or failures during flights.

6. **Cloud Storage & Analytics**:
   - AWS IoT Core stores the data for further analysis, compliance reporting, and historical tracking.

---

## Example Pin Configuration Summary

| Sensor     | Pins Used                  |
|------------|----------------------------|
| DHT22      | VCC -> 3.3V, Data -> GPIO 2 |
| BMP180     | VCC -> 3.3V, SDA -> GPIO 4, SCL -> GPIO 5 |
| MPU6050    | VCC -> 3.3V, SDA -> GPIO 4, SCL -> GPIO 5 |
| MQ-135     | VCC -> 5V, Analog Out -> A0 |

---

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/smart-aircraft-maintenance-system.git
   cd smart-aircraft-maintenance-system
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
   - Open `arduino_code.ino` in the Arduino IDE and upload it to your ESP8266.

5. **Run the Backend**:
   ```bash
   mvn spring-boot:run
   ```

6. **Run the React Dashboard**:
   ```bash
   npm start
   ```

7. **Model Training (Optional)**:
   To retrain the predictive maintenance model, run the `predictive_maintenance.py` script:
   ```bash
   python predictive_maintenance.py
   ```

### Conclusion 
Feel free to customize the script according to your requirements, especially the API, credentials, and other personal details. Contributions are welcome! If you have suggestions or improvements, please let me know and researchers are requested to use this block of code in their respective projects. I hope this helps, thank you.
