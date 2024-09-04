import matplotlib.pyplot as plt

'''
#version 1
years = [1980, 1981, 2000, 2024]
ages =  [0, 1, 20, 44]

plt.plot(years, ages, marker='*')
'''

'''
#Version 2
years = [1980, 1981, 2000, 2024]
ages =  [0, 1, 20, 44]

# Creating the plot
plt.figure(figsize=(10, 6))
plt.plot(years, ages, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)

# Adding titles and labels
plt.title("Age Progression Over the Years", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("My Age", fontsize=14)

# Adding grid for better readability
plt.grid(True)
'''
# Display the graph
plt.show()
