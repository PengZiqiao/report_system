from flask import render_template

from . import weekly


@weekly.route('/winsun')
def winsun():
    from app.weekly.models import LiangJia, Rank
    wuye_list = ['住宅', '商业', '办公', '别墅']
    gxj, plate, data, rank = dict(), dict(), dict(), dict()
    for wuye in wuye_list:
        lj = LiangJia('weekly', wuye)
        gxj[wuye] = lj.gxj_table()
        plate[wuye] = lj.plate_table()
        data[wuye] = lj.data_dict()
        if wuye != '别墅':
            rank[wuye] = Rank('weekly', wuye).table()
    return render_template('weekly/winsun.html', **locals())


@weekly.route('/huarun')
def huarun():
    from app.weekly.models import HuaRunLiangjia, LiangJia, Rank
    # 住宅
    lj = HuaRunLiangjia('weekly', '住宅（含别墅）')
    rank = {'住宅': Rank('weekly', '住宅（含别墅）').table()}
    gxj = {'住宅': lj.gxj_table()}
    data = {'住宅': lj.data_dict()}
    # 商办
    for wuye in ['商业', '办公']:
        lj = LiangJia('weekly', wuye)
        gxj[wuye] = lj.gxj_table()
        data[wuye] = lj.data_dict()
        rank[wuye] = Rank('weekly', wuye).table()
    return render_template('weekly/huarun.html', **locals())
