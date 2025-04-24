def Percent_Calc(data):
    total = sum(data)
    result = {}
    for X in data:
    result[X] = (X / total) * 100
	return result
