import cv2
import time 
import math
import gesture_initiator as gi
from threading import Thread


from pynput.keyboard import Key, Controller 
keyboard = Controller()
thumb_tip = 4 

thumb_tip = 4 
index_finger_tip = 8
middle_finger_tip = 12 
ring_finger_tip = 16	
pinky_tip = 20

# thumb_cmc = 1
index_finger_dip = 7
middle_finger_dip = 11
ring_finger_dip = 15
pinky_dip = 19

wrist = 0 
index_finger_mcp = 5

class gesture_finder():
	def __init__(self, thumb_tip = 4, index_finger_tip = 8, middle_finger_tip = 12, ring_finger_tip = 16,	
	pinky_tip = 20, index_finger_dip = 7, middle_finger_dip = 11, ring_finger_dip = 15, pinky_dip = 19):
		self.thumb_tip = thumb_tip
		self.index_finger_tip = index_finger_tip
		self.middle_finger_tip = middle_finger_tip
		self.ring_finger_tip= ring_finger_tip

		self.thumb_dip = thumb_tip
		self.index_finger_dip = index_finger_dip
		self.middle_finger_dip = middle_finger_dip
		self.ring_finger_dip= ring_finger_dip

	def find_high_five(self,lm_list):
		sign = "UNDEFINED"
		checkmark_high_five = 0
		if len(lm_list) != 0:
			thumb_to_knuckles = math.hypot(lm_list[thumb_tip][1] - lm_list[index_finger_mcp][1],
				lm_list[thumb_tip][2] - lm_list[index_finger_mcp][2])
			index_to_ring = math.hypot(lm_list[index_finger_tip][1] - lm_list[ring_finger_tip][1],
				lm_list[index_finger_tip][2] - lm_list[ring_finger_tip][2])
			
			if thumb_to_knuckles > index_to_ring:
					checkmark_high_five = checkmark_high_five - 1

			if lm_list[thumb_tip][1] < lm_list[index_finger_tip][1]:
				if lm_list[thumb_tip][2] > lm_list[index_finger_tip][2]:
					checkmark_high_five = checkmark_high_five + 1
			if lm_list[index_finger_tip][1] < lm_list[middle_finger_tip][1]:
				checkmark_high_five = checkmark_high_five + 1
			if lm_list[middle_finger_tip][1] < lm_list[ring_finger_tip][1]:
				checkmark_high_five = checkmark_high_five + 1
			if lm_list[ring_finger_tip][1] < lm_list[pinky_tip][1]:
				checkmark_high_five = checkmark_high_five + 1		
			
		if checkmark_high_five == 4:
			sign = "HIGHFIVE"
			print("HIGHFIVE", checkmark_high_five)
			keyboard.press('w')
			time.sleep(0.1)
			keyboard.release('w')
		else:
			pass

	def find_fist(self,lm_list):
		sign = "UNDEFINED"
		checkmark_fist = 0
		if len(lm_list) != 0:
			if lm_list[index_finger_dip][2] < lm_list[index_finger_tip][2]:
				checkmark_fist = checkmark_fist + 1
			if lm_list[middle_finger_dip][2] < lm_list[middle_finger_tip][2]:
				checkmark_fist = checkmark_fist + 1
			if lm_list[ring_finger_dip][2] < lm_list[ring_finger_tip][2]:
				checkmark_fist = checkmark_fist + 1		
			if lm_list[pinky_dip][2] < lm_list[pinky_tip][2]:
				checkmark_fist = checkmark_fist + 1		

			thumb_to_knuckles = math.hypot(lm_list[thumb_tip][1] - lm_list[index_finger_mcp][1],
				lm_list[thumb_tip][2] - lm_list[index_finger_mcp][2])
			index_to_ring = math.hypot(lm_list[index_finger_tip][1] - lm_list[ring_finger_tip][1],
				lm_list[index_finger_tip][2] - lm_list[ring_finger_tip][2])


			if thumb_to_knuckles > index_to_ring:
					checkmark_fist = checkmark_fist - 1
			
		if checkmark_fist == 4:
			sign = "FIST"
			print("FIST", checkmark_fist)
			keyboard.press('s')
			time.sleep(0.1)
			keyboard.release('s')
		else:
			pass



	def find_left(self, lm_list):
		sign = "UNDEFINED"
		checkmark_left = 0
		if len(lm_list) != 0:
			if lm_list[index_finger_dip][2] < lm_list[index_finger_tip][2]:
				checkmark_left = checkmark_left + 1
			if lm_list[ring_finger_dip][2] < lm_list[ring_finger_tip][2]:
				checkmark_left = checkmark_left + 1

			if lm_list[thumb_tip][1] < lm_list[pinky_tip][1]:
				checkmark_left = checkmark_left + 1	

			thumb_to_knuckles = math.hypot(lm_list[thumb_tip][1] - lm_list[index_finger_mcp][1],
				lm_list[thumb_tip][2] - lm_list[index_finger_mcp][2])
			index_to_ring = math.hypot(lm_list[index_finger_tip][1] - lm_list[ring_finger_tip][1],
				lm_list[index_finger_tip][2] - lm_list[ring_finger_tip][2])

			if thumb_to_knuckles > index_to_ring:
					checkmark_left = checkmark_left + 1
			
		if checkmark_left == 4:
			sign = "LEFT"
			print("LEFT", checkmark_left)
			keyboard.press('a')
			time.sleep(0.5)
			keyboard.release('a')
		else:
			pass

	def find_right(self, lm_list):
		sign = "UNDEFINED"
		checkmark_right = 0
		if len(lm_list) != 0:
			if lm_list[thumb_tip][1] > lm_list[pinky_tip][1]:
				checkmark_right = checkmark_right + 1	

			if lm_list[index_finger_dip][2] < lm_list[index_finger_tip][2]:
				checkmark_right = checkmark_right + 1
			if lm_list[ring_finger_dip][2] < lm_list[ring_finger_tip][2]:
				checkmark_right = checkmark_right + 1

			thumb_to_knuckles = math.hypot(lm_list[thumb_tip][1] - lm_list[index_finger_mcp][1],
				lm_list[thumb_tip][2] - lm_list[index_finger_mcp][2])
			index_to_ring = math.hypot(lm_list[index_finger_tip][1] - lm_list[ring_finger_tip][1],
				lm_list[index_finger_tip][2] - lm_list[ring_finger_tip][2])

			if thumb_to_knuckles > index_to_ring:
					checkmark_right = checkmark_right + 1

		if checkmark_right == 4:
			sign = "RIGHT"
			print("RIGHT", checkmark_right)
			keyboard.press('d')
			time.sleep(0.5)
			keyboard.release('d')
		else:
			pass

