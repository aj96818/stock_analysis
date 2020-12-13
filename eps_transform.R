
#install.packages("reshape")

library(tidyr)
library(plyr)
library(dplyr)
library(readr)
library(reshape)

eps_data <- read_csv("~/Documents/Environments/stocks_env/eps_data.csv", col_types = cols(period = col_date(format = "%Y-%m-%d")))
colnames(eps_data)[1] <- 'index'
eps_data$unique_row <- paste0(eps_data$symbol, eps_data$index)
dupes<-eps_data[c('unique_row')]
eps_data<-eps_data[!duplicated(dupes),]
eps_list <- split(eps_data, eps_data$symbol)

pvt_wide_func <- function(df){
  myvars <- c('unique_row', 'actual', 'period')
  df <- df[myvars]
  pv_wide_df <- tidyr::pivot_wider(df, names_from = period, values_from = actual)
  return(pv_wide_df)
  }

pvt_wide_list <- lapply(eps_list, pvt_wide_func)
df_wide <- bind_rows(pvt_wide_list)

setwd('~/Documents/Environments/stocks_env/')
write_csv(eps_wide, 'eps_wide.csv')

# drop na's ...

# rename columns

# add calc fields

