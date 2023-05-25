import csv
import matplotlib.pyplot as plt
import numpy as np

# Define the CSV file path
csv_file = 'data.csv'

# Initialize lists to store force and time values
force = []
time = []

# Read data from CSV file
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file, delimiter=';')
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        force.append(float(row[1]))
        time.append(float(row[0]))

# Find the index of the first non-zero force value
start_index = next((index for index, value in enumerate(force) if value != 0), None)

# Find the index of the first zero force value after the start index
end_index = next((index for index, value in enumerate(force[start_index:]) if value == 0), None)
if end_index is not None:
    end_index += start_index

# Generate the graph
plt.plot(time, force)
plt.xlabel('Time (ms)')
plt.ylabel('Force (N)')
plt.title('Force vs Time')
plt.grid(True)
plt.show()

# Calculate the area under the curve using the trapezoidal rule
area = np.trapz(force[start_index:end_index], time[start_index:end_index])

print("Area under the curve: {:.2f} N.ms".format(area))
