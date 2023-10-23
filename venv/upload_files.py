import pandas as pd
import utils

pd.options.display.max_columns = None

strokes_df = utils.upload_csv("Strokes_data_new", "heart disease")
strokes_df = utils.set_index(strokes_df)
col_names = ["Year", "LocationAbbr", "LocationDesc", "Data_Value", "Data_Value_Unit"]
strokes_df = utils.select_columns(strokes_df, col_names)


strokes_df = utils.drop_na(strokes_df, "Data_Value")
strokes_df = strokes_df[strokes_df['Data_Value_Unit'] == "per 100,000"]

utils.save_data(strokes_df, "Strokes_data_new")

air_df = utils.upload_csv("Air_data", "US_AQI")
air_df = utils.set_index(air_df)
columns_for_air = ['Date', 'AQI', 'Category', 'Defining Parameter', 'city_ascii', 'state_id', 'state_name', 'population']
air_df = utils.select_columns(air_df, columns_for_air)
air_df = utils.drop_na(air_df, 'AQI')
utils.save_data(air_df, "Air_data")