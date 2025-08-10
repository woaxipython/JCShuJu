import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # 或 'Qt5Agg'
import matplotlib.pyplot as plt



class JiSuanChanChu(object):
    def __init__(self, ZhiChengRenYuan, KaiPinShuLiang, SuoXuPR, TouRuZhouQi,
                 YueHeShuLiang, YueHeDanJia, UnitPrice, YuGuXiaoLiang, ChengGongLv, LiRunLv):
        self.ZhiChengRenYuan = self.YuChuLi_Int(ZhiChengRenYuan) if self.YuChuLi_Int(ZhiChengRenYuan) else False
        self.KaiPinShuLiang = self.YuChuLi_Int(KaiPinShuLiang) if self.YuChuLi_Int(KaiPinShuLiang) else False
        self.SuoXuPR = self.YuChuLi_Int(SuoXuPR) if self.YuChuLi_Int(SuoXuPR) else False
        self.TouRuZhouQi = self.YuChuLi_Int(TouRuZhouQi) if self.YuChuLi_Int(TouRuZhouQi) else False
        self.YueHeShuLiang = self.YuChuLi_Int(YueHeShuLiang) if self.YuChuLi_Int(YueHeShuLiang) else False
        self.YueHeDanJia = self.YuChuLi_Int(YueHeDanJia) if self.YuChuLi_Int(YueHeDanJia) else False

        self.UnitPrice = self.YuChuLi_Int(UnitPrice) if self.YuChuLi_Int(UnitPrice) else False
        self.YuGuXiaoLiang = self.YuChuLi_Int(YuGuXiaoLiang) if self.YuChuLi_Int(YuGuXiaoLiang) else False
        self.ChengGongLv = self.YuChuLi_float(ChengGongLv) if self.YuChuLi_float(ChengGongLv) else False
        self.LiRunLv = self.YuChuLi_float(LiRunLv) if self.YuChuLi_float(LiRunLv) else False

        # 如果为False，则返回False

        # 常量
        self.ZhiChengGongZi = 11000
        self.KaiPinYuSuan = 5000
        self.PRGongZi = 7000
        self.TuiKuanLv = 0.2

    def init(self):
        if not self.ZhiChengRenYuan or not self.KaiPinShuLiang or not self.SuoXuPR or not self.TouRuZhouQi or not self.YueHeShuLiang or not self.YueHeDanJia or not self.UnitPrice or not self.YuGuXiaoLiang or not self.ChengGongLv or not self.LiRunLv:
            return False
        else:
            return True

    def YuChuLi_Int(self, value):
        # 检查是否为 整数，如果不是，则返回False
        if isinstance(value, int):
            return value
        else:
            return False

    def YuChuLi_float(self, value):
        # 检查是否为 整数，如果不是，则返回False
        if isinstance(value, float):
            # 如果小于0，则返回False
            if value <= 0:
                return False
            elif value > 1:
                value = 1
            return value
        else:
            return False

    def malimalihong(self):
        # 根据循环周期，制定一个列表数
        months = range(1, self.TouRuZhouQi)
        # 初始投入
        ChanPinChengBen = self.KaiPinYuSuan * self.KaiPinShuLiang

        # 每月投入
        month_in_zc = self.ZhiChengRenYuan * self.ZhiChengGongZi
        month_in_pr = self.SuoXuPR * self.PRGongZi
        month_in_yuehe = self.SuoXuPR * self.YueHeShuLiang * self.YueHeDanJia
        # 计算每个月的投入
        month_in = month_in_zc + month_in_pr + month_in_yuehe

        # 每月收入
        month_out = self.KaiPinShuLiang * self.ChengGongLv * self.UnitPrice * self.YuGuXiaoLiang * self.LiRunLv * 30 * (
                1 - self.TuiKuanLv)
        month_in_list = []
        month_out_list = []
        month_lists = []
        for month in months:
            month_list = []
            if month == 1:
                in_ = month_in + ChanPinChengBen
            else:
                in_ = month_in
            if month in [1, 2, 3]:
                out_ = 0
            else:
                out_ = month_out
            total_in = month_in_list[-1] if month_in_list else 0
            total_out = month_out_list[-1] if month_out_list else 0
            month_list.append(month)
            month_list.append(in_)
            month_list.append(out_)
            month_list.append(total_in + in_)
            month_list.append(total_out + out_)
            month_in_list.append(total_in + in_)
            month_out_list.append(total_out + out_)
            month_lists.append(month_list)
        # 把month_lists转换为pd格式
        month_lists = pd.DataFrame(month_lists, columns=['月份', '投入', '收入', '累计投入', '累计收入'])
        print(month_lists)
        # 调用图表方法
        self.make_pot(month_lists)

        return month_lists
    def make_pot(self,data):
#         传入数据，制作图表
        # 导入图表库
        # 绘制图表
        plt.plot(data['月份'], data['累计投入'], label='累计投入')
        plt.plot(data['月份'], data['累计收入'], label='累计收入')
        plt.plot(data['月份'], data['收入'], label='收入')
        # 添加图例
        plt.legend()
        # 添加标题
        plt.title('投入与收入')
        # 显示图表
        plt.show()
if __name__ == '__main__':
    # 实例化
    jsc = JiSuanChanChu(2, 2, 3, 12, 80, 200, 30, 200, 0.5, 0.7)
    # 调用
    if jsc.init():
        month_lists = jsc.malimalihong()
