import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 13})

''' Setup for retreiving data '''
# The following commented-out code is just used to retrieve the data from the Excel files and bring it into Python

# # Load the Excel files
# gdps = pd.read_excel('/Users/teofield-marsham/Library/CloudStorage/OneDrive-Personal/OneDrive Desktop/Uni Stuff/CS 6/Macro_Economics/namq_10_gdp__nominal gdp real gdp gdp deflator.xlsx', sheet_name='Sheet 2')

# pop = pd.read_excel('/Users/teofield-marsham/Library/CloudStorage/OneDrive-Personal/OneDrive Desktop/Uni Stuff/CS 6/Macro_Economics/demo_pjan__population.xlsx', sheet_name='Sheet 1', thousands=',')

# unemp = pd.read_excel('/Users/teofield-marsham/Library/CloudStorage/OneDrive-Personal/OneDrive Desktop/Uni Stuff/CS 6/Macro_Economics/une_rt_m__unemployment rate.xlsx', sheet_name='Sheet 1')

# inflat = pd.read_excel('/Users/teofield-marsham/Library/CloudStorage/OneDrive-Personal/OneDrive Desktop/Uni Stuff/CS 6/Macro_Economics/prc_hicp_manr__inflation rate.xlsx', sheet_name='Sheet 1')

# # Drop all completely empty columns
# gdps = gdps.dropna(axis=1, how='all')
# pop = pop.dropna(axis=1, how='all')
# unemp = unemp.dropna(axis=1, how='all')
# inflat = inflat.dropna(axis=1, how='all')

# real_gdp_from_excel = gdps.iloc[10].tolist()
# real_pop_from_excel = pop.iloc[10].tolist()
# unemp_from_excel = unemp.iloc[11].tolist()
# inflat_from_excel = inflat.iloc[9].tolist()

# real_pop_from_excel = [
#     int(x) if isinstance(x, (np.integer, np.floating, int, float)) and not pd.isna(x) else x
#     for x in real_pop_from_excel
# ]

# print(real_gdp_from_excel)
# print(real_pop_from_excel)
# print(unemp_from_excel)
# print(inflat_from_excel)


# Chain linked real GDP quarterly values from 1990-Q1 to 2024-Q4
# chain_linked_index_real_gdp = [68.313, 67.393, 65.921, 65.562, 64.289, 63.506, 62.201, 61.481, 61.662, 60.983, 60.474, 60.028, 60.119, 59.988, 60.351, 60.788, 61.192, 61.728, 63.147, 64.745, 64.202, 65.919, 65.634, 65.674, 66.839, 67.369, 67.724, 69.065, 69.867, 70.982, 72.661, 74.822, 74.221, 75.695, 76.723, 77.419, 78.678, 79.085, 79.493, 80.15, 82.552, 83.188, 84.478, 85.447, 85.859, 85.93, 86.507, 86.236, 86.828, 87.62, 87.434, 88.462, 87.818, 89.083, 90.149, 90.341, 91.498, 92.235, 93.27, 94.705, 95.636, 94.454, 95.831, 96.109, 98.546, 98.708, 99.65, 100.484, 102.471, 104.232, 105.226, 106.567, 106.463, 105.632, 105.997, 103.691, 96.964, 96.532, 97.452, 96.774, 97.619, 100.406, 99.914, 102.061, 102.488, 102.237, 102.367, 102.471, 101.827, 100.782, 100.412, 100.303, 99.422, 99.865, 100.133, 99.96, 99.105, 99.295, 99.589, 99.479, 98.67, 100.083, 99.994, 100.575, 101.732, 101.73, 102.83, 103.299, 104.293, 105.665, 106.166, 107.002, 107.217, 107.017, 106.919, 107.021, 107.944, 108.699, 108.752, 108.558, 108.324, 101.259, 106.259, 107.304, 106.522, 108.239, 109.413, 110.3, 109.517, 109.926, 109.723, 108.623, 109.253, 109.337, 107.701, 107.346, 107.865, 108.003, 108.606, 108.587]


