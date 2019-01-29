# All technical Indicators will contain strategies to be used for a machine learning model and portfolio simulationself.

from talib import RSI

# get_functions()

def rsi_strategy_001(dfsource, length=14, overbought=80, oversold=20):
    """ Simple RSI strategy:
        [1] Buy: RSI(t-1) < Oversold(t-1) and RSI(t) > Oversold(t)
        [-1]Sell: RSI(t-1) > Overbought(t-1) and RSI(t) < Overbought(t)
        [0] Hold: Otherwise

        input: series

        returns: A list of results [{0,-1,1},..., n]
    """
    rsi = RSI(dfsource, length)
    results = []
    for i in range(len(rsi)):
        if rsi[i] == None:
            results.append(0)
            continue

        # Buy condition
        elif rsi[i-1] < oversold and rsi[i] > oversold:
            results.append(1)
        
        # Sell Condition
        elif rsi[i-1] > overbought and rsi[i] < overbought:
            results.append(-1)

        # Hold Condition
        else:
            results.append(0)

    return results
