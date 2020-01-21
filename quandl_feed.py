#install quandl first
import quandl

quandl.ApiConfig.api_key = 'Rhzxnk4YNsZxJFyycLuK'

#Leading Indicator : Stock Price
stock_eod_data = quandl.get('EOD/HD', start_date='2017-12-28', end_date='2017-12-28')
print (stock_eod_data)

#Output
#              Open    High     Low   Close     Volume  Dividend  Split  \
#Date                                                                     
#2017-12-28  190.91  190.98  189.64  189.78  3175631.0       0.0    1.0   
#
#              Adj_Open    Adj_High   Adj_Low   Adj_Close  Adj_Volume  
#Date                                                                  
#2017-12-28  181.803521  181.870182  180.5941  180.727422   3175631.0 
