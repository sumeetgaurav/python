"""Takes a user-entered CPU usage value and classifies it as high, moderate, or normal."""

# This program asks for CPU usage and prints whether it is high, moderate, or normal.
cpu = float(input("Enter the CPU: ")) #take input from user and storing it in cpu variable and typecasting it to float
if cpu > 50:
    print("CPU usage is high") #if cpu usage is greater than 50, print high usage message
elif cpu > 20 and cpu < 50:
    print("CPU usage is moderate") #if cpu usage is greater than 20 and less than 50, print moderate usage message
else:
    print("CPU usage is normal") #if cpu usage is less than or equal to 50, print normal usage message
