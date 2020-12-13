
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
  #pv_wide_df <- reshape::melt(as.matrix(pv_wide_df), na.rm = T)
  pv_wide_df$symbol <- gsub('[[:digit:]]+', '', pv_wide_df$unique_row)
  pv_wide_df <- pv_wide_df[, !(colnames(pv_wide_df) == 'unique_row')]
  pv_final <- pv_wide_df %>%
    group_by(symbol) %>%
    summarise_all(funs(first(.[!is.na(.)])))
  return(pv_final)
  }

pvt_wide_list <- lapply(eps_list, pvt_wide_func)

df_wide <- bind_rows(pvt_wide_list)


setwd('~/Documents/Environments/stocks_env/')

head(df_wide)

write_csv(eps_wide, 'eps_wide.csv')

# add calc fields

