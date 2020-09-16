

install.packages("alphavantager")
library(alphavantager)
av_api_key("YBPBDWS569VUQ3I2")
c_full<-av_get(symbol = "MSFT", av_fun = 'TIME_SERIES_DAILY_ADJUSTED', outputsize = 'full')


### 9/16/2020 ###


df_total <- data.frame()
ticker_vector <- c('MSFT', 'NFLX', 'NIO', 'WKHS', 'NKLA', 'PRTK', 'EIGR', 'ATRA', 'VKTX', 'VXRT',
                   'JNJ', 'NVAX', 'AZN', 'INO', 'MRNA', 'TTNP', 'BA')

company_vector <- c('Microsoft', 'Netflix', 'Nio (Electric Car)', 'Workhorse Group Inc', 'Nikola Corp',
                    'Paratek Pharma', 'Eiger Biopharm', 'Atara biotherapeutics', 'Viking Therapeutics',
                    'Vaxart Pharma', 'Johnson&Johnson', 'Novavax Pharm', 'AstraZeneca Pharm', 
                    'Inovio Pharma', 'Moderna Pharma', 'Titan Pharma', 'Boeing')

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

