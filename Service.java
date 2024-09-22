package com.example.smartmaintenance.service;

import com.example.smartmaintenance.model.SensorData;
import com.example.smartmaintenance.repository.SensorDataRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class SensorDataService {

    private final SensorDataRepository repository;

    public SensorDataService(SensorDataRepository repository) {
        this.repository = repository;
    }

    public List<SensorData> getAllSensorData() {
        return repository.findAll();
    }

    public SensorData saveSensorData(SensorData sensorData) {
        return repository.save(sensorData);
    }

    public SensorData getSensorDataById(Long id) {
        return repository.findById(id).orElseThrow(() -> new IllegalArgumentException("Sensor data not found"));
    }
}