''' Real GDP per capita '''

nominal_gdp = [28277.5, 28081.1, 27727.8, 27330.6, 26527.2, 26784.3, 25908.2, 24235.1, 22779.8, 22590.9, 21799, 19940, 18427.2, 18921.7, 19126.9, 19542.6, 20522.3, 20869.3, 21825.5, 23975.6, 24480.5, 25764.2, 26082.5, 26260.6, 25574.3, 25396.6, 26189, 26862.6, 27168.3, 27424.4, 28315.6, 29076.8, 29097.5, 29745.6, 30244.6, 30601.3, 31228, 31498, 31882, 32280, 33053, 33657, 34462, 35214, 35902, 36099, 36368, 36244, 36716, 37157, 37018, 37549, 37397, 37745, 38106, 38466, 39031, 39377, 39799, 40534, 41049, 40701, 41233, 41683, 42445, 42779, 43491, 44146, 45409, 46461, 47062, 48127, 48505, 48618, 49138, 47992, 45761, 45202, 45456, 45316, 45629, 47037, 47036, 48445, 48948, 49273, 49599, 49835, 50199, 49936, 50052, 50191, 50300, 50816, 51128, 51253, 51103, 51348, 51686, 51718, 51793, 52668, 52732, 52999, 53514, 53546, 54257, 54400, 55287, 55947, 56343, 57129, 57554, 57690, 58083, 58578, 59045, 59588, 59819, 60066, 60658, 56854, 59196, 59679, 59924, 61639, 62895, 64306, 65026, 66179, 67224, 67706, 67954, 68650, 68300, 67878, 68405, 68810, 69346, 69611]

price_index = [88.004, 88.585, 89.424, 88.626, 87.724, 89.665, 88.552, 83.804, 78.541, 78.756, 76.635, 70.621, 65.164, 67.059, 67.379, 68.349, 71.3, 71.877, 73.48, 78.727, 81.066, 83.094, 84.486, 85.011, 81.346, 80.146, 82.213, 82.69, 82.671, 82.139, 82.848, 82.62, 83.347, 83.544, 83.808, 84.034, 84.383, 84.675, 85.267, 85.623, 85.123, 86.015, 86.728, 87.615, 88.898, 89.313, 89.378, 89.354, 89.899, 90.157, 90.011, 90.241, 90.535, 90.079, 89.866, 90.522, 90.69, 90.763, 90.717, 90.993, 91.253, 91.611, 91.474, 92.206, 91.569, 92.139, 92.787, 93.402, 94.211, 94.765, 95.085, 96.013, 96.862, 97.85, 98.557, 98.399, 100.334, 99.551, 99.166, 99.554, 99.373, 99.596, 100.084, 100.914, 101.537, 102.462, 103.009, 103.394, 104.808, 105.34, 105.974, 106.383, 107.559, 108.181, 108.554, 109.008, 109.626, 109.941, 110.338, 110.528, 111.596, 111.879, 112.115, 112.031, 111.834, 111.902, 112.175, 111.96, 112.702, 112.567, 112.828, 113.508, 114.124, 114.606, 115.494, 116.366, 116.291, 116.546, 116.941, 117.633, 119.049, 119.368, 118.437, 118.241, 119.599, 121.07, 122.211, 123.948, 126.231, 127.992, 130.254, 132.516, 132.234, 133.486, 134.823, 134.433, 134.825, 135.449, 135.748, 136.29]

# Population annual values from 1990 to 2024
population = [4974383, 4998478, 5029002, 5054982, 5077912, 5098754, 5116826, 5132320, 5147349, 5159646, 5171302, 5181115, 5194901, 5206295, 5219732, 5236611, 5255580, 5276955, 5300484, 5326314, 5351427, 5375276, 5401267, 5426674, 5451270, 5471753, 5487308, 5503297, 5513130, 5517919, 5525292, 5533793, 5548241, 5563970, 5603851]

