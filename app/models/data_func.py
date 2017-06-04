import pandas as pd


def table2df(filename, sheet):
    # set path
    from .file_path import STATIC_PATH
    path = f'{STATIC_PATH}/data/{filename}.xlsx'

    # read table to DateFrame
    df = pd.read_excel(path, sheet, index_col=0)

    # ㎡ to 万㎡
    for each in ['上市', '认购', '已售']:
        df[f'{each}面积'] = round(df[f'{each}面积'] / 1e4, 2)

    # 同环比转成涨跌文字
    for each in df:
        if '比' in each:
            df[each] = df[each].apply(zhang_die)

    return df


def df2html(df):
    return df.to_html(classes='table table-bordered table-condensed table-hover table-responsive', border=0)


def zhang_die(rate):
    """判断环比上涨或下降"""
    try:
        change = "下降" if rate < 0 else "上涨"
    except:
        return "NA"
    return "{}{}%".format(change, round(abs(rate)))


def week_date():
    import datetime
    import calendar
    sunday = datetime.datetime.today()
    while sunday.weekday() != calendar.SUNDAY:
        sunday -= datetime.timedelta(days=1)
    monday = sunday - datetime.timedelta(days=6)
    date = "{}-{}".format(monday.strftime("%m.%d"), sunday.strftime("%m.%d"))
    week = "第{}周".format(monday.strftime("%U"))
    return week, date
