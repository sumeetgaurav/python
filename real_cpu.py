"""Monitors real-time CPU usage with psutil and flags it as healthy or unhealthy against a user-defined threshold."""

# This script imports psutil and prints the available CPU-related functions and current CPU times.

import psutil  # Import the psutil library to access system information.


# print(dir(psutil))  # Show all available psutil functions and attributes.
# print(psutil.cpu_times())  # Print the current CPU times from the system.
# print(psutil.subprocess.__doc__)  # Print the documentation for the subprocess module in psutil.

threshold = float(input("Enter the threshold for CPU usage: "))  # Set a threshold value for CPU usage.
for i in range(5):

    if psutil.cpu_percent(interval=1) > threshold:  # Check if the CPU usage exceeds the threshold.
        print("CPU usage is Unhealthy")  # If it does, print a message indicating high CPU usage.
    else:
        print("CPU usage is Healthy")  # If it doesn't, print a message indicating normal CPU usage.
   