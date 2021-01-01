
#install.packages("tidyquant")

library(tidyquant)
library(plyr)
library(dplyr)
library(ggplot2)
library(readr)
library(tidyr)

mac_wd = ''
win_wd = 'C:/Users/aljackson/Documents/Environments/py_yfinance/'
  
setwd(win_wd)


# Read in AV EPS data and transform it from long format to wide format so each stock symbol has one record and it can be neatly joined to Stocks & Fundamentals dataframe.


date <- '2020-12-24'
win_av_eps_path <- paste0('C:/Users/aljackson/Documents/Environments/py_yfinance/AV_EPS_Report_', date, '.csv')

av_eps <- read_csv(win_av_eps_path, col_types = cols(X1 = col_integer(), reportedDate = col_date(format = "%Y-%m-%d")))
colnames(av_eps)[1] <- 'index'

av_eps$unique_row <- paste0(av_eps$symbol, av_eps$index)
dupes<-av_eps[c('unique_row')]
av_eps<-av_eps[!duplicated(dupes),]

eps_list <- split(av_eps, av_eps$symbol)

pvt_wide_func <- function(df){
  myvars <- c('unique_row', 'reportedEPS', 'fiscalDateEnding')
  df <- df[myvars]
  pv_wide_df <- tidyr::pivot_wider(df, names_from = fiscalDateEnding, values_from = reportedEPS)
  pv_wide_df$symbol <- gsub('[[:digit:]]+', '', pv_wide_df$unique_row)
  pv_wide_df <- pv_wide_df[, !(colnames(pv_wide_df) == 'unique_row')]
  pv_final <- pv_wide_df %>%
    group_by(symbol) %>%
    summarise_all(funs(first(.[!is.na(.)])))
  return(pv_final)
}

pvt_wide_list <- lapply(eps_list, pvt_wide_func)
df_wide <- bind_rows(pvt_wide_list)
vars <- c('symbol', '2020-09-30', '2020-06-30', '2020-03-31', '2019-12-31', '2019-09-30', '2019-06-30', '2019-03-31', '2018-12-31', '2018-09-30', '2018-06-30', '2018-03-31', '2017-12-31')
eps_final <- df_wide[vars]

eps_final$eps_2020_09_30_chg <- eps_final$`2020-09-30` - eps_final$`2020-06-30`
eps_final$eps_2020_06_30_chg <- eps_final$`2020-06-30` - eps_final$`2020-03-31`
eps_final$eps_2020_03_31_chg <- eps_final$`2020-03-31` - eps_final$`2019-12-31`
eps_final$eps_2019_12_31_chg <- eps_final$`2019-12-31` - eps_final$`2019-09-30`
eps_final$eps_2020_09_yr_chg <- eps_final$`2020-09-30` - eps_final$`2019-09-30`


# calc_eps_pct_chg <- function(df){
#   df$eps_last_qtr_chg <- ifelse(length(df$symbol) > 1, (df$actual[df$rank == max(df$rank)] - df$actual[df$rank == max(df$rank-1)]) /df$actual[df$rank == max(df$rank-1)], 0)
#   df$eps_2qtr_chg <- ifelse(length(df$symbol) >= 3, (df$actual[df$rank == max(df$rank)] - df$actual[df$rank == max(df$rank-2)]) /df$actual[df$rank == max(df$rank-2)], 0)
#   df$eps_3qtr_chg <- ifelse(length(df$symbol) >= 4, (df$actual[df$rank == max(df$rank)] - df$actual[df$rank == max(df$rank-3)]) /df$actual[df$rank == max(df$rank-3)], 0)
#   return(df)
# }
# df_list_out <- lapply(eps_list, calc_eps_pct_chg)
# df_eps<-ldply(df_list_out, data.frame)
#write_csv(df_eps, 'eps_pct_chg.csv')


# Read in AV Stock and Fundamentals data and merge it with transformed EPS dataframe above (eps_final)

mac_av_stocks_path <- "~/Documents/Environments/stocks_env/AV_StocksFundamentals_Merged.csv"

win_av_stocks_path <- paste0('C:/Users/aljackson/Documents/Environments/py_yfinance/AV_Stocks&Fundamentals_Merged_', date, '.csv')

av_stocks <- read_csv(win_av_stocks_path, col_types = cols(LatestQuarter = col_date(format = "%Y-%m-%d"), X1 = col_integer(), date = col_date(format = "%Y-%m-%d")))
colnames(av_stocks)[1] <- 'Index'

av_merged <- merge(av_stocks, eps_final, by.x = 'Symbol', by.y = 'symbol', all.x = TRUE)

av_merged$avg_price <- (av_merged$high + av_merged$`adj close` + av_merged$low) / 3
av_merged$AvgPriceXVol <- av_merged$avg_price * av_merged$volume

av_merge_split <- split(av_merged, av_merged$symbol)

# Extract of full list to test following function on:
av_merge_split <- av_merge_split[1:3]


# https://www.youtube.com/watch?v=L1J3M9jEWvQ

