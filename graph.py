import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import result
data = pd.read_csv("result.csv")


# Display the table
print("Model Ranking Table:")
print(
    data[["Model", "Max_Seq_Length", "Batch_Size", "Accuracy", "F1_Score", "Rank"]].sort_values(
        by="Rank"
    )
)

# Bar chart
labels = data["Model"]
num_models = len(labels)

# Parameters for bar chart
max_seq_length = data["Max_Seq_Length"]
batch_size = data["Batch_Size"]
accuracy = data["Accuracy"]
f1_score = data["F1_Score"]
ranks = data["Rank"]

# Normalize ranks to a scale of 0 to 1 for better comparison
normalized_ranks = ranks / np.max(ranks)

# Plot the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.2
index = range(num_models)

ax.bar(index,max_seq_length,width=bar_width,label="Max_Seq_Length")
ax.bar(index,batch_size,width=bar_width,label="Batch_Size",bottom=max_seq_length,)
ax.bar(index, accuracy, width=bar_width, label="Accuracy",bottom=max_seq_length + batch_size,)
ax.bar(index,f1_score,width=bar_width,label="f1_score",bottom=max_seq_length + batch_size + accuracy,)
ax.bar(
    index,
    normalized_ranks,
    width=bar_width,
    label="Normalized Rank",
    color="black",
    alpha=0.5,
)

ax.set_xticks(index)
ax.set_xticklabels(labels)
ax.set_ylabel("Metrics")
ax.set_title("Text Classification Model Comparison Through Topsis")

ax.legend()
plt.savefig("BarChart.png")
plt.show()