<div align="center">

# 通辽转换器！

</div>

## 什么是 "通辽"
>”通辽“是 UP 主小约翰可汗来介绍国家使用的单位。因小约翰可汗过于出名变成了一个梗<br>

[\[点击观看视频\]](./tongliao.mp4)<br>
”通辽“简写 T, 为 59535 平方千米, 或者是 285.31 万人。<br>

## Usage

这里实现了一个通辽转换模块: 

``` python
from tongliao import country2tongliao
import pprint
pprint.pprint(country2tongliao("中国"))
```

``` python
{'area': 9600012,
 'area_str': '9600012 平方千米(km²)',
 'name': '中国',
 'result': {'area': 161.25,
         'area_str': '161.25 通辽(T)',
         'people': 507.27,
         'people_str': '507.27 通辽(T)'},
 'people': 1447301400,
 'people_str': '1447301400 人'}
```

``` python
__all__ = [
    "TONGLIAO_AREA",    # 通辽面积，单位平方千米
    "TONGLIAO_CHINESE", # 通辽单位中文 "通辽"
    "TONGLIAO_ENGLISH", # 通辽单位英文 "T"
    "TONGLIAO_PEOPLE",  # 通辽人口
    "area2tongliao",    # 输入平方千米数，转换为通辽
    "country2tongliao", # 输入国家名，转换为通辽
    "people2tongliao",  # 输入人口数量，转换为通辽
]
```

同时还做了一个简陋的通辽转换 GUI

``` bash
python3 tongliao.py
```

![](/tongliao_calc.jpg)

## 注意事项

1. 运行模块时会在当前目录下写入各个国家的信息的 `json` 文件
2. **"通辽" 绝对不只是人口单位、面积单位！** [如果有好像发的话发个 issues 吧!][issues-new]
3. **给个赞吧！**

## 脚注

世界各国国土数据来源: <https://www.kylc.com/stats/global/yearly_overview/g_area_surface.html>

世界各国人口数据来源: <https://mip.phb123.com/city/renkou/rk.html>

- 国土数据共记录 214 个地区
- 人口数据共记录 233 个地区
- **最后有 197 个地区在两项数据中均有记录，其他一并过滤**
- 197 个地区中 **没有科索沃** ！~~科索沃永远是塞尔维亚的一部分~~
- **国土数据中美国国土为 983 万平方千米，算上了领海面积。目前普遍为 937 万平方千米，已修正。**
- **收集的各国国土与人口数据难免会有遗漏，如有发现可以提出**


[issues-new]: https://github.com/nemo2011/tongliao/issues/new
