TONGLIAO_CHINESE = "通辽"
TONGLIAO_ENGLISH = "T"
TONGLIAO_AREA = 59535 # 单位：平方千米
TONGLIAO_PEOPLE = 2853100 # 单位：人

def people2tongliao(people):
    return people / TONGLIAO_PEOPLE

def area2tongliao(area):
    return area / TONGLIAO_AREA
