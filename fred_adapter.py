from fredapi import Fred

fred = Fred(api_key='63fc387c98de1bee97a7659efb6ffa3a')

####################################################
# LEADING INDICATORS
####################################################

# M2 money supply
m2_df = fred.get_series('M2')

# Building permits / Housing starts
housing_starts_df = fred.get_series('HOUST')

# Average weekly claims for state unemployment compensation
unemployment_claims_df = fred.get_series('CCSA')

# Average work weeks in manufacturing
manufacturing_work_weeks_df = fred.get_series('AWHMAN')
manufacturing_work_weeks_df = manufacturing_work_weeks_df.dropna()

#Edit's by Kanchan Start

#COININCIDENT INDICATOR
#Number of Hours Worked
avg_annual_hours_df = fred.get_series('AVHWPEUSA065NRUG')

#Employment Level
employment_level_df = fred.get_series('CE16OV')

#GDP
GDP_df = fred.get_series('GDP')

#Edit's by Kanchan End
