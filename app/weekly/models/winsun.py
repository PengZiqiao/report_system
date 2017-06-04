from ...models.liangjia import LiangJia

wuye_list = ['住宅', '商业', '办公']
gxj, plate, data = dict(), dict(), dict()
for wuye in wuye_list:
    lj = LiangJia('weekly', wuye)
    gxj[wuye] = lj.gxj_table()
    plate[wuye] = lj.plate_table()
    data[wuye] = lj.data_dict()