# Quarterly dates from 1990-Q1 to 2024-Q4
dates = ['1990-Q1', '1990-Q2', '1990-Q3', '1990-Q4', '1991-Q1', '1991-Q2', '1991-Q3', '1991-Q4', '1992-Q1', '1992-Q2', '1992-Q3', '1992-Q4', '1993-Q1', '1993-Q2', '1993-Q3', '1993-Q4', '1994-Q1', '1994-Q2', '1994-Q3', '1994-Q4', '1995-Q1', '1995-Q2', '1995-Q3', '1995-Q4', '1996-Q1', '1996-Q2', '1996-Q3', '1996-Q4', '1997-Q1', '1997-Q2', '1997-Q3', '1997-Q4', '1998-Q1', '1998-Q2', '1998-Q3', '1998-Q4', '1999-Q1', '1999-Q2', '1999-Q3', '1999-Q4', '2000-Q1', '2000-Q2', '2000-Q3', '2000-Q4', '2001-Q1', '2001-Q2', '2001-Q3', '2001-Q4', '2002-Q1', '2002-Q2', '2002-Q3', '2002-Q4', '2003-Q1', '2003-Q2', '2003-Q3', '2003-Q4', '2004-Q1', '2004-Q2', '2004-Q3', '2004-Q4', '2005-Q1', '2005-Q2', '2005-Q3', '2005-Q4', '2006-Q1', '2006-Q2', '2006-Q3', '2006-Q4', '2007-Q1', '2007-Q2', '2007-Q3', '2007-Q4', '2008-Q1', '2008-Q2', '2008-Q3', '2008-Q4', '2009-Q1', '2009-Q2', '2009-Q3', '2009-Q4', '2010-Q1', '2010-Q2', '2010-Q3', '2010-Q4', '2011-Q1', '2011-Q2', '2011-Q3', '2011-Q4', '2012-Q1', '2012-Q2', '2012-Q3', '2012-Q4', '2013-Q1', '2013-Q2', '2013-Q3', '2013-Q4', '2014-Q1', '2014-Q2', '2014-Q3', '2014-Q4', '2015-Q1', '2015-Q2', '2015-Q3', '2015-Q4', '2016-Q1', '2016-Q2', '2016-Q3', '2016-Q4', '2017-Q1', '2017-Q2', '2017-Q3', '2017-Q4', '2018-Q1', '2018-Q2', '2018-Q3', '2018-Q4', '2019-Q1', '2019-Q2', '2019-Q3', '2019-Q4', '2020-Q1', '2020-Q2', '2020-Q3', '2020-Q4', '2021-Q1', '2021-Q2', '2021-Q3', '2021-Q4', '2022-Q1', '2022-Q2', '2022-Q3', '2022-Q4', '2023-Q1', '2023-Q2', '2023-Q3', '2023-Q4', '2024-Q1', '2024-Q2', '2024-Q3', '2024-Q4']

# print(len(dates), len(nominal_gdp), len(price_index))

# Apply the same population to all 4 quarters of a year
expanded_population = []
for pop in population[0:]:  
    expanded_population += [pop] * 4

# Calculate real GDP in million euros
real_gdp = [(ngdp / pidx) * 100 for ngdp, pidx in zip(nominal_gdp, price_index)]

# Calculate real GDP per capita
real_gdp_per_capita = [rgdp * 1_000_000 / pop for rgdp, pop in zip(real_gdp, expanded_population)]

plt.figure(figsize=(16,6))
plt.plot(dates, real_gdp_per_capita, marker='o')
plt.title('Real GDP per Capita - Finland')
plt.xlabel('Date')
plt.ylabel('Real GDP per Capita (€)')

# Only show every 4th quarter
step = 4
plt.xticks(ticks=range(0, len(dates), step), labels=[dates[i] for i in range(0, len(dates), step)], rotation=45)

plt.grid(True)
plt.tight_layout()
plt.show(block=False)


''' Growth of real GDP per capita '''
# Uses the same data as the real GDP per capita

# Calculate quarterly growth rate (in %)
growth_rate = []

