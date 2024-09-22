import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@RestController
@RequestMapping("/data")
public class DataController {

    @PostMapping(consumes = MediaType.APPLICATION_FORM_URLENCODED_VALUE)
    public ResponseEntity<String> receiveData(@RequestParam Map<String, String> data) {
        String temperature = data.get("temperature");
        String humidity = data.get("humidity");
        String pressure = data.get("pressure");
        String vibration = data.get("vibration");
        String airQuality = data.get("airQuality");

        // Log the data (in reality, you'd save this to a database)
        System.out.println("Temperature: " + temperature + "°C, Humidity: " + humidity + "%, Pressure: " + pressure + " Pa, Vibration: " + vibration + " g, Air Quality: " + airQuality + " ppm");

        return ResponseEntity.ok("Data received");
    }
}
