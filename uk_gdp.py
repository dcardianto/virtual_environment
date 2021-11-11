import pandas as pd
import os

def get_uk_data(file, sheet, var_name):
    df = pd.read_excel(file, sheet_name=sheet, header=1)
    df = df[df['ITL']=='ITL1'].reset_index()
    df = df[['Region name', 2015]]
    df = df.rename(columns={'Region name':'region', 2015:var_name})
    return df

path = r'C:\Users\dwica\Documents\GitHub\virtual_environment'
uk_gdp_file = os.path.join(path, 'regionalgrossdomesticproductallitlregions.xlsx')
uk_gdp_capita = get_uk_data(uk_gdp_file, 'Table 7', 'GDP per Capita')
uk_gdp_capita.head()
