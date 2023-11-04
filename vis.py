
import matplotlib.pyplot as plt
import pandas as pd



# Create a simple visualization
plt.figure(figsize=(8, 6))
plt.hist(df['Region'], bins=20, color='red')
plt.xlabel('Region')
plt.ylabel('Count')
plt.title('Histogram of Our Data')
plt.xticks(rotation=90)
plt.grid(True)

# Save the visualization as vis.png
plt.savefig('/app/vis.png')

exec(open("app/model.py").read())
