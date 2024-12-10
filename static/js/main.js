// Function to update the table dynamically with current date and time
function updateSensorData() {
    const tbody = document.getElementById('sensor-data-body');
    tbody.innerHTML = ""; // Clear the previous rows
  
    // Create a single row with current date and time in the first cell
    const currentTime = new Date().toLocaleString(); // Get current date and time
  
    const row = document.createElement('tr');
    row.innerHTML = `
      <td>${currentTime}</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    `;
    tbody.appendChild(row);
  }
  
  // Call the function every 2 seconds to simulate real-time updates
  setInterval(updateSensorData, 2000);
  
  // Trigger the function on page load as well
  updateSensorData();
  