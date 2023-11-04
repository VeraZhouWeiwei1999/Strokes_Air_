import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = None

def select_dates(f, s, df):
    years = range(f, s, 1)
    df_dates = pd.DataFrame(
        columns=['Date', 'AQI', 'Category', 'Defining Parameter', 'city_ascii', 'state_id', 'population'])
    for year in years:
        start_date = f'{year}-01-01'
        end_date = f'{year}-12-31'
        mask = (df['Date'] > start_date) & (df['Date'] <= end_date)
        df_selected = df.loc[mask]
        df_dates = pd.concat([df_dates, df_selected], ignore_index=True)
    df_dates['Date'] = df_dates['Date'].astype('datetime64[ns]')
    df_dates['Year'] = df_dates['Date'].dt.year
    df_dates['Month'] = df_dates['Date'].dt.month
    return df_dates


# write documentation to the function
def explore_data(df, parameter):
    mask = df.groupby(['state_id', 'state_name', 'city_ascii', 'Year'], axis = 0)['AQI']
    select_action = {
        "max": mask.max().to_frame(),
        "min": mask.min().to_frame(),
        "mean": mask.mean().to_frame(),
    }
    df_grouped = select_action.get(parameter, "unknown")
    df_grouped = df_grouped.reset_index()
    return df_grouped


# def explore_data_year(parameter):
#     mask = df_air.groupby(['state_id', 'state_name', 'city_ascii', 'Year'], axis = 0)['AQI']
#     select_action = {
#         "max": mask.max().to_frame(),
#         "min": mask.min().to_frame(),
#         "mean": mask.mean().to_frame(),
#     }
#     df = select_action.get(parameter, "unknown")
#     df = df.reset_index()
#     return df

