from Artificial_Agents.Technical_Indicators import RSI_strategies
from data.Crypto import cryptocompareapi
import pickle
import pandas as pd

symbol = 'BTC'
comparison_symbol = 'USD'
strategy = 'strategy001'
df = cryptocompareapi.daily_price_historical(symbol, comparison_symbol)
df.to_pickle("./cryptocompare_daily_BTCUSD.pkl")
df = pd.read_pickle("./cryptocompare_daily_BTCUSD.pkl")


results = RSI_strategies.rsi_strategy_001(df.close)

def portfolio_simulation(df):
    capital = 10000
    portfolio_value = [capital]
    commission = 0.01 # Percentage of each trade
    start_date = df.index[0]
    end_date = df.index[-1]
    buy_strategy='strategy001'
    df[buy_strategy] = results
    sell_strategy=''
    risk_management=''

    # iterate over every day and decide to buy or sell
    shares_bought = 0
    net_gain = [0]
    action = ["initialize"]
    timestamp = [start_date]
    price = [df.close[start_date]]
    equity = [0]
    history = {}
    for i in range(len(df)-1):
        if df.strategy001[i] == 0: # Do Nothing
            continue

        elif df.strategy001[i] == 1:
            if capital == 0: # If we have no money do nothing
                continue

            # Implement Investment strategy
            action.append("Buy")
            shares_bought = capital/df.open[i+1] # Buy all shares possible
            equity.append(shares_bought)
            capital = capital-shares_bought*df.open[i+1]

        elif df.strategy001[i] == -1:
            if shares_bought == 0: # If we have no shares to sell Do nothing.
                continue

            # Implement sell strategy
            action.append("Sell")
            net = shares_bought*df.open[i+1]
            shares_bought = 0
            equity.append(shares_bought)
            capital = capital+net

        timestamp.append(df.index[i])
        price.append(df.close[i])
        portfolio_value.append(shares_bought*df.close[i] + capital)
        net_gain.append(portfolio_value[-1]-portfolio_value[-2])

    history = {"{}".format(symbol+comparison_symbol): price,
               "Equity": equity,
               "Portfolio_Value": portfolio_value,
               "Net_Gain": net_gain,
               "Action": action}

    return pd.DataFrame(history, index=timestamp)

history = portfolio_simulation(df)
ROI = history.Portfolio_Value[-1]/history.Portfolio_Value[0]*100
overview = ("Start Value: $%.2f\n"
            "End Value: $%.2f\n"
            ""
            "ROI: %.2f%%"
            % (history.Portfolio_Value[0],
               history.Portfolio_Value[-1],
               ROI))
# Name 	Gain 	Abs. Gain 	Daily 	Monthly 	Drawdown 	Balance 	Equity 	Profit 	Pips 	Deposits
print(overview)
test = {"Name":symbol+comparison_symbol+strategy,
        "Abs. Gain %":round(history.Portfolio_Value[-1]/history.Portfolio_Value[0]*100,2),
        "Drawdown":}
test
history
history.Portfolio_Value[-1]/history.Portfolio_Value[0]
DD = [x for i in len(history) min(history.Portfolio_Value[i] - max(history.Portfolio_Value))/max(history.Portfolio_Value)]


create_sharpe_ratio(history.Portfolio_Value.pct_change(1), periods=len(history))
