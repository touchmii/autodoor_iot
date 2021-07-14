

import asyncio
import xlrd

def read_config():
	workbook = xlrd.open_workbook('Auto-Door-config.xlsx')
	sheet = workbook.sheet_by_index(0)
	door_dic = {}
	row = sheet.row_values(0)
	row2 = sheet.row_values(1)
	print(row2)
	row3 = sheet.row_values(2)
	row4 = sheet.row_values(4)
	row5 = list(map(int, row4))
#	row3 = list(map(lambda x: x+'.local' , row3))
	row3 = list(map(lambda x: f'{x}.local' , row3))
	print(row3)
	room_dict = dict(zip(row2, row5))
	print(room_dict)

	for i in range(1,19):
		door_dic[int(row[i])] = []
		door_dic[row[i]].append(row2[i])
		door_dic[row[i]].append(row3[i])
	return door_dic

if __name__ == '__main__':
	print(read_config())