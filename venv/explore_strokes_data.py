import pandas as pd

pd.options.display.max_columns = None

# check the data, think about how the data from strokes and air datasets can be used
# group the data by dates, locations

# select_strokes_data = ['Year', 'LocationAbbr', 'LocationDesc', 'Class', 'Topic', 'Data_Value', 'Data_Value_Unit',
#                        'Data_Value_Type', 'LocationID']

# find min and max time
df_strokes = pd.read_csv("./data for project/Strokes_data/joined_data.csv")

def states_locs(df):
    unique_states = pd.unique(df['LocationAbbr'])
    print(f'There are {len(unique_states)} states mentioned')
    unique_loc = pd.unique(df['LocationDesc'])
    print(f'There are {len(unique_loc)} locations mentioned')
    return

# # explore data values units
# unique_val_units = pd.unique(df_strokes['Data_Value_Unit'])
# print(unique_val_units)
# print(len(unique_val_units))  # this means we can aggregate Data_Value columns' values freely

def create_mask(df):
    df = df.groupby(['LocationDesc', 'Year'])['Data_Value'].sum()
    return df

mask = create_mask(df_strokes)
print(mask)

# find locations with the most and least mortality for each year
# find locations with the most and least mortality in total
loc_year_min = df_strokes.groupby(['LocationDesc', 'Year'])['Data_Value'].sum().min()
loc_year_max = df_strokes.groupby(['LocationDesc', 'Year'])['Data_Value'].sum().max()
print(loc_year_max)  # ??

# # sum the mortality over the state and year
# loc_year_sum = df_strokes.groupby(['LocationAbbr','Year'])['Data_Value'].sum()

# sum the mortality over years for each state
loc_sum = df_strokes.groupby(['LocationAbbr'])['Data_Value'].sum()
print(type(loc_sum))
loc_sum = loc_sum.to_frame().reset_index()
print(type(loc_sum))
print(loc_sum.columns)

# find states with the most and least mortality in total
loc_sum_min = loc_sum.min()
print(f'loc_sum_min is \n {loc_sum_min}')
loc_sum_max = loc_sum.max()
print(f'loc_sum_min is \n {loc_sum_max}')

# sum the mortality over each years for each state
loc_year_sum = df_strokes.groupby(['LocationAbbr', 'Year'])['Data_Value'].sum()
loc_year_sum = loc_year_sum.to_frame().reset_index()
print(type(loc_year_sum))
print(loc_year_sum.columns)
print(loc_year_sum.head(10))

print(loc_year_sum.max())
print(loc_year_sum.min())