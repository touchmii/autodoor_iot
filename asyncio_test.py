# coding: utf-8
#usr/bin/python3

import aiohttp
import asyncio
import time
import json

door_dic2 = {2: ['中间站(批料)', 'Auto-Door-10732899'], 3: ['中间站(胶囊)', 'Auto-Door-10733225'], 4: ['胶囊3', 'Auto-Door-10734019'], 5: ['压片2', 'Auto-Door-10732467'], 6: ['批料第1扇门', 'Auto-Door-10734827'], 7: ['制粒', 'Auto-Door-10733482'], 8: ['容器清洗', 'Auto-Door-10734728'], 9: ['批料第2扇门', 'Auto-Door-10732445'], 10: ['容器存放', 'Auto-Door-10735290'], 11: ['批混', 'Auto-Door-10734132'], 12: ['包衣第1扇门', 'Auto-Door-10735438'], 13: ['包衣第2扇门', 'Auto-Door-10734196'], 14: ['胶囊1', 'Auto-Door-10733094'], 15: ['胶囊2', 'Auto-Door-10734974'], 16: ['压片1', 'Auto-Door-10733177'], 17: ['铝塑1', 'Auto-Door-10732753'], 18: ['铝塑2', 'Auto-Door-10734635'], 19: ['铝塑3', 'Auto-Door-10732064']}
door_dic = {245: ['中间站(批料)', 'Auto-Door-10732899.local'], 260: ['中间站(胶囊)', 'Auto-Door-10733225.local'], 741: ['胶囊3', 'Auto-Door-10734019.local'], 801: ['压片2', 'Auto-Door-10732467.local'], 621: ['批料第1扇门', 'Auto-Door-10734827.local'], 601: ['制粒', 'Auto-Door-10733482.local'], 565: ['容器清洗', 'Auto-Door-10734728.local'], 623: ['批料第2扇门', 'Auto-Door-10732445.local'], 581: ['容器存放', 'Auto-Door-10735290.local'], 876: ['批混', 'Auto-Door-10734132.local'], 841: ['包衣第1扇门', 'Auto-Door-10735438.local'], 845: ['包衣第2扇门', 'Auto-Door-10734196.local'], 781: ['胶囊1', 'Auto-Door-10733094.local'], 747: ['胶囊2', 'Auto-Door-10734974.local'], 821: ['压片1', 'Auto-Door-10733177.local'], 726: ['铝塑1', 'Auto-Door-10732753.local'], 681: ['铝塑2', 'Auto-Door-10734635.local'], 661: ['铝塑3', 'Auto-Door-10732064.local']}
door_id_list = ['Auto-Door-10732899', 'Auto-Door-10733225', 'Auto-Door-10734019', 'Auto-Door-10732467', 'Auto-Door-10734827', 'Auto-Door-10733482', 'Auto-Door-10734728', 'Auto-Door-10732445', 'Auto-Door-10735290', 'Auto-Door-10734132', 'Auto-Door-10735438', 'Auto-Door-10734196', 'Auto-Door-10733094', 'Auto-Door-10734974', 'Auto-Door-10733177', 'Auto-Door-10732753', 'Auto-Door-10734635', 'Auto-Door-10732064', 'Auto-Door-10730242']

default_auth = aiohttp.BasicAuth('login', password='Passw0rd')

async def fetch(session, url, dic_id=None):
	try:
		async with session.get(url) as response:
			return await response.text()
	except OSError:
		print('port not open %r' % door_dic[dic_id])
		return -2, 
	except asyncio.TimeoutError:
		print('canot connected to %r' % door_dic[dic_id])
		return -1

async def door_action(door_id , action='status', auth=default_auth, dic_id=None):
	idd = door_dic[door_id][1]
	url = 'http://{}/door.lua?action={}'.format(idd, action)
	timeout = aiohttp.ClientTimeout(total=3)
	async with aiohttp.ClientSession(auth=auth, timeout=timeout) as session:
		html = await fetch(session, url, door_id)
		if isinstance(html, str):
			rec = json.loads(html)
#			rec = html
			print(door_id)
#			print(type(rec))
			print(rec)
			return rec
		else:
			return html
	
def task_config():
	task = []
	for i in range(2,19):
		task.append('asyncio.Task(door_action({}))'.format(door_dic[i][1]))
	return task

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
#	loop.run_until_complete(door_action())
	
#	tasks = task_config()
#	tasks = [asyncio.Task(door_action(door_id)) for door_id in door_id_list]
#	tasks2 = [asyncio.Task(door_action(door_id, 'open')) for door_id in door_id_list]
#	tasks3 = [asyncio.Task(door_action(door_id, 'close')) for door_id in door_id_list]
#	tasks3 = [asyncio.Task(door_action(door_id, 'status')) for door_id in door_id_list]
#	tasks3 = [asyncio.Task(door_action(door_id, 'open')) for door_id in door_dic]
	tasks3 = [asyncio.Task(door_action(door_id, 'status')) for door_id in door_dic]
#	tasks3 = [asyncio.Task(door_action(door_id, 'reboot')) for door_id in door_dic]
#	tasks3 = [asyncio.Task(door_action(door_id, 'uptime')) for door_id in door_dic]
	
#	print(tasks)
#	loop.run_until_complete(asyncio.wait(tasks))
#	loop.run_until_complete(asyncio.wait(tasks2))
	loop.run_until_complete(asyncio.wait(tasks3))