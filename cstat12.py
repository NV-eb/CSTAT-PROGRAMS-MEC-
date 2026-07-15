import matplotlib.pyplot as plt

# Data
continents = ["Africa", "Asia", "Europe", "North America",
              "Oceania", "South America", "Soviet Union"]

area = [11.7, 10.4, 1.9, 9.4, 3.3, 6.9, 7.9]

# Draw bar chart
plt.bar(continents, area, color="skyblue")

# Labels and title
plt.title("Area of Continents")
plt.xlabel("Continents")
plt.ylabel("Area (Million Square Miles)")

# Rotate x-axis labels for better readability
plt.xticks(rotation=20)

# Display chart
plt.show()
