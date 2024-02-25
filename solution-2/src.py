import pandas as pd
import numpy as np
from scipy.spatial import distance

if __name__ == "__main__":
    df = pd.read_pickle("input.pkl")
    query_df = pd.read_csv("query.csv")

    input_values = df[["x", "y"]].values
    query_values = query_df.values

    # Compute pairwise squared Euclidean distances
    diffs = distance.cdist(input_values, query_values, metric="euclidean")

    # Get the minimum distances and corresponding indices
    min_indices = np.argmin(diffs, axis=0)
    min_distances = np.min(diffs, axis=0)

    # Get the corresponding "weapon" values using min_indices
    weapon_values = df.iloc[min_indices]["weapon"].values

    # Create the output DataFrame
    out_df = pd.DataFrame({"dist": min_distances, "weapon": weapon_values})
    out_df.to_csv("out.csv", index=False)
