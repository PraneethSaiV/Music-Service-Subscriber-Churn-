import pandas as pd

def read_saved(file):
    test_init = pd.read_csv(str(file), index_col = 0)
    
    headers = []
    for i in range(len(test_init.columns)):
        headers.append('{m} {year}'.format(m = test_init.columns[i], year = int(test_init.iloc[0,i])))

    test_init.columns = headers
    test_init = test_init.drop(test_init.index[[0,1]])
    return test_init

user_logs = pd.read_csv('user_logs_6_months.csv', header = None)
user_logs.columns = ['msno', 'date', 'num_25', 'num_50', 'num_75', 'num_985', 'num_100','num_unq', 'total_secs']
user_logs['msno'] = user_logs['msno'].astype(str)
user_logs['date'] = pd.to_datetime(user_logs['date'], format = '%Y%m%d')

user_logs['year_month'] = user_logs['date'].map(lambda x: 100*x.year + x.month)
user_logs = user_logs[user_logs['year_month'] > 201608]
user_log_monthly = user_logs.groupby(['msno', 'year_month']).sum()
user_log_monthly = user_log_monthly.reset_index()
user_log_monthly = user_log_monthly.pivot(index = 'msno', columns = 'year_month')
user_log_monthly = user_log_monthly.fillna(0)
user_log_monthly.columns = user_log_monthly.columns.map('{0[0]}|{0[1]}'.format)
user_log_monthly.to_csv('Month_Grouped.csv')
