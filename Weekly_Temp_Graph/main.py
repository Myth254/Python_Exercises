import matplotlib.pyplot as plt

# Temperature data for the week
temperatures = [20, 22, 19, 23, 21, 24, 20]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(days, temperatures, marker='o', linewidth=2, markersize=8, color='#2E86C1')

# Customize the plot
plt.title('Weekly Temperature Readings', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Day of the Week', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.grid(True, alpha=0.3)

# Add value labels on each point
for i, temp in enumerate(temperatures):
    plt.annotate(f'{temp}°C', (i, temp), textcoords="offset points",
                xytext=(0,10), ha='center', fontsize=10)

# Set y-axis limits for better visualization
plt.ylim(min(temperatures) - 2, max(temperatures) + 2)

# Improve layout and display
plt.tight_layout()
plt.show()

# Print summary statistics
print(f"Weekly Temperature Summary:")
print(f"Average temperature: {sum(temperatures)/len(temperatures):.1f}°C")
print(f"Highest temperature: {max(temperatures)}°C")
print(f"Lowest temperature: {min(temperatures)}°C")
print(f"Temperature range: {max(temperatures) - min(temperatures)}°C")