def main():
	timeP = 0 
	timeC = 0 
	cap = cv2.VideoCapture(0)


	def lm_each_hand(lst):
		if len(lst) == 42:
			lst_0 = []
			lst_1 = []
			lst_0.append(lst[0:21])
			lst_1.append(lst[21:])
			return lst_0, lst_1
 	

	
	while True:
		success, img = cap.read()
		detector = gi.hand_detector()
		finder = gesture_finder()
		img = detector.img_function(img)


		lm_list = detector.find_hand(img)
		result = lm_each_hand(lm_list)

		# if result:
		# 	if len(result[0][0]) != 0:
		# 		if len(result[0][0][0]):
		# 			print("hand_one", result[0][0][0])
		# 			print("hand_two", result[1][0])
		# else:
		# 	if len(lm_list) != 0:
		# 		print("either hand", lm_list[0])

		try:

			high_five_thread = Thread(target = finder.find_high_five, args = (result[0][0],))
			fist_thread = Thread(target = finder.find_fist, args = (result[0][0],))
			left_thread = Thread(target = finder.find_left, args = (result[1][0],))
			right_thread = Thread(target = finder.find_right, args = (result[1][0],))

			high_five_thread.daemon = True
			fist_thread.daemon = True
			left_thread.daemon = True
			right_thread.daemon = True

			high_five_thread.start()
			fist_thread.start()
			left_thread.start()
			right_thread.start()

		except:
			print("Put both hands up at the camera")

		timeC = time.time()
		fps = 1 / (timeC - timeP)
		timeP = timeC

		cv2.putText(img, str(int(fps)), (15,50), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 2 )

		cv2.imshow("image", img)
		k = cv2.waitKey(30) & 0xff
		if k == 27:
			break

	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main()
