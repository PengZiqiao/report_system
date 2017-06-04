from app.models.data_func import table2df, df2html, week_date
from app.models.file_path import STATIC_PATH
import pandas as pd


class LiangJia:
    def __init__(self, filename, wuye):
        self.df = table2df(filename, wuye)

    def plate_table(self):
        df = self.df.ix[:-1, ['上市面积', '已售面积', '均价']]
        return df2html(df)

    def gxj_table(self):
        df = self.df.loc['合计':'合计', ['周数', '日期', '上市面积', '已售面积', '均价']]
        df[['周数', '日期']] = week_date()
        return df2html(df)

    def data_dict(self):
        s = self.df.iloc[-1]
        return s.to_dict()


class HuaRunLiangjia(LiangJia):
    def gxj_table(self):
        df = self.df.loc['合计':'合计', ['周数', '日期', '上市面积', '认购面积', '已售面积', '均价']]
        df[['周数', '日期']] = week_date()
        return df2html(df)


class Rank:
    def __init__(self, filename, wuye):
        path = f'{STATIC_PATH}/data/{filename}.xlsx'
        df = pd.read_excel(path, f'{wuye}-排行', index_col='排名')
        df['面积'] = round(df['面积'] / 1e4, 2)
        df['金额'] = round(df['金额'] / 1e4, 2)
        self.df = df

    def table(self):
        return df2html(self.df)
