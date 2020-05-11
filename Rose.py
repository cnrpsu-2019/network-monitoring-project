#import modules
import Extract
import createFiles
import time
import ExportToDB
'''
เอาล่ะ มาเริ่มกันใหม่ เนื่องจาก session id มันค่อนค่างแตกต่างนะ
เอา mac addr สองตัว มาเทียบกัน
ถ้าเหมือนกัน : ยอดเท่าเดิม
ไม่เหมือนกัน : ดูสถานะ
	assocaited : total_user++
	disassocicate : total_user--
จากนั้น : ยัดลง database
เคลียร์สถานะ

ดีเลย์อีก 5 นาที ค่อยนับใหม่
Associate Disassociate
'''
def harvest_user():
	status = Extract.extractSpecific(createFiles)
	prev_mac = Extract.client_mac(createFiles.realFile)[-1]
	time.sleep(10) #sleep for 10 secs
	curr_mac = Extract.client_mac(createFiles.realFile)[-1]
	total_user = 0

	while True:
		try:
			if curr_mac == prev_mac:
				time.sleep(5) #snooze for 5 secs
			elif curr_mac != prev_mac:
				if status is Associate:
					total_user = total_user + 1
				elif status is Disassociate:
					total_user = total_user - 1

			ExportToDB.harvest_user(total_user)
			time.sleep(300) #delayed for 5 mins
			total_user = 0
		except e:
			print(e)
