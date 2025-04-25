def Percent_Calc(data):
	total = sum(data)
	result = {}
	result_unformatted={}
	result_lastkey=[]
	result_unfinished={}
	for X in data:
    		result_formatted[X] = (X / total) * 100
	result_lastkey=list(result_unformatted.key())[-1]
	for number,label in result_unformatted.items():
		result_unfinished[number]='{:.2f}'.format(label)
	for number,label in result_unfinished.items():
		result[label]='{:,}'.format(number)
	value={value:key for key,value in result_unfinished.items()}
	del result[result_lastkey]
	return result
