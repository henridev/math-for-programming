def standard_form(v1, v2):
    '''
    Ax + By = C
    '''
    x1, y1 = v1
    x2, y2 = v2
    a = y2 - y1
    b = x1 - x2
    c = x1 * y2 - y1 * x2
    return a, b, c


def slope(v1, v2):
    '''
    Ax + By = C
    '''
    x1, y1 = v1
    x2, y2 = v2
    m = (y2 - y1) / (x2 - x1)
    return m

def standard(v1, v2):
    '''
    Ax + By = C
    '''
    x1, y1 = v1
    x2, y2 = v2
    m = slope(v1, v2)
    b = (m * x1)
    a = m * -1
    c = b * -1
    return m
