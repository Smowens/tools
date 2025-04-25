def Percent_Calc(data):
	total = sum(data)
	result = {}
	result_unformatted={}
	result_lastkey=[]
	result_unfinished={}
	for X in data:
		result_unformatted[X] = (X / total) * 100
	for number,label in result_unformatted.items():
		result_unfinished[number]='{:.2f}'.format(label)
	for number,label in result_unfinished.items():
		result[label]='{:,}'.format(number)
	result={value:key for key,value in result.items()}
	result_lastkey=list(result.keys())[-1]
	del result[result_lastkey]
	return result
