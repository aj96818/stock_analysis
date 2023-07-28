
select * from txns where symbol = 'eth' order by txn_id desc;

use crypto_tracker_db;

-- This table needs to be dropped before new day's prices are obtained.

drop table prices;

create table prices (
	row_id int not null auto_increment
    , Symbol VARCHAR(25)
    , `name` VARCHAR(75)
    , date_added VARCHAR(25)
    , last_updated VARCHAR(25)
    , price_usd decimal(15, 5)
	, volume_24h decimal(35, 5)
    , market_cap decimal(35, 5)
    , percent_change_24h decimal(10, 4)
    , percent_change_7d decimal(10, 4)
    , percent_change_30d decimal(10, 4)
    , percent_change_60d decimal(10, 4)
    , percent_change_90d decimal(10, 4)
    , primary key (row_id));

--------------------------------------    
-- then run 'latest_prices_app.py' !!!
--------------------------------------


-- Drop balances if exists; will recreate it down below.

DROP TABLE balances;

CREATE TABLE balances (
	symbol VARCHAR(25)
    , quantity decimal(12, 5)
    , price_usd decimal(12, 5)
    , total_amount decimal(25, 6)
);

-- https://stackoverflow.com/questions/24008316/insert-into-from-cte

INSERT INTO balances
	WITH
		accounts_cte AS (SELECT 
					symbol
                    , sum(quantity) 'accounts_quantity'
              FROM accounts
              GROUP BY
				symbol),
		prices_cte AS (SELECT
					symbol
                    , price_usd
				FROM prices)
                    
SELECT
	accounts_cte.symbol as symbol
    , accounts_cte.accounts_quantity as quantity
    , prices_cte.price_usd as price_usd
    , (accounts_cte.accounts_quantity * prices_cte.price_usd) as total_amount
FROM
	accounts_cte
JOIN
	prices_cte
WHERE 
	accounts_cte.symbol = prices_cte.symbol;

select * from balances order by total_amount desc;
select sum(total_amount) from balances where symbol not in ('btc', 'eth');
# order by total_amount desc;

select sum(quantity) from accounts where symbol = 'btc';
select sum(quantity) from accounts where symbol = 'eth';
select * from accounts;

select symbol, quantity, total_amount from balances order by total_amount desc;-- where symbol not in ('btc', 'eth');

use crypto_tracker_db;

SELECT * FROM accounts order by symbol desc;
select * from accounts where symbol = 'avax';
select 
  ((price * quantity) + fee) as spent
  , quantity
  , symbol
  , txn_type
  , price
  , exchange_name
  from txns order by txn_id desc;




select distinct name from prices order by name desc;

-- Binance Historical Prices from Testnet

drop table binance;
create table binance (
	row_id int not null auto_increment
    , symbol VARCHAR(25)
    , price decimal(15, 5)
    , close_date date
    , primary key (row_id));

select * from binance;

select * from txns;

select sum(price * quantity) as cost
from txns
where txn_type = 'BUY';

select sum(price * quantity) as cost
from txns
where txn_type = 'SELL';
