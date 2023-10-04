import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = None

# check the data, think about how the data from strokes and air datasets can be used
# group the data by dates, locations

def get_data(route):
    df = pd.read_csv(route)
    return df

df_air = get_data("./data for project/Air_data/joined_data.csv")
# df_air = get_data("./data for project/Air_data/joined_dat.csv")

# select 2013, 2014, 2016
def select_dates(dates):
    df_dates = pd.DataFrame(
        columns=['Date', 'AQI', 'Category', 'Defining Parameter', 'city_ascii', 'state_id', 'population'])
     #   columns=['Date', 'AQI', 'Category', 'Defining Parameter', 'city_ascii', 'state_id', 'state_name', 'population'])
    for year in dates:
        start_date = f'{year}-01-01'
        end_date = f'{year}-12-31'
        mask = (df_air['Date'] > start_date) & (df_air['Date'] <= end_date)
        df_selected = df_air.loc[mask]
        df_dates = pd.concat([df_dates, df_selected], ignore_index=True)
    # print(df_dates.head())
    # print(df_dates.tail())
    return df_dates

years = range (1999, 2020 , 1 )
df_air = select_dates(years)

def reformat_date_to_YM(df):
    df['Date'] = df['Date'].astype('datetime64[ns]')
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    return df

df_air = reformat_date_to_YM(df_air)


# write documentation to the function
def explore_data(parameter):
    # mask = df_air.groupby(['state_id', 'state_name', 'city_ascii', df_air['Date'].dt.year])['AQI']
    mask = df_air.groupby(['state_id', 'state_name', 'city_ascii', 'Year', 'Month'], axis = 0)['AQI']
    select_action = {
        "max": mask.max().to_frame(),
        "min": mask.min().to_frame(),
        "mean": mask.mean().to_frame(),
    }
    df = select_action.get(parameter, "unknown")
    df = df.reset_index()
    return df
air_mean_per_month_df = explore_data("mean")

def explore_data_year(parameter):
    # mask = df_air.groupby(['state_id', 'state_name', 'city_ascii', df_air['Date'].dt.year])['AQI']
    mask = df_air.groupby(['state_id', 'state_name', 'city_ascii', 'Year'], axis = 0)['AQI']
    select_action = {
        "max": mask.max().to_frame(),
        "min": mask.min().to_frame(),
        "mean": mask.mean().to_frame(),
    }
    df = select_action.get(parameter, "unknown")
    df = df.reset_index()
    return df
air_mean_per_year_df = explore_data_year("mean")
def save_data(df_name, directory, name):
    df_name.to_csv(f"./data for project/{directory}/{name}.csv")
    print(f"The data saved to {directory}")
    return
save_data(air_mean_per_year_df, "combined", "air_mean_per_year")
def create_plot(df, city):
    df['date'] = df['Month'].map(str) + '-' + df['Year'].map(str)
    df['date'] = pd.to_datetime(df['date'], format='%m-%Y').dt.strftime('%m-%Y')
    # fig, ax = plt.subplots()
    df = df[df['city_ascii'] == city]
    plt.plot_date(df['date'], df['AQI'], linestyle='dashed')
    plt.xlabel("Date")
    plt.ylabel("AQI")
    plt.title(city)
    plt.tick_params("x", labelrotation=35)

    return plt.show()

def create_plot_yearly(df, city):
    # df['date'] = df['Month'].map(str) + '-' + df['Year'].map(str)
    df['Year'] = pd.to_datetime(df['Year'], format='%Y').dt.strftime('%Y')
    # fig, ax = plt.subplots()
    df = df[df['city_ascii'] == city]
    plt.plot_date(df['Year'], df['AQI'], linestyle='dashed')
    plt.xlabel("Date")
    plt.ylabel("AQI")
    plt.title(city)
    plt.tick_params("x", labelrotation=35)

    return plt.show()

# create_plot(air_mean_per_month_df, "Albuquerque")
create_plot_yearly(air_mean_per_year_df, "Albuquerque")
# different cities can have the same name. Refactor to city and state instead of city.




