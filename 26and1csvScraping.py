import pandas as pd

csv_input = pd.read_csv(filepath_or_buffer= r'26and1.csv', encoding="shift_jis", sep=",")
print(csv_input[["Ру", "Ном"]])
print("=" * 20)
print(csv_input.iloc[2, 0])
