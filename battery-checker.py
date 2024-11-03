import time
from datetime import datetime
import psutil

# Name of the log file
log_file = "battery_log.txt"

# Open the file in append mode (creates the file if it doesn't exist)
with open(log_file, "a") as file:
    # Write the table headings
    file.write("Date | Time | Elapsed Time | Battery Percentage | Charging Status\n\n")
    
    # Print the initial message to the terminal
    print("Battery checker running... (Press Ctrl + C to stop)")

    # Get the start time
    start_time = time.time()
    
    try:
        # Infinite loop to keep logging every 1 minute
        while True:
            # Get the current date and time
            current_time = datetime.now()
            date_str = current_time.strftime("%Y-%m-%d")
            time_str = current_time.strftime("%H:%M:%S")

            # Calculate elapsed time
            elapsed_seconds = int(time.time() - start_time)
            hours = elapsed_seconds // 3600
            minutes = (elapsed_seconds % 3600) // 60
            seconds = elapsed_seconds % 60

            # Format elapsed time as HH:MM:SS
            elapsed_time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

            # Get battery information
            battery = psutil.sensors_battery()
            if battery:
                battery_percentage = f"{battery.percent}%"
                charging_status = "Charging" if battery.power_plugged else "Not Charging"
            else:
                battery_percentage = "N/A"
                charging_status = "N/A"

            # Prepare log message
            log_message = f"{date_str}\t{time_str}\t{elapsed_time_str}\t{battery_percentage}\t{charging_status}"

            # Write to file
            file.write(log_message + "\n")
            
            # Flush to ensure the content is written to disk immediately
            file.flush()
            
            # Wait for 60 seconds (1 minute)
            time.sleep(60)

    except KeyboardInterrupt:
        print("\nUser stopped the battery checker.")
