from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG
import pandas as pd


def _read_file(filename):
    from os.path import dirname, join

    return pd.read_csv(join(dirname(__file__), filename),
                       index_col=0, parse_dates=True, infer_datetime_format=True)


TSMC = _read_file('./2330.TW.csv')


class SmaCross(Strategy):
    n1 = 10
    n2 = 20

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()


if __name__ == '__main__':
    bt = Backtest(TSMC, SmaCross,
                  cash=10000, commission=.002,
                  exclusive_orders=True)

    output = bt.run()
    print(output)
    bt.plot()