for i in range(1, len(real_gdp_per_capita)):
    growth = (real_gdp_per_capita[i] - real_gdp_per_capita[i-1]) / real_gdp_per_capita[i-1] * 100
    growth_rate.append(growth)

growth_dates = dates[1:]

# Calculate the average growth rate
average_growth = sum(growth_rate) / len(growth_rate)

plt.figure(figsize=(16,6))
plt.plot(growth_dates, growth_rate, marker='o', label='Quarterly Growth Rate')
plt.axhline(average_growth, color='red', linestyle=':', label=f'Average Growth Rate ({average_growth:.2f}%)')
plt.title('Growth Rate of Real GDP per Capita - Finland')
plt.xlabel('Date')
plt.ylabel('Growth Rate (%)')

# Only show every 4th quarter
step = 4
plt.xticks(ticks=range(0, len(growth_dates), step), labels=[growth_dates[i] for i in range(0, len(growth_dates), step)], rotation=45)

plt.axhline(0, color='black', linestyle='--')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show(block=False)


''' Unemployment rate '''

dates_unemp = pd.date_range(start='1988-01-01', end='2025-03-01', freq='MS')

unemployment_rate = [4.8, 4.6, 4.5, 4.4, 4.3, 4.3, 4.1, 4, 3.9, 3.8, 3.7, 3.6, 3.6, 3.5, 3.4, 3.2, 3.1, 3, 2.9, 2.9, 2.9, 2.9, 2.9, 2.9, 3, 3, 3, 3, 2.9, 2.9, 2.9, 3, 3.2, 3.5, 3.7, 3.9, 4.3, 4.6, 5, 5.4, 5.9, 6.4, 6.9, 7.5, 8, 8.3, 8.7, 9.2, 9.6, 9.9, 10.1, 10.5, 11, 11.6, 12.2, 12.6, 13, 13.3, 13.6, 13.9, 14.2, 14.7, 15.2, 15.6, 16.1, 16.5, 16.8, 17.1, 17.3, 17.5, 17.5, 17.6, 17.6, 16.6, 16.8, 17, 17.1, 17.1, 16.9, 16.5, 16.2, 15.9, 15.7, 15.5, 15.3, 15.1, 14.9, 14.8, 14.8, 14.9, 15, 15, 15, 15.1, 15.2, 15.3, 15.2, 15.1, 13.9, 14.1, 14.4, 14.7, 14.9, 14.9, 14.8, 14.6, 14.4, 13.6, 13.5, 13.4, 13.3, 13.2, 13, 12.7, 12.5, 12.3, 12.2, 12.1, 12, 11.9, 11.8, 11.7, 11.7, 11.7, 11.7, 11.6, 11.5, 11.3, 11, 10.9, 10.8, 10.8, 10.7, 10.6, 10.5, 10.4, 10.3, 10.3, 10.2, 10.1, 10, 10.1, 10.1, 10.1, 10.1, 10.2, 10.2, 10, 9.8, 9.6, 9.6, 9.6, 9.6, 9.5, 9.4, 9.3, 9.4, 9.4, 9, 9.2, 9.1, 9, 8.8, 8.9, 9.5, 9, 9.4, 8.9, 9.4, 9, 8.9, 9.2, 9.5, 8.7, 9.1, 9.2, 9, 9.2, 8.8, 9, 9.1, 8.6, 9.2, 9.4, 9.1, 9.4, 9, 8.7, 9, 9, 8.9, 9, 9, 8.7, 8.9, 9.5, 9.5, 8.6, 8.9, 9, 8, 8.6, 8.7, 8.4, 9.3, 8.9, 7.9, 8.9, 8.1, 8.3, 8.4, 8.1, 7.9, 7.8, 8.5, 8.4, 8.3, 8, 7.7, 7.7, 7.9, 7.7, 7.6, 7.7, 7.6, 7.7, 7.3, 7.1, 7.2, 7.2, 7.1, 6.5, 6.6, 6.9, 6.8, 6.8, 7.1, 6.6, 6.7, 6.6, 6.5, 6.1, 6.4, 5.7, 6.4, 6.4, 6.1, 6.4, 6.7, 6.3, 6.7, 6.7, 6.9, 7.5, 7.7, 8.2, 8.7, 8.7, 8.5, 8.8, 8.4, 9.1, 9.5, 8.5, 9.5, 8.9, 8.5, 8.6, 8.4, 8.6, 8.6, 8.5, 8.1, 8.3, 8.1, 8.6, 8.3, 8.2, 8.9, 7.7, 7.7, 8.3, 8, 7.6, 7.9, 7.8, 7.3, 8, 7.9, 7.4, 7.9, 7.6, 7.7, 7.7, 7.8, 8.4, 8, 7.7, 8.3, 7.6, 8.7, 8.5, 8.2, 8.2, 8.5, 7.4, 7.8, 8.2, 8.4, 8.1, 9, 8.5, 8.4, 8.8, 8.8, 8.3, 8.7, 8.9, 8, 8.5, 9.1, 9.1, 9.1, 9.4, 8.7, 9.7, 9.5, 9.5, 9.3, 9.9, 9.5, 9.5, 9.3, 9.5, 9.2, 9.7, 9.1, 9.1, 9.4, 8.9, 8.6, 9.3, 9, 8.4, 8.4, 8.9, 9.4, 8.5, 8.9, 9.1, 9, 9.3, 8.8, 8.9, 8.5, 8.4, 9, 8.2, 8, 9, 8.5, 8.4, 8.3, 7.7, 7.3, 7, 7.2, 7.4, 7, 7.2, 7.1, 5.9, 6.6, 7, 6.5, 7.2, 6.8, 6.2, 6.5, 7, 6.6, 6.9, 6.9, 6.5, 6.8, 6.7, 6.7, 7.2, 8.5, 7.7, 8.2, 8.8, 8.1, 8.2, 8, 8.2, 8.3, 8.1, 7.7, 8.5, 8.2, 7.7, 7.6, 7.1, 7.5, 6.7, 6.8, 7.3, 7, 6.6, 6.6, 6.2, 6.1, 6.9, 7.1, 7.3, 7.2, 6.4, 6.7, 7.3, 7.1, 6.6, 6.5, 7, 7.1, 7.2, 7.4, 7.5, 7.5, 7.5, 7.6, 7.6, 7.7, 7.7, 8.4, 8.3, 8.3, 8.4, 8.6, 8.3, 8.7, 8.9, 8.9, 8.7, 9, 9.2, 9.5]

