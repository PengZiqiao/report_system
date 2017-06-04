from flask import render_template

from . import weekly


@weekly.route('/winsun')
def winsun():
    from .models.winsun import wuye_list, gxj, plate, data
    return render_template('weekly/winsun.html', **locals())
