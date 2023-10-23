import pandas as pd
import utils
pd.options.display.max_columns = None

def upload_data(folder, file, columns, key):
    df = utils.upload_csv(folder, file)
    df = utils.set_index(df)
    df = utils.select_columns(df, columns)
    df = utils.drop_na(df, key)
    return df


