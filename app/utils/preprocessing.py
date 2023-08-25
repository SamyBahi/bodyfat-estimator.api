import pandas as pd


def mens_to_input(mens: dict) -> pd.DataFrame:
    mens_df = pd.DataFrame(mens)

    input = mens_df.copy()

    input["AAnRatio"] = input["Abdomen"] / input["Ankle"]
    input["AWnRatio"] = input["Abdomen"] / input["Wrist"]
    input["AFRatio"] = input["Abdomen"] / input["Forearm"]
    input["AARatio"] = input["Abdomen"] / input["Age"]
    input["WARatio"] = input["Abdomen"] / input["Weight"]

    input["TCRatio"] = input["Thigh"] / input["Chest"]
    input["TWnRatio"] = input["Thigh"] / input["Wrist"]
    input["TARatio"] = input["Thigh"] / input["Age"]

    input["CWnRatio"] = input["Chest"] / input["Wrist"]
    input["CKRatio"] = input["Chest"] / input["Knee"]

    input["ANNRatio"] = input["Ankle"] / input["Neck"]

    input["WBRatio"] = input["Wrist"] / input["Biceps"]

    input["AGBRatio"] = input["Age"] / input["Biceps"]

    input.drop(["Abdomen", "Ankle", "Wrist", "Knee"], axis=1, inplace=True)

    return input
