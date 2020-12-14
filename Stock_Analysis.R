
#install.packages("ggplot2")
#install.packages("plyr")
#install.packages("dplyr")


library(plyr)
library(dplyr)
library(ggplot2)
library(readr)



setwd('C:/Users/aljackson/Documents/Environments/py_yfinance/')

stock_data_full <- read_csv("stock_data_full.csv", col_types = cols(X1 = col_date(format = "%Y-%m-%d")))

colnames(stock_data_full)[1] <- 'Date'

head(stock_data_full)

recent <- stock_data_full[stock_data_full$Date >= as.Date('2015-01-01'),]

table(recent$ticker)

azn <- recent[recent$ticker == 'AZN',]

ggplot(azn, aes(x = (Date), y = adjclose)) + geom_line(color = "darkblue") + ggtitle("AstraZeneca Adj Close Price") + xlab("Date") + ylab("Price") + theme(plot.title = element_text(hjust = 0.5)) + scale_x_date(date_labels = "%b %y", date_breaks = "6 months")

# Read in "eps_data.csv" and join to stock_data_full.csv

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
