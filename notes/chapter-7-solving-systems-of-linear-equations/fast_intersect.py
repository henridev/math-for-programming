def line_intersection(line1, line2):
    '''
    in: 
    s1 = ((1, 5), (2, 3))
    s2 = ((2, 2), (4, 4))

    out: 
    2.3333333333333335 2.3333333333333335
    '''
    s1_start, s1_end = s1
    s2_start, s2_end = s2
    s1_start_x, s1_start_y = s1_start
    s1_end_x, s1_end_y = s1_end
    s2_start_x, s2_start_y = s2_start
    s2_end_x, s2_end_y = s2_end
    xdiff = (s1_start_x - s1_end_x, s2_start_x - s2_end_x)
    ydiff = (s1_start_y - s1_end_y, s2_start_y - s2_end_y)

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    print(x, y)
    return x, y


s1 = ((1, 5), (2, 3))
s2 = ((2, 2), (4, 4))

line_intersection(s1, s2)