VMAP_func <- function(df){
  df <- df %>%
    mutate(avg_price_lag0 = avg_price,
           avg_price_lag1 = lag(avg_price, n = 1, order_by = date),
           avg_price_lag2 = lag(avg_price, n = 2, order_by = date),
           avg_price_lag3 = lag(avg_price, n = 3, order_by = date),
           avg_price_lag4 = lag(avg_price, n = 4, order_by = date))
  df <- df %>%
    mutate(APXVol_lag0 = AvgPriceXVol,
           APXVol_lag1 = lag(AvgPriceXVol, n = 1, order_by = date),
           APXVol_lag2 = lag(AvgPriceXVol, n = 2, order_by = date),
           APXVol_lag3 = lag(AvgPriceXVol, n = 3, order_by = date),
           APXVol_lag4 = lag(AvgPriceXVol, n = 4, order_by = date),
           Vol_lag0 = volume,
           Vol_lag1 = lag(volume, n = 1, order_by = date),
           Vol_lag2 = lag(volume, n = 2, order_by = date),
           Vol_lag3 = lag(volume, n = 3, order_by = date),
           Vol_lag4 = lag(volume, n = 4, order_by = date))
  df <- df %>%
    mutate(VMAP_4wk = (APXVol_lag0 + APXVol_lag1 + APXVol_lag2 + APXVol_lag3 + APXVol_lag4)/(Vol_lag0 + Vol_lag1 + Vol_lag2 + Vol_lag3 + Vol_lag4))
  df <- df %>%
    mutate(StDev_4wk = sd(c(avg_price_lag0, avg_price_lag1, avg_price_lag2, avg_price_lag3, avg_price_lag4), na.rm = T))
  df <- df %>%
    mutate(Upper_BB = VMAP_4wk + (StDev_4wk * 1))
  df <- df %>%
    mutate(Lower_BB = VMAP_4wk - (StDev_4wk * 1))
  
  return(df)
}

av_merge_split <- lapply(av_merge_split, VMAP_func)

av_merged <- ldply(av_merge_split, data.frame)

sq <- av_merged[av_merged$symbol == 'SQ',]
# write_csv(test, 'test_lag44.csv')


p = ggplot() + 
  geom_line(data = sq, aes(x = date, y = `adj.close`), color = "blue") +
  geom_line(data = sq, aes(x = date, y = VMAP_4wk), color = "red") +
  geom_line(data = sq, aes(x = date, y = Upper_BB), color = "black") +
  geom_line(data = sq, aes(x = date, y = Lower_BB), color = "black") +
  geom_hline(yintercept = min(sq$adj.close)) +
  #geom_hline(yintercept = max(sq$adj.close)) +
  xlab('Dates') +
  ylab('Adj Close')


p3 = ggplot() + 
  geom_line(data = sq, aes(x = date, y = volume), color = 'purple') +
  xlab('Dates') +
  ylab('Volume')

#print(p)

install.packages('gtable')
library(gtable)
library(grid)
g2 <- ggplotGrob(p)
g3 <- ggplotGrob(p3)
g <- rbind(g2, g3, size = "first")
#g$widths <- unit.pmax(g2$widths, g3$widths)
#grid.newpage()
#grid.draw(g)

grid.draw(g)





mid_range_stocks <- av_merged[av_merged$`adj close` >= 10 & av_merged$`adj close` <= 30 & av_merged$eps_last_qtr_chg > 0 & av_merged$eps_2020_09_yr_chg > 0 & av_merged$MarketCapitalization >= 1000000000,]

small_cap <- mid_range_stocks[which(!is.na(mid_range_stocks[,1])),]

write_csv(small_cap, 'mid_range_stocks.csv')

# Let's start plotting!

azn <- av_merged[av_merged$symbol == 'AZN',]
sq <- av_merged[av_merged$symbol == 'SQ',]
apple <- av_merged[av_merged$symbol == 'AAPL',]

# https://www.reed.edu/data-at-reed/resources/R/loops_with_ggplot2.html
# ggplot(i, aes(x = (date), y = `adj close`)) + geom_line(color = "darkblue") + ggtitle("AstraZeneca Adj Close Price") + xlab("Date") + ylab("Price") + theme(plot.title = element_text(hjust = 0.5)) + scale_x_date(date_labels = "%b %y", date_breaks = "6 months") + geom_bbands(aes(high = high, low = low, close = `adj close`, volume = volume), ma_fun = VWMA, n = 7)


stock_list <- list(azn, sq, apple)
  
for(i in  stock_list) {
  plot <- ggplot(i, aes(x = (date), y = `adj close`)) + geom_line(color = "darkblue") + ggtitle("AstraZeneca Adj Close Price") + xlab("Date") + ylab("Price") + theme(plot.title = element_text(hjust = 0.5)) + scale_x_date(date_labels = "%b %y", date_breaks = "6 months") + geom_bbands(aes(high = high, low = low, close = `adj close`, volume = volume), ma_fun = VWMA, n = 20)
  print(plot)
  par(ask = TRUE)
}

