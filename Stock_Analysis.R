
#install.packages("tidyr")

library(plyr)
library(dplyr)
library(ggplot2)
library(readr)
library(tidyr)

mac_wd = ''
win_wd = 'C:/Users/aljackson/Documents/Environments/py_yfinance/'
  
setwd(win_wd)

# Read in Alpha Vantage stock data merged with Alpha Vantage Fundamentals data:


av_stocks <- read_csv("~/Documents/Environments/stocks_env/AV_StocksFundamentals_Merged.csv", col_types = cols(LatestQuarter = col_date(format = "%Y-%m-%d"), X1 = col_integer(), date = col_date(format = "%Y-%m-%d")))
colnames(av_stocks)[1] <- 'Index'

av_eps <- read_csv("~/Documents/Environments/stocks_env/AV_EPS_Data.csv", col_types = cols(X1 = col_integer(), reportedDate = col_date(format = "%Y-%m-%d")))
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

vars <- c('symbol', '2020-09-30', '2020-06-30', '2020-03-31', '2019-12-31')

eps_final <- df_wide[vars]









setwd('C:/Users/aljackson/Documents/Environments/py_yfinance/')
eps_data <- read_csv("eps_data.csv", col_types = cols(period = col_date(format = "%Y-%m-%d")))

eps_data <- eps_data[,2:5]

eps_ranked_dates <- eps_data %>% group_by(symbol) %>%
  mutate(rank = rank(period)) %>% arrange(symbol)

eps_list <- split(eps_ranked_dates, f = eps_ranked_dates$symbol)

#(df$actual[df$rank == max(df$rank)] - df$actual[df$rank == max(df$rank-1)]) /df$actual[df$rank == max(df$rank-1)]


calc_eps_pct_chg <- function(df){
  df$eps_last_qtr_chg <- ifelse(length(df$symbol) > 1, (df$actual[df$rank == max(df$rank)] - df$actual[df$rank == max(df$rank-1)]) /df$actual[df$rank == max(df$rank-1)], 0)
  df$eps_2qtr_chg <- ifelse(length(df$symbol) >= 3, (df$actual[df$rank == max(df$rank)] - df$actual[df$rank == max(df$rank-2)]) /df$actual[df$rank == max(df$rank-2)], 0)
  df$eps_3qtr_chg <- ifelse(length(df$symbol) >= 4, (df$actual[df$rank == max(df$rank)] - df$actual[df$rank == max(df$rank-3)]) /df$actual[df$rank == max(df$rank-3)], 0)
  return(df)
  }


df_list_out <- lapply(eps_list, calc_eps_pct_chg)
df_eps<-ldply(df_list_out, data.frame)
#write_csv(df_eps, 'eps_pct_chg.csv')



# Let's start plotting!

azn <- recent[recent$ticker == 'AZN',]
ggplot(azn, aes(x = (Date), y = adjclose)) + geom_line(color = "darkblue") + ggtitle("AstraZeneca Adj Close Price") + xlab("Date") + ylab("Price") + theme(plot.title = element_text(hjust = 0.5)) + scale_x_date(date_labels = "%b %y", date_breaks = "6 months")







