
def groupBy(lst, nmr):
    new_list = []
    row = []
    for i, el in enumerate(lst):
        if i % nmr == 0 and i != 0:
            new_list.append(row)
            row = []
        row.append(el)
    return new_list


lst = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
]

def average_of_tuple_lists(lst):
    '''
    in : [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
    ]
    out : (4.0, 5.0, 6.0)
    '''
    return tuple(int(sum(lst)/len(lst)) for lst in zip(*lst))
