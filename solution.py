import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


covid = pd.read_csv("owid-covid-data.csv")


columns_to_include = ["iso_code", "continent", "location", "date", "total_cases", "new_cases", "total_deaths", "new_deaths"]

covid = covid[columns_to_include]


covid['total_cases'].fillna(0, inplace=True)
covid['new_cases'].fillna(0, inplace=True)
covid['total_deaths'].fillna(0, inplace=True)
covid['new_deaths'].fillna(0, inplace=True)


covid.dropna(inplace=True)




covid['date'] = pd.to_datetime(covid['date'])



top_5_countries = covid.groupby('location')['new_cases'].sum().sort_values(ascending=False).head(5)


plt.figure(figsize=(12,8))

for country in top_5_countries.index:
    temp_df = covid[covid['location'] == country]
    plt.plot(temp_df['date'], temp_df['new_cases'] / 1e6, label=country, linestyle='dashed')

plt.xlabel('Date', fontsize=20)
plt.ylabel('New Cases (in millions)', fontsize=20)
plt.title('New Cases per Day', fontsize=24)
plt.legend(loc='upper left', fontsize=22)
plt.savefig("new_cases_line_plot.png", dpi=200)


plt.show()


# Assuming grouped_df is your DataFrame and it has columns 'location', 'new_deaths', 'new_cases'

# plt.figure(figsize=(12,8))

for country in top_5_countries.index:
    temp_df = covid[covid['location'] == country]
    plt.scatter(temp_df['new_cases'], temp_df['new_deaths'], label=country)

plt.xlabel('New Cases')
plt.ylabel('New Deaths')
# make legend outside the graph
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# save the whole fig including legend
plt.savefig("new_cases_vs_new_deaths.png", dpi=200, bbox_inches='tight')

# show the legend too
plt.show()


# create a pie chart of all the locations with any location that has less than 1% of the total cases grouped into an "other" category
plt.figure(figsize=(8,8))


top_countries_pctg = pd.DataFrame(covid.groupby('location')['new_cases'].sum().sort_values(ascending=False) / sum(covid['new_cases']) * 100)

top_countries_pctg.reset_index(inplace=True)

top_countries_pctg.loc[top_countries_pctg['new_cases'] < 3, 'location'] = 'Other'

top_countries_pctg = top_countries_pctg.groupby('location')['new_cases'].sum().sort_values(ascending=False)

# plot a pie chart
plt.pie(top_countries_pctg, labels=top_countries_pctg.index, autopct='%1.1f%%', startangle=140)

plt.savefig("pie_chart.png", dpi=300)

plt.show()





