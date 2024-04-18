#!/usr/bin/env python
# coding: utf-8

# In[1]:


def github() -> str:
    """
    Returns a link to this code in my github repository
    """

    return "https://github.com/jkirsch8/econ481/edit/main/HW3%20(2).py"


# In[29]:


import pandas as pd

def import_yearly_data(years: list) -> pd.DataFrame:
    """
    Returns data on direct emitters for given years from the EPA data.
    """
    
    upd_df = pd.DataFrame()
    for year in years:
        url = f'https://lukashager.netlify.app/econ-481/data/ghgp_data_{year}.xlsx'
        df = pd.read_excel(url,header = 3,sheet_name = 'Direct Emitters')
        df['year'] = year
        upd_df = pd.concat([df,upd_df])
    
    
    return upd_df


# In[30]:


pip install pyxlsb


# In[31]:


import pandas as pd

def import_parent_companies(years: list) -> pd.DataFrame:
    """
    Takes in a list of years, returns a dataframe of the parent companies excel sheets from those years
    """
    url = 'https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb'
    upd_df = pd.DataFrame()
    for year in years:
        df = pd.read_excel(url,sheet_name = str(year), header = 0)
        df = df.dropna(axis = 0, how = 'all')
        df['year'] = year
        upd_df = pd.concat([df,upd_df])
    return upd_df


# In[32]:


def n_null(df: pd.DataFrame, col: str) -> int:
    """
    Takes a data frame and a column name and returns the number of null values in said column
    """
    nulls = df[col].isnull().sum()
    return nulls


# In[38]:


def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    Merges and cleans emission and parent company data by year and facility ID
    """
    merged_data = emissions_data.merge(parent_data,how = 'left',left_on=['Facility Id', 'year'],right_on = ['GHGRP FACILITY ID', 'year'])
    merged_data = merged_data[['Facility Id','year','State','Industry Type (sectors)','Total reported direct emissions','PARENT CO. STATE','PARENT CO. PERCENT OWNERSHIP']]
    merged_data.columns = merged_data.columns.str.lower()
    return merged_data


# In[39]:


#Test
emissions_data = import_yearly_data(['2019','2020','2021','2022'])
parent_data = import_parent_companies(['2019','2020','2021','2022'])


# In[35]:


#Exploration
merged_data = emissions_data.merge(parent_data,how = 'left',left_on=['Facility Id', 'year'],right_on = ['GHGRP FACILITY ID', 'year'])
merged_data = merged_data[['Facility Id','year','State','Industry Type (sectors)','Total reported direct emissions','PARENT CO. STATE','PARENT CO. PERCENT OWNERSHIP']]
merged_data.columns = merged_data.columns.str.lower()
merged_data

grouped_data = merged_data.groupby(['industry type (sectors)'])
summary_df = grouped_data[['total reported direct emissions','parent co. percent ownership']].agg([('mean','mean'),('median','median'),('min','min'),('max','max'),('sum','sum')])
sorted = summary_df.sort_values(by=('total reported direct emissions', 'sum'),ascending = False)


# In[36]:


def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    Groups the dataframe by the given variables and outputs summary statistics for emissions and parent co. ownership
    """
    grouped_data = df.groupby(group_vars)
    summary_df = grouped_data[['total reported direct emissions','parent co. percent ownership']].agg([('mean','mean'),('median','median'),('min','min'),('max','max')])
    sorted = summary_df.sort_values(by=('total reported direct emissions', 'mean'),ascending = False)
    return sorted


# In[37]:


total = aggregate_emissions(clean_data(import_yearly_data([2019,2020,2021]),import_parent_companies([2019,2020,2021])),['parent co. state'])


# In[ ]:




