

#setwd("/Users/alanjackson/Documents/Environments/stocks_env")

nyse <- NYSE

stocks <- as.data.frame(nyse[,1])
a <- paste0("'", stocks$Symbol, "'")
x1 <- str_replace_all(a, "[\r\n]", "")
write.csv(as.data.frame(x1), 'stock_ticers_all.csv', quote = FALSE, row.names = FALSE, eol = ',')