# print(len(dates_unemp), len(unemployment_rate))

print("Average unemployment rate: ", np.average(unemployment_rate))
print("Minimum unemployment rate: ", np.min(unemployment_rate))
print("Maximum unemployment rate: ", np.max(unemployment_rate))

idx_min = np.argmin(unemployment_rate)
idx_max = np.argmax(unemployment_rate)
date_min = dates_unemp[idx_min]
date_max = dates_unemp[idx_max]
print(f"Minimum unemployment rate was on {date_min.strftime('%Y-%m')}")
print(f"Maximum unemployment rate was on {date_max.strftime('%Y-%m')}")

plt.figure(figsize=(16,6))
plt.plot(dates_unemp, unemployment_rate)
plt.title('Unemployment Rate - Finland')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show(block=False)


''' Inflation rate '''

dates_inflation = pd.date_range(start='1997-01-01', end='2025-03-01', freq='MS')

inflation_rate = [0.9, 0.6, 0.7, 0.9, 0.9, 1.1, 1.1, 1.7, 1.6, 1.7, 1.8, 1.6, 1.8, 1.7, 1.6, 1.7, 1.6, 1.6, 1.1, 1.1, 1.4, 1.1, 0.9, 0.8, 0.5, 0.9, 0.9, 1.3, 1.4, 1.2, 1.4, 1.3, 1.4, 1.6, 1.9, 2.2, 2.3, 2.7, 3.2, 2.5, 2.7, 3.1, 2.9, 2.9, 3.4, 3.4, 3.3, 2.9, 2.9, 2.7, 2.5, 2.9, 3.3, 3, 2.6, 2.7, 2.6, 2.4, 2.2, 2.3, 2.9, 2.5, 2.6, 2.5, 1.8, 1.5, 2, 1.8, 1.3, 1.7, 1.7, 1.7, 1.4, 2.1, 1.8, 1.4, 1.1, 1.1, 1, 1.2, 1.3, 0.9, 1.1, 1.2, 0.7, 0.4, -0.4, -0.4, -0.1, -0.1, 0.2, 0.2, 0.2, 0.6, 0.2, 0.1, -0.1, 0, 0.9, 1.2, 0.7, 1, 0.9, 1, 1.2, 0.8, 0.9, 1, 1.2, 1.3, 1.2, 1.5, 1.7, 1.5, 1.3, 1.3, 0.8, 1, 1.3, 1.2, 1.3, 1.2, 1.6, 1.5, 1.3, 1.4, 1.6, 1.3, 1.7, 1.8, 2.2, 1.9, 3.4, 3.3, 3.6, 3.3, 4.1, 4.3, 4.3, 4.6, 4.7, 4.4, 3.5, 3.4, 2.5, 2.7, 2, 2.1, 1.5, 1.6, 1.2, 1.3, 1.1, 0.6, 1.3, 1.8, 1.6, 1.3, 1.5, 1.6, 1.4, 1.3, 1.3, 1.3, 1.4, 2.4, 2.4, 2.8, 3.1, 3.5, 3.5, 3.4, 3.4, 3.4, 3.7, 3.5, 3.5, 3.2, 3.2, 2.6, 3, 3, 2.9, 3, 3.1, 2.9, 3.1, 3.3, 3.4, 3.5, 3.2, 3.4, 2.6, 2.4, 2.5, 2.4, 2.5, 2.3, 2.5, 2.1, 1.8, 1.7, 1.8, 1.9, 1.9, 1.6, 1.3, 1.3, 1, 1.1, 1, 1.2, 1.5, 1.2, 1.1, 0.6, -0.1, -0.1, 0, -0.1, 0.1, 0.1, -0.1, -0.2, -0.7, -0.3, -0.2, -0.2, 0, -0.1, 0, 0.3, 0.3, 0.3, 0.5, 0.5, 0.5, 0.6, 0.6, 1.1, 0.9, 1.4, 0.9, 1, 0.9, 0.9, 0.6, 0.8, 0.8, 0.5, 0.9, 0.5, 0.8, 0.6, 0.9, 0.8, 1, 1.2, 1.4, 1.4, 1.4, 1.7, 1.4, 1.3, 1.2, 1.3, 1.1, 1.5, 1.3, 1.1, 1, 1.2, 1, 0.9, 0.8, 1.1, 1.2, 1.1, 0.9, -0.3, -0.1, 0.1, 0.7, 0.3, 0.3, 0.2, 0.2, 0.2, 1, 0.9, 1.4, 2.2, 2.3, 1.9, 1.8, 1.8, 2.1, 2.8, 3.5, 3.2, 4.1, 4.4, 5.8, 5.8, 7.1, 8.1, 8, 7.9, 8.4, 8.4, 9.1, 8.8, 7.9, 8, 6.7, 6.3, 5, 4.1, 4.2, 3.1, 3, 2.4, 0.7, 1.3, 1.1, 1.1, 0.6, 0.6, 0.4, 0.5, 0.5, 1.1, 1, 1.5, 1.7, 1.6, 1.7, 1.5, 1.8]

# print(len(dates_inflation), len(inflation_rate))

plt.figure(figsize=(16,6))
plt.plot(dates_inflation, inflation_rate)
plt.title('Inflation Rate - Finland')
plt.xlabel('Date')
plt.ylabel('Inflation Rate (%)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show(block=False)





plt.show()


