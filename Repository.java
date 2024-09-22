package com.example.smartmaintenance.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.smartmaintenance.model.SensorData;
import org.springframework.stereotype.Repository;
import java.util.List;

// SensorData is the entity class and Long is the type of the primary key
@Repository
public interface SensorDataRepository extends JpaRepository<SensorData, Long> {

    // Custom query methods can be added here
    
    // Example: Find all records with a temperature greater than a certain value
    List<SensorData> findByTemperatureGreaterThan(String temperature);

    // Example: Find all records with a specific air quality
    List<SensorData> findByAirQuality(String airQuality);

    // Example: Find all records within a specific date range
    List<SensorData> findByTimestampBetween(LocalDateTime start, LocalDateTime end);

    // Example: Find all records with vibration above a threshold
    List<SensorData> findByVibrationGreaterThan(String vibration);

    // Example: Find all records sorted by timestamp
    List<SensorData> findAllByOrderByTimestampAsc();
}
