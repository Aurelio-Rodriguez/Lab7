import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "breadprice.csv"  # Ensure the file is in the same directory
df = pd.read_csv(file_path)

# Compute the average price per year
df["Average Price"] = df.iloc[:, 1:].mean(axis=1)

# Prepare the plot
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Average Price"], marker='o', linestyle='-', color="blue", label="Average Bread Price")

# Customizing the plot
plt.xticks(df["Year"])
plt.xlabel("Year")
plt.ylabel("Average Bread Price")
plt.title("Average Bread Price Per Year")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# Save the plot as an image
plt.savefig("breadprice_plot.png")
