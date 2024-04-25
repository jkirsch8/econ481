#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Problem 0
def github() -> str:
    """
    Some docstrings.
    """
    
    return "https://github.com/jkirsch8/econ481/blob/main/HW4.py"


# In[21]:


#Problem 1
import pandas as pd

def load_data() -> pd.DataFrame:
    """
    Loads data on Tesla stock price history.
    """
    df = pd.read_csv('https://lukashager.netlify.app/econ-481/data/TSLA.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date',inplace=True)
    return df



# In[22]:


# Problem 2
import matplotlib.pyplot as plt
def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    Plots the closing price of the stock from optional start to end dates
    """
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    sub_df = df.loc[start:end]
    plt.plot(sub_df['Close'])
    plt.title(f'Tesla Closing Prices from {start.date()} to {end.date()}')
    plt.show
plot_close(load_data())


# In[11]:


# Problem 3 Scratch
import statsmodels.api as sm
import statsmodels.formula.api as smf
df = load_data()
print(df)
shifted_df = df.shift(freq = 'D')
sub3_df = df[df.index.isin(shifted_df.index)]
sub3_df['last_price'] = df['Close'].shift(1)
sub3_df['delta'] = sub3_df['Close'] - sub3_df['last_price']
print(sub3_df)
shift2 = sub3_df.shift(freq ='D')
newsub_df = sub3_df[sub3_df.index.isin(shift2.index)]
newsub_df['prev_delta'] = sub3_df['delta'].shift(1)
model = sm.OLS(newsub_df['delta'],newsub_df['prev_delta'])
results = model.fit(cov_type = 'HC1')
print(newsub_df)
# 4 scratch
newsub_df['positive'] = (newsub_df['delta']>0).astype(int)
logit = sm.Logit(newsub_df['positive'],newsub_df['prev_delta'])
#print(logit.fit(cov_type = 'HC1').summary())


# In[19]:


#Problem 3

def autoregress(df: pd.DataFrame) -> float:
    """
    Returns the t-stat of a linear regression on the movement of stocks on consecutive days.
    """
    shifted_df = df.shift(freq = 'D')
    sub3_df = df[df.index.isin(shifted_df.index)]
    #sub3_df contains only dates where we have data on the day before them
    sub3_df['last_price'] = df['Close'].shift(1)
    sub3_df['delta'] = sub3_df['Close'] - sub3_df['last_price']
    shift2 = sub3_df.shift(freq ='D')
    newsub_df = sub3_df[sub3_df.index.isin(shift2.index)]
    newsub_df['prev_delta'] = sub3_df['delta'].shift(1)
    model = sm.OLS(newsub_df['delta'],newsub_df['prev_delta'])
    results = model.fit(cov_type = 'HC1')
    return results.tvalues[0]
autoregress(load_data())


# In[20]:


#Problem 4
def autoregress_logit(df: pd.DataFrame) -> float:
    """
    Fits a logit model regressing the current delta on yesterday's delta and returns the t-statistic
    """
    shifted_df = df.shift(freq = 'D')
    sub3_df = df[df.index.isin(shifted_df.index)]
    #sub3_df contains only dates where we have data on the day before them
    sub3_df['last_price'] = df['Close'].shift(1)
    sub3_df['delta'] = sub3_df['Close'] - sub3_df['last_price']
    shift2 = sub3_df.shift(freq ='D')
    newsub_df = sub3_df[sub3_df.index.isin(shift2.index)]
    newsub_df['prev_delta'] = sub3_df['delta'].shift(1)
    newsub_df['positive'] = (newsub_df['delta']>0).astype(int)
    logit = sm.Logit(newsub_df['positive'],newsub_df['prev_delta'])
    results = logit.fit()
    
    return results.tvalues[0]
autoregress_logit(load_data())


# In[10]:


# Problem 5
def plot_delta(df: pd.DataFrame) -> None:
    """
    Plots the delta x's for the full dataset.
    """
    shifted_df = df.shift(freq = 'D')
    sub3_df = df[df.index.isin(shifted_df.index)]
    #sub3_df contains only dates where we have data on the day before them
    sub3_df['last_price'] = df['Close'].shift(1)
    sub3_df['delta'] = sub3_df['Close'] - sub3_df['last_price']
    plt.plot(sub3_df['delta'])
    plt.title('Price Changes from Previous Day, Tesla Stock 2010-2024')
plot_delta(load_data())


# In[ ]:




