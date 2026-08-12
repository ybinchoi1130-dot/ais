#!/usr/bin/env python
# coding: utf-8

# ## 12-1 datetime 객체

# In[77]:


from datetime import datetime


# In[78]:


now = datetime.now()
print(now)


# In[79]:


t1 = datetime.now()
t2 = datetime(1970, 1, 1)
print(t1)
print(t2)


# In[80]:


diff = t1 - t2
print(diff)


# In[81]:


print(type(diff))


# ## 12-2 datetime으로 변환하기

# In[82]:


import pandas as pd

ebola = pd.read_csv('../data/country_timeseries.csv')
print(ebola.iloc[:5, :5])


# In[83]:


print(ebola.info())


# In[84]:


ebola['date_dt'] = pd.to_datetime(ebola['Date'])


# In[85]:


ebola['date_dt'] = pd.to_datetime(ebola['Date'], format='%m/%d/%Y')


# In[86]:


print(ebola.info())


# ## 12-3 시계열 데이터 불러오기

# In[87]:


ebola = pd.read_csv('../data/country_timeseries.csv', parse_dates=["Date"])
print(ebola.info())


# ## 12-4 시간 정보 추출하기

# In[88]:


d = pd.to_datetime('2021-12-14')
print(d)
print(type(d))


# In[89]:


print(d.year)
print(d.month)
print(d.day)


# In[90]:


ebola['date_dt'] = pd.to_datetime(ebola['Date'])
print(ebola[['Date', 'date_dt']])


# In[91]:


ebola['year'] = ebola['date_dt'].dt.year
print(ebola[['Date', 'date_dt', 'year']])


# In[92]:


ebola = ebola.assign(
    month=ebola["date_dt"].dt.month,
    day=ebola["date_dt"].dt.day
)
print(ebola[['Date', 'date_dt', 'year', 'month', 'day']])


# In[93]:


print(ebola.info())


# ## 12-5 시간 간격 계산하기

# In[94]:


print(ebola.iloc[-5:, :5])


# In[95]:


print(ebola['date_dt'].min())


# In[96]:


ebola['outbreak_d'] = ebola['date_dt'] - ebola['date_dt'].min()
print(ebola[['Date', 'Day', 'outbreak_d']])


# In[97]:


print(ebola.info())


# ## 12-6 datetime 객체의 메서드

# In[98]:


banks = pd.read_csv('../data/banklist.csv')
print(banks.head())


# In[99]:


banks = pd.read_csv(
    "../data/banklist.csv", parse_dates=["Closing Date", "Updated Date"]
)
print(banks.info())


# In[100]:


banks = banks.assign(
    closing_quarter=banks['Closing Date'].dt.quarter,
    closing_year=banks['Closing Date'].dt.year
)


# In[101]:


closing_year = banks.groupby(['closing_year']).size()
print(closing_year)


# In[102]:


closing_year_q = (
    banks
    .groupby(['closing_year', 'closing_quarter'])
    .size()
)
print(closing_year_q)


# In[103]:


import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax = closing_year.plot()
plt.show()


# In[104]:


fig, ax = plt.subplots()
ax = closing_year_q.plot()
plt.show()


# ## 12-7 주식 데이터 다루기

# In[105]:


# !pip install pandas-datareader


# In[106]:


import pandas_datareader.data as web

tesla = web.DataReader('TSLA', 'stooq')
print(tesla)


# In[107]:


tesla.info()


# In[108]:


print(tesla.index)


# In[109]:


tesla = pd.read_csv('../data/tesla_stock_yahoo.csv')
print(tesla.head())


# In[110]:


tesla = pd.read_csv(
    '../data/tesla_stock_yahoo.csv', parse_dates=["Date"]
)


# In[111]:


print(tesla.info())


# ## 12-8 시간별 데이터 추출하기

# In[112]:


print(
    tesla.loc[
        (tesla.Date.dt.year == 2010) & (tesla.Date.dt.month == 6)
    ]
)


# #### [Do It! 실습] DatetimeIndex 객체로 추출하기

# In[113]:


tesla.index = tesla['Date']
print(tesla.index)


# In[114]:


print(tesla.loc['2015'])


# In[115]:


print(tesla.loc['2010-06'])


# #### [Do It! 실습] TimedeltaIndex 객체로 추출하기

# In[116]:


tesla['ref_date'] = tesla['Date'] - tesla['Date'].min()


# In[117]:


tesla.index = tesla['ref_date']
print(tesla.index)


# In[118]:


print(tesla)


# In[119]:


print(tesla.loc['0 day': '10 day'])


# ## 12-9 시간 범위 다루기

# In[120]:


ebola = pd.read_csv(
    '../data/country_timeseries.csv', parse_dates=["Date"]
)
print(ebola.iloc[:, :5])


# In[121]:


head_range = pd.date_range(start='2014-12-31', end='2015-01-05')
print(head_range)


# In[122]:


ebola_5 = ebola.head()


# In[123]:


ebola_5.index = ebola_5['Date']


# In[124]:


ebola_5 = ebola_5.reindex(head_range)
print(ebola_5.iloc[:, :5])


# ### 시간 범위의 주기 설정하기

# In[125]:


print(pd.date_range('2022-01-01', '2022-01-07', freq='B'))


# #### [Do It! 실습] 시간 범위의 주기 간격 설정하기

# In[154]:


print(pd.date_range('2022-01-01', '2022-01-07', freq='2B'))


# In[155]:


print(pd.date_range('2022-01-01', '2022-12-31', freq='WOM-1THU'))


# In[156]:


print(pd.date_range('2022-01-01', '2022-12-31', freq='WOM-3FRI'))


# ## 12-10 열 방향으로 값 옮기기

# In[129]:


ebola = pd.read_csv('../data/country_timeseries.csv', parse_dates=["Date"])

import matplotlib.pyplot as plt

ebola.index = ebola['Date']

fig, ax = plt.subplots()
ax = ebola.plot(ax=ax)
ax.legend(fontsize=7, loc=2, borderaxespad=0.0)
plt.show()


# In[130]:


ebola_sub = ebola[['Day', 'Cases_Guinea', 'Cases_Liberia']]
print(ebola_sub.tail(10))


# In[131]:


ebola = pd.read_csv(
    "../data/country_timeseries.csv",
    parse_dates=["Date"],
    index_col="Date",
)
print(ebola.iloc[:, :4])


# In[132]:


new_idx = pd.date_range(ebola.index.min(), ebola.index.max())
print(new_idx)


# In[133]:


new_idx = reversed(new_idx)
print(new_idx)


# In[134]:


ebola = ebola.reindex(new_idx)


# In[135]:


print(ebola.iloc[:, :4])


# In[136]:


last_valid = ebola.apply(pd.Series.last_valid_index)
print(last_valid)


# In[137]:


earliest_date = ebola.index.min()
print(earliest_date)


# In[138]:


shift_values = last_valid - earliest_date
print(shift_values)


# In[139]:


ebola_dict = {}

for idx, col in enumerate(ebola):
    d = shift_values[idx].days
    shifted = ebola[col].shift(d)
    ebola_dict[col] = shifted

# print(ebola_dict)


# In[140]:


ebola_shift = pd.DataFrame(ebola_dict)


# In[141]:


print(ebola_shift.tail())


# In[142]:


ebola_shift.index = ebola_shift['Day']
ebola_shift = ebola_shift.drop(['Day'], axis="columns")
print(ebola_shift.tail())


# ## 12-11 시간 주기 변경하기

# In[143]:


down = ebola.resample('M').mean()
print(down.iloc[:, :5])


# In[144]:


up = down.resample('D').mean()
print(up.iloc[:, :5])


# ## 12-12 시간대 다루기

# In[145]:


import pytz


# In[146]:


print(len(pytz.all_timezones))


# In[147]:


import re

regex = re.compile(r'^US')
selected_files = filter(regex.search, pytz.common_timezones)
print(list(selected_files))


# In[158]:


depart = pd.Timestamp('2017-08-29 07:00', tz='US/Eastern')
print(depart)


# In[149]:


arrive = pd.Timestamp('2017-08-29 09:57')
print(arrive)


# In[150]:


arrive = arrive.tz_localize('US/Pacific')
print(arrive)


# In[151]:


print(arrive.tz_convert('US/Eastern'))


# In[152]:


duration = arrive - depart
print(duration)


# In[ ]:




