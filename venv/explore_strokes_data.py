import pandas as pd
pd.options.display.max_columns = None

# group by year and location
def explore_strokes(df, parameter):
    mask = df.groupby(["Year", "LocationAbbr", "LocationDesc"])['Data_Value']
    select_action = {
        "max": mask.max().to_frame(),
        "min": mask.min().to_frame(),
        "mean": mask.mean().to_frame(),
    }
    df = select_action.get(parameter, "unknown")
    df = df.reset_index()
    return df

# strokes_per_year = explore_strokes(df_strokes, "mean")



# def explore_data_year(parameter):
#     # mask = df_air.groupby(['state_id', 'state_name', 'city_ascii', df_air['Date'].dt.year])['AQI']
#     mask = df_air.groupby(['state_id', 'state_name', 'city_ascii', 'Year'], axis = 0)['AQI']
#     select_action = {
#         "max": mask.max().to_frame(),
#         "min": mask.min().to_frame(),
#         "mean": mask.mean().to_frame(),
#     }
#     df = select_action.get(parameter, "unknown")
#     df = df.reset_index()
#     return df