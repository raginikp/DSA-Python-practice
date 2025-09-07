def unique_in_order(sequence):
    res=[]
    for item in sequence:
        if item not in res or item != res[-1]:
            res.append(item)
    return res