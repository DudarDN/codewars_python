def mix(s1, s2):
    dict_res = {}
    for i in s1:
        if i.islower():
            dict_res[i] = s1.count(i)
    for j in s2:
        if j.islower() and s2.count(j) > dict_res.get(j, 0):
            dict_res[j] = s2.count(j)
    dict_res = {key: val for key, val in dict_res.items() if val > 1}
    for _ in dict_res:
        if s1.count(_) > s2.count(_):
            dict_res[_] = (dict_res[_], "1")
        elif s1.count(_) < s2.count(_):
            dict_res[_] = (dict_res[_], "2")
        else:
            dict_res[_] = (dict_res[_], "=")
    list_ = []
    for key, val in dict_res.items():
        str_ = ""
        str_ += val[1] + ":" + key * val[0]
        list_.append(str_)
    list_.sort()
    list_.sort(key=len, reverse=True)
    str_res = "/".join(list_)
    return str_res
