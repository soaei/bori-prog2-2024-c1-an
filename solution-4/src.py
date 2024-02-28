import pandas as pd
import pickle


if __name__ == "__main__":

    df = pd.read_pickle("input.pkl")
    query_df = pd.read_csv("query.csv")

    with open("tree.pkl", "rb") as file:
        tree = pickle.load(file)

    distances, indices = tree.query(query_df, k=1)

    weapon_values = df.iloc[indices]["weapon"].values

    out_df = pd.DataFrame({"dist": distances, "weapon": weapon_values})

    out_df.to_feather("out.feather")
