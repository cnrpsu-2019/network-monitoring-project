class Rose():
	prev_session = ''
	curr_session = ''
	total_user = 0
	
	'''
	แบ่งไว้เป็น 2-3 กรณี หากว่า
		ถ้า prev_session != curr_session:
			ถ้า event == 'Associated':
				total_user++ 
			ถ้า นอกนั้น event == 'Disasociated':
				total_user--
	
		นอกนั้น ถ้า prev_session == curr_session:
			total_user = total_user
	'''