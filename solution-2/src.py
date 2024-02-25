import pandas as pd

if __name__ == "__main__":

    df = pd.read_pickle("input.pkl")
    query_df = pd.read_csv("query.csv")

    out = []
    for idx, row in query_df.iterrows():

        diffs = (df[["x", "y"]] - row).pipe(lambda df: df**2).sum(axis=1)
        out.append({"dist": diffs.min(), "weapon": df.loc[diffs.argmin(), "weapon"]})

    pd.DataFrame(out).to_csv("out.csv", index=False)
