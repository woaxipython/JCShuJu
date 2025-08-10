class JiSuanChanChu(object):
    def __init__(self, ZhiChengRenYuan, KaiPinShuLiang,  SuoXuPR, TouRuZhouQi,
                 YueHeShuLiang, YueHeDanJia, UnitPrice, YuGuXiaoLiang,ChengGongLv, LiRunLv):
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

        self.ZhiChengGongZi = 11000
        self.KaiPinYuSuan = 5000
        self.PRGongZi = 7000
        self.TuiKuanLv = 0.2

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
            elif value >1 :
                value = 1
            return value
        else:
            return False