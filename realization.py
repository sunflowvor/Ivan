#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyecharts import Geo


data = [
    ("海门", 49),("招远", 12),("舟山", 112),("齐齐哈尔", 14),
    ("赤峰", 16),("青岛", 218),("乳山", 18),("金昌", 19),("泉州", 121),("莱西", 21),
    ("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 125),
    ("文登", 25),("攀枝花", 25),("威海", 25),("承德", 25),("厦门", 226),
    ("汕尾", 26),("潮州", 26),("丹东", 27),("太仓", 27),("烟台", 28),
    ("福州", 129),("瓦房店", 30),("即墨", 30),("抚顺", 31),("玉溪", 31),("张家口", 31),
    ("阳泉", 31),("莱州", 32),("湖州", 32),("汕头", 132),("昆山", 33),("宁波", 33),
    ("湛江", 33),("揭阳", 34),("荣成", 34),("常熟", 36),("葫芦岛", 35),("上海", 555),
    ("东莞", 136),("河源", 36),("淮安", 36),("泰州", 36),("南宁", 37),("营口", 37),
    ("惠州", 37),("江阴", 37),("蓬莱", 37),("韶关", 38),("嘉峪关", 38),("广州", 338),
    ("延安", 38),("太原", 239),("清远", 39),("中山", 239),("昆明", 139),("寿光", 40),
    ("盘锦", 40),("长治", 41),("深圳", 241),("珠海", 142),("宿迁", 43),("咸阳", 343),
    ("铜川", 44),("平度", 44),("佛山", 144),("海口", 44),("江门", 45),("章丘", 45),
    ("肇庆", 46),("大连", 147),("临汾", 47),("吴江", 47),("石嘴山", 49),("沈阳", 286),
    ("苏州", 250),("茂名", 50),("嘉兴", 51),("长春", 378),("胶州", 52),("银川", 52),
    ("张家港", 52),("三门峡", 53),("锦州", 54),("南昌", 254),("柳州", 54),("三亚", 54),
    ("自贡", 56),("吉林", 456),("阳江", 57),("泸州", 57),("西宁", 57),("宜宾", 58),
    ("呼和浩特", 58),("成都", 458),("大同", 58),("镇江", 59),("桂林", 59),("张家界", 59),
    ("宜兴", 59),("北海", 60),("西安", 361),("金坛", 62),("东营", 62),("牡丹江", 63),
    ("遵义", 63),("绍兴", 263),("扬州", 64),("常州", 64),("潍坊", 65),("重庆", 466),
    ("台州", 67),("南京", 375),("滨州", 70),("贵阳", 71),("无锡", 71),("本溪", 71),
    ("克拉玛依", 72),("渭南", 72),("马鞍山", 72),("宝鸡", 72),("焦作", 75),("句容", 75)
    ,("徐州", 79),("衡水", 80),("包头", 80),("绵阳", 80),("乌鲁木齐", 84),
    ("枣庄", 84),("杭州", 359),("淄博", 85),("鞍山", 86),("溧阳", 86),("库尔勒", 86),
    ("安阳", 90),("开封", 190),("济南", 292),("德阳", 93),("温州", 195),("九江", 296),
    ("邯郸", 98),("临安", 99),("连云港", 35),("兰州", 99),("沧州", 100),("临沂", 103),("南充", 104),
    ("天津", 478),("富阳", 106),("泰安", 112),("诸暨", 112),("郑州", 113),("哈尔滨", 114),
    ("聊城", 116),("芜湖", 47),("唐山", 319),("日照", 21),
    ("平顶山", 119),("胶南", 22),("邢台", 119),("曲靖", 27),("德州", 120),
    ("济宁", 120),("荆州", 127),("宜昌", 130),("义乌", 132),("丽水", 63),("洛阳", 134),
    ("秦皇岛", 336),("株洲", 143),("石家庄", 488),("莱芜", 148),("常德", 152),("保定", 153),
    ("湘潭", 154),("金华", 357),("岳阳", 169),("长沙", 375),("鄂尔多斯", 12),("衢州", 177),("廊坊", 493),
    ("菏泽", 194),("合肥", 200),("盐城", 15),("武汉", 273),("大庆", 279),("北京", 734)
  ]

geo = Geo("空间分布可视化系统", "科研人才", title_color="#fff",
          title_pos="center", width=1024,
          height=684, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value,is_visualmap=True, visual_range=[0, 500],
        visual_text_color='#fff')

geo.render('Visualization System.html')
