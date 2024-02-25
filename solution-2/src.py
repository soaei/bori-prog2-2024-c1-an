import pandas as pd
import numpy as np
from scipy.spatial import distance

if __name__ == "__main__":

    df = pd.read_pickle("input.pkl")
    query_df = pd.read_csv("query.csv")

    input_values = df[["x", "y"]].values
    query_values = query_df.values

    diffs = distance.cdist(input_values, query_values, metric="sqeuclidean")

    # Get the minimum distances and corresponding indices
    min_distances = np.min(diffs, axis=0)
    min_indices = np.argmin(diffs, axis=0)

    out = []
    for i, idx in enumerate(min_indices):
        # Use idx to get the corresponding "weapon" value from the input DataFrame
        weapon_value = df.loc[idx, "weapon"]
        out.append({"dist": min_distances[i], "weapon": weapon_value})

    pd.DataFrame(out).to_csv("out.csv", index=False)
