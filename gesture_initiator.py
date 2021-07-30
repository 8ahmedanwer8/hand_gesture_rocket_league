import cv2
import mediapipe as mp 
import time 

class hand_detector():
	def __init__(self,mode = False, max_hands = 2, detection_con = 0.5, track_con = 0.5):
		self.mode = mode
		self.max_hands = max_hands
		self.detection_con = detection_con
		self.track_con = track_con

		self.mpHands = mp.solutions.hands
		self.hands = self.mpHands.Hands(self.mode, self.max_hands, self.detection_con, 
			self.track_con)
		self.mpDraw = mp.solutions.drawing_utils

	def img_function(self, img, draw=True):
		imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		self.results = self.hands.process(imgRGB)
		# print(results.multi_hand_landmarks)

		if self.results.multi_hand_landmarks:
			for hand_lms in self.results.multi_hand_landmarks:
				if draw: 
					self.mpDraw.draw_landmarks(img, hand_lms, self.mpHands.HAND_CONNECTIONS)
		return img

	def find_hand(self, img, which_hand = 1, draw = True):
		lm_list = []
		imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		self.results = self.hands.process(imgRGB)

		if self.results.multi_hand_landmarks:
			for hand_landmarks in self.results.multi_hand_landmarks:
				for val, lm in enumerate(hand_landmarks.landmark):
					h, w, c = img.shape
					cx, cy = int(lm.x*w), int(lm.y*h)
					# print(val, cx, cy)

					lm_list.append([val,cx,cy])
		return lm_list




def main():
	timeP = 0 
	timeC = 0 
	cap = cv2.VideoCapture(0)

	detector = hand_detector()

	def left_right(lst):
		if len(lst) == 42:
			lst_0 = []
			lst_1 = []
			lst_0.append(lst[0:21])
			lst_1.append(lst[21:])
			return lst_0, lst_1

	while True:
		success, img = cap.read()
		img = detector.find_hands(img)
		lm_list = detector.find_hand_1(img)

		# if len(lm_list) != 0:
		# 	print(lm_list[1])

		result = left_right(lm_list)

		if result:
			if len(result[0][0]) != 0:
				if len(result[0][0][0]):
					print("hand_one", result[0][0][0])
					print("hand_two", result[1][0][0])
		else:
			if len(lm_list) != 0:
				print("any hand", lm_list[0])

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
 