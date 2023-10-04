import pandas as pd
pd.options.display.max_columns = None


def get_data(route):
    df = pd.read_csv(route)
    return df

df_strokes = get_data("./data for project/Strokes_data_new/joined_data.csv")
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

strokes_per_year = explore_strokes(df_strokes, "mean")

def save_data(df_name, directory, name):
    df_name.to_csv(f"./data for project/{directory}/{name}.csv")
    print(f"The data saved to {directory}")
    return
save_data(strokes_per_year, "combined", "strokes_per_year")



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