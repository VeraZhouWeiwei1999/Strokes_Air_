import pandas as pd

pd.options.display.max_columns = None


# function to upload data
def upload_csv(directory, file_name):
    df_name = pd.read_csv(f"./data for project/{directory}/{file_name}.csv", header=None)
    print(df_name.shape)
    return df_name


# function to set new index
def set_index(df_name):
    df_name.columns = df_name.iloc[0]
    df_name = df_name.drop(0)
    print(f"The shape is {df_name.shape}")
    return df_name


# select data we need
def select_columns(df_name, columns_list):
    df_name = df_name[columns_list]
    print(f"The shape after selecting columns is {df_name.shape}")
    return df_name


# drop nan values
def drop_na(df_name, column_name):
    df_name = df_name[df_name[f'{column_name}'].notna()]
    print(f"The shape after dropping na is {df_name.shape}")
    return df_name


# join data from several dfs
def join_data(df_fin, df_name):
    df_fin = pd.concat([df_fin, df_name], axis=0)
    print(f"The shape joining the dfs is {df_fin.shape}")
    return df_fin


def save_data(df_name, directory):
    df_name.to_csv(f"./data for project/{directory}/joined_data.csv")
    print(f"The data saved to {directory}")
    return


# upload strokes data
folder = "Strokes_data"
file_list = ["strokes_2013", "strokes_2014", "strokes_2016"]
columns_for_strokes = ['Year', 'LocationAbbr', 'LocationDesc', 'Class', 'Topic', 'Data_Value', 'Data_Value_Unit',
                       'Data_Value_Type', 'LocationID']
df_final = pd.DataFrame()

for file in file_list:
    df = upload_csv(folder, file)
    df = set_index(df)
    df = select_columns(df, columns_for_strokes)
    df = drop_na(df, 'Data_Value')
    df_final = join_data(df_final, df)
    save_data(df_final, folder)


# upload air data
folder = "Air_data"
file = "US_AQI"
columns_for_air = ['Date', 'AQI', 'Category', 'Defining Parameter', 'city_ascii', 'state_id', 'state_name',
                   'population']
df = upload_csv(folder, file)
df = set_index(df)
df = select_columns(df, columns_for_air)
df = drop_na(df, 'AQI')
save_data(df, folder)
# df.to_csv(f"./data for project/{folder}/joined_data.csv")