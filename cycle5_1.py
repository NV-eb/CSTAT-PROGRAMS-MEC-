import matplotlib.pyplot as plt

continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
populations = [1340598, 4641055, 747636, 579024, 422535, 43100]

plt.bar(continents, populations,color="skyblue")

plt.title('Population of Continents')
plt.xlabel('Continents')
plt.ylabel('Population (in thousands)')

plt.xticks(rotation=30)
plt.show()