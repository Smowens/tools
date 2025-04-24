Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
def Percent_Calc(data):
    total = sum(data)
    result = {}
    for X in data:
    result[X] = (X / total) * 100
	return result
