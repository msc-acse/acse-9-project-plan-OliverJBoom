import pandas as pd
import quandl
import matplotlib.pyplot as plt


def get_engagement():
    engagement_data = quandl.get_table('SMA/FBD', brand_ticker='AAPL',
                            qopts={"columns": ["brand_ticker", "sector", "date", "engagement_score"]},
                            date={'gte': '2017-01-01', 'lte': '2017-07-18'})
    mean_engagement = engagement_data.groupby(['brand_ticker', 'sector', 'date'])['engagement_score'].mean()
    return engagement_data, mean_engagement


def main():
    API_key = "2TCh5Acf5dsnUvJ8XgMT"
    quandl.ApiConfig.api_key = API_key
    financial_data = quandl.get_table('SHARADAR/SEP', date={'gte':'2017-01-01', 'lte':'2017-10-30'}, ticker='AAPL')
    financial_data.plot(kind="line", x='date', y='close')
    # plt.show()
    engagement_data = quandl.get_table('SMA/FBD', brand_ticker='AAPL',
                            qopts={"columns": ["brand_ticker", "sector", "date", "engagement_score"]},
                            date={'gte': '2017-01-01', 'lte': '2017-07-18'})
    mean_engagement = engagement_data.groupby(['brand_ticker', 'sector', 'date'])['engagement_score'].mean()

    # engagement_data, mean_engagement = get_engagement()
    print(mean_engagement)
    engagement_data.plot(kind="line", x='date', y='engagement_score')
    plt.show()
    mean_engagement.plot(kind="line", x='date', y='close')
    # plt.show()


if __name__ == '__main__':
    main()