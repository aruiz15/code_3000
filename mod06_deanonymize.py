import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    common_cols = [col for col in anon_df.columns if col in aux_df.columns] #finds common columns 

    exclude_cols = {"anon_id", "matched_name", "name"} #removes identifier columns
    match_cols = [col for col in common_cols if col not in exclude_cols]

    if "anon_id" not in anon_df.columns:
        raise ValueError("anon_df must contain an 'anon_id' column")
    if "name" not in aux_df.columns:
        raise ValueError("aux_df must contain a 'name' column")
    if not match_cols:
        raise ValueError("no shared quasi-identifier columns found to match on")

    anon_unique = anon_df.groupby(match_cols).filter(lambda x: len(x) == 1).copy() #keeps only the unique rows
    aux_unique = aux_df.groupby(match_cols).filter(lambda x: len(x) == 1).copy()

    matches = anon_unique.merge( #merges unique rows 
        aux_unique[match_cols + ["name"]],
        on=match_cols,
        how="inner"
    )

    matches = matches[["anon_id", "name"]].rename(columns={"name": "matched_name"}) #returns required columns
    matches = matches.drop_duplicates(subset=["anon_id"]) #ensures one match per anon_id

    return matches


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    if len(anon_df) == 0:
        return 0.0
    return len(matches_df) / len(anon_df)
