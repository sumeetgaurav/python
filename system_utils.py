"""Reusable utility module that collects live CPU, memory, and disk usage stats into a dictionary."""

# create a function that can be reused, it should show the system info
import psutil  # Import the psutil library to access system information.

def get_system_info():
    """
    This function retrieves and returns the current system information, including CPU usage, memory usage, and disk usage.
    """
    cpu = psutil.cpu_percent(interval=1)  # Get the current CPU usage percentage over a 1-second interval.
    mem = psutil.virtual_memory().percent  # Get the current virtual memory usage statistics.
    disk = psutil.disk_usage('/').percent  # Get the disk usage statistics for the root directory.
    
    system_info = {
        "CPU Usage": cpu,  # Store the CPU usage percentage in the system_info dictionary
        "Memory Usage": mem,  # Store the memory usage percentage in the system_info dictionary.
        "Disk Usage": disk  # Store the disk usage percentage in the system_info dictionary.
    }
    
    return system_info  # Return the system_info dictionary containing CPU, memory, and disk usage statistics.
