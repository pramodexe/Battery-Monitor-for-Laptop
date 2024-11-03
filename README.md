### NAME
Battery Checker for Laptop

### ABOUT
This is a battery monitoring program for laptops. You can run it through your CMD or terminal.

### DESCRIPTION
This Battery Checker script runs continuously from the terminal, logging essential battery data every minute until you stop it. The log file records the date, time, elapsed time (since the script started), battery percentage, and charging status. You can use this to get a rough idea of how long you can use your laptop. Open a terminal, run this script, and continue your work. The script will log battery status to a text file every minute. So you don't have to worry about powering off your laptop; you can see the output file anytime afterward.

### HOW TO USE
Follow these steps to use the Battery Checker.

1. **Install Python (if not already installed)**
    - Install Python on your computer from its [official website](https://www.python.org/downloads/).
    - Choose the latest version compatible with your operating system (Windows, macOS, or Linux).
    - **REMEMBER:** During installation, check the box that says `Add Python to PATH`.
    - You can check if it's already installed by running this command in the terminal.
      ```python
      python --version
      ```
    - If its output is the Python version (something like this: `Python 3.12.6`), you're good to go.

2. **Install the `psutil` Library**
   - This is needed to access the battery information like percentage and charging status, which the script logs.
   - Use one of the following commands to install it:
     ```python
     pip install psutil
     ```
     or
     ```python
     pip3 install psutil
     ```
   - To ensure psutil is installed correctly, type:
     ```python
     python -c "import psutil; print(psutil.__version__)"
     ```
   - You should see the version number of `psutil`.

3. **Prepare the Script**
    - Now you have to clone this repository from GitHub.
    - Run the following command to clone it:
      ```bash
      git clone https://github.com/pramodexe/Battery-Checker-for-Laptop
      ```
    - Move into the cloned directory.
      ```bash
      cd Battery-Checker-for-Laptop
      ```
    - You should see the `battery-checker.py` file in there.

4. **Run the Script**
    - Type the following command and press Enter:
      ```python
      python battery_checker.py
      ```
    - Your terminal will display a message: `Battery checker running...`
    - To stop the script (only if you want), you can press `Ctrl + C` in the terminal.
    - You can see a text file named like this: `battery_log_20241103_192237.txt`, which contains the output.
    - `20241103` is the date (2024.11.03 or November 3, 2024), and `192237` is the time (19:22:37 or 7:22:37 PM).

### AUTHOR
Pramod Lakshan https://github.com/pramodexe/Battery-Checker-for-Laptop/
