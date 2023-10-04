import pandas as pd
from upload_data_functions import upload_csv, select_columns, drop_na, set_index, save_data
pd.options.display.max_columns = None

strokes_df = upload_csv("Strokes_data_new", "heart disease")
strokes_df = set_index(strokes_df)
col_names = ["Year", "LocationAbbr", "LocationDesc", "Data_Value", "Data_Value_Unit"]
strokes_df = select_columns(strokes_df, col_names)


strokes_df = drop_na(strokes_df, "Data_Value")
strokes_df = strokes_df[strokes_df['Data_Value_Unit'] == "per 100,000"]

save_data(strokes_df, "Strokes_data_new")
print(strokes_df)