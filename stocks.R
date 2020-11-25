
#install.packages("ggplot2")

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



