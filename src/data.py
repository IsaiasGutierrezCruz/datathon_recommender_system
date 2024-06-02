from typing import List
import pandas as pd


data = pd.read_parquet("data/base_info.parquet", engine="pyarrow")



def get_base_info(ids: List[int]) -> dict:
    result: List[dict] = data[data["id"].isin(ids)].to_dict(orient="records")

    for item in result:
        for key in item.keys():
            if item[key] == "NA":
                item[key] = ""

    return result