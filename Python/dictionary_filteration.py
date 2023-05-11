def filter_dictionary(d):
    for i in d:
        d[i] = d[i].lower()
        d[i] = (d[i].split())[0]
    return d
d1 = {1:' oNe',2:'tWo ',3:' tHrEE  ',4:'foUr ',5:' fIVe '}
print(filter_dictionary(d1))