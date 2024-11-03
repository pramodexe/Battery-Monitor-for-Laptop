import time
from datetime import datetime

# Name of the log file
log_file = "battery_log.txt"

# Open the file in append mode (creates the file if it doesn't exist)
with open(log_file, "a") as file:
    # Write the table headings
    file.write("Date\t\tTime\t\tElapsed Time\n")
    
    # Print the initial message to the terminal
    print("Battery checker running...")
    
    # Get the start time
    start_time = time.time()
    
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

        # Prepare log message
        log_message = f"{date_str}\t{time_str}\t{elapsed_time_str}"

        # Write to file
        file.write(log_message + "\n")
        
        # Flush to ensure the content is written to disk immediately
        file.flush()
        
        # Wait for 60 seconds (1 minute)
        time.sleep(60)
