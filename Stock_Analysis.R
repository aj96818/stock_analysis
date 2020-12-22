
#install.packages("tidyr")

library(plyr)
library(dplyr)
library(ggplot2)
library(readr)
library(tidyr)

mac_wd = ''
win_wd = 'C:/Users/aljackson/Documents/Environments/py_yfinance/'
  
setwd(win_wd)


# Read in AV EPS data and transform it from long format to wide format so each stock symbol has one record and it can be neatly joined to Stocks&Fundamentals dataframe.

win_av_eps_path <- 'C:/Users/aljackson/Documents/Environments/py_yfinance/AV_EPS_Data.csv'
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
win_av_stocks_path <- 'C:/Users/aljackson/Documents/Environments/py_yfinance/AV_StocksFundamentals_Merged.csv'

av_stocks <- read_csv(win_av_stocks_path, col_types = cols(LatestQuarter = col_date(format = "%Y-%m-%d"), X1 = col_integer(), date = col_date(format = "%Y-%m-%d")))
colnames(av_stocks)[1] <- 'Index'


av_merged <- merge(av_stocks, eps_final, by.x = 'Symbol', by.y = 'symbol', all.x = TRUE)



# Let's start plotting!

azn <- recent[recent$ticker == 'AZN',]
ggplot(azn, aes(x = (Date), y = adjclose)) + geom_line(color = "darkblue") + ggtitle("AstraZeneca Adj Close Price") + xlab("Date") + ylab("Price") + theme(plot.title = element_text(hjust = 0.5)) + scale_x_date(date_labels = "%b %y", date_breaks = "6 months")







