

#install.packages("alphavantager")
library(alphavantager)
av_api_key("YBPBDWS569VUQ3I2")


install.packages("request")
library(request)


### 9/16/2020 ###


df_total <- data.frame()
ticker_vector <- c('MSFT', 'NFLX', 'NIO', 'WKHS', 'NKLA', 'PRTK', 'EIGR', 'ATRA', 'VKTX', 'VXRT',
                   'JNJ', 'NVAX', 'AZN', 'INO', 'MRNA', 'TTNP', 'BA', 'SNOW', 'FSLR', 'JOBS',
                   'APPS', 'SRNE', 'OM', 'CRNC', 'CDLX', 'EBON', 'ATEX')

company_vector <- c('Microsoft', 'Netflix', 'Nio (Electric Car)', 'Workhorse Group Inc', 'Nikola Corp',
                    'Paratek Pharma', 'Eiger Biopharm', 'Atara biotherapeutics', 'Viking Therapeutics',
                    'Vaxart Pharma', 'Johnson&Johnson', 'Novavax Pharm', 'AstraZeneca Pharm', 
                    'Inovio Pharma', 'Moderna Pharma', 'Titan Pharma', 'Boeing', 'Snowflake', 'First Solar', '51job', 'Digital Turbine', 'Sorento Therapeutics', 'Outset Medical', 'Cerence', 'Cardlytics', 'Ebang', 'Anterix')

stock_lookup <- data.frame(ticker_vector, company_vector)
names(stock_lookup) <- c('Ticker', 'Company')


for (stock in ticker_vector){
   output <- av_get(symbol = stock, av_fun = 'TIME_SERIES_DAILY_ADJUSTED', outputsize = 'full')
   output$Ticker <- stock
   df <- data.frame(output)
   df_total <- rbind(df_total, df)
   Sys.sleep(15)
}

df <- merge(df_total, stock_lookup, by = 'Ticker')



test <- av_get(symbol = 'MSFT', av_fun = 'INCOME_STATEMENT')


# R 'request' library

path = 'https://www.alphavantage.co'

r <- GET(url = path,
         apikey = 'YBPBDWS569VUQ3I2',
         av_fun = 'OVERVIEW',
         query = list(LatestQuarter = '2020-03-31'))

r$status_code

r <- GET('https://www.alphavantage.co/query?function=OVERVIEW&symbol=MSFT&apikey=YBPBDWS569VUQ3I2',
         query = list(LatestQuarter = '2020-03-31'))


response <- content(r, as = 'text', encoding = 'UTF-8')


content(r)$doc


r <- GET("http://httpbin.org/get", 
         query = list(key1 = "value 1", "key 2" = "value2", key2 = NULL))


str(content(r))

class(content(r))

length((content(r)))

c <- x %>% http()



