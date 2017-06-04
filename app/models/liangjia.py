from .data_func import table2df, df2html, week_date


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