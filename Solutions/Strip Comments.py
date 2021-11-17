def solution(string, markers):
    lines = string.split("\n")
    res = []
    for line in lines:
        st = ''
        for i in line:
            if i in markers:
                break
            st += i
        res.append(st.rstrip())
    return "\n".join(res)
