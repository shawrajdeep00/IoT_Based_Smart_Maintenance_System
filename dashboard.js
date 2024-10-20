import React, { useState, useEffect } from 'react';
import './App.css';  // For styling

function App() {
  const [sensorData, setSensorData] = useState([]);
  const [loading, setLoading] = useState(true); // Loading state
  const [error, setError] = useState(null); // Error state

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://your-backend-server.com/sensor-data");

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        setSensorData(data);
      } catch (err) {
        setError(err.message);  // Set error message
      } finally {
        setLoading(false);  // Stop loading once data is fetched
      }
    };

    // Call the function to fetch data
    fetchData();

    // Optional: Auto-refresh data every 30 seconds
    const intervalId = setInterval(fetchData, 30000);
    return () => clearInterval(intervalId); // Clean up interval on component unmount
  }, []);

  // Display loading message
  if (loading) {
    return <div className="App"><h1>Loading data...</h1></div>;
  }

  // Display error message if fetch failed
  if (error) {
    return <div className="App"><h1>Error fetching data: {error}</h1></div>;
  }

  // Display the dashboard once data is loaded
  return (
    <div className="App">
      <h1>Real-time Aircraft Monitoring Dashboard</h1>
      <table className="sensor-table">
        <thead>
          <tr>
            <th>Temperature (°C)</th>
            <th>Humidity (%)</th>
            <th>Pressure (Pa)</th>
            <th>Vibration (g)</th>
            <th>Air Quality (ppm)</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {sensorData.map((data) => (
            <tr key={data.id}>
              <td>{data.temperature}</td>
              <td>{data.humidity}</td>
              <td>{data.pressure}</td>
              <td>{data.vibration}</td>
              <td>{data.airQuality}</td>
              <td>{new Date(data.timestamp).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
