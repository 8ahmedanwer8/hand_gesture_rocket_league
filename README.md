# hand_gesture_rocket_league
I used the MediaPipe library by Google which uses machine learning to provide a variety of face and body tracking methods. Using their hand gesture library, and OpenCV, you can track the location of 21 points (hand landmarks) drawn on the hand which I then used to recognize what hand gesture was being displayed. Then, I used the pynput library to simulate keyboard presses while I had Rocket League open. The keyboard keys pressed are W, A, S, D allowing for basic ground movement.

You make a high five gesture with one hand and fist with the same hand to move forward and backward respectively. On the other hand (pun intended), a fist with thumb to the right or left moves the car right or left, and a fist keeps it straight. Surprisingly, the hardest part was extracting the hand landmarks for both hands and having them not switch. Unfortunately, the code chooses any hand for front and back movement and the other hand for lateral movement, so if you take your hands off, it takes some fiddling to re-adjust.

This code is far from perfect and I hope I can find ways to optimize it later. When I ran the program, not only were the OpenCV FPS dropping but Rocket League was also slowing down along with my computer. Having the program on longer made it slower and slower. Of course with the code itself, there is the  inaccuracy with the gesture detecting as well. The biggest trouble is not being able to test the program properly when it slows down the game.

The gesture_initiator file deals with MediaPipe and OpenCV detection of the hands on the screen, and the other file loosely classifies these hands into pre-defined gestures and sends the keyboard presses. 

Lastly, I used threads where each thread was responsible for one or more keyboard press. I chose this for two reasons. One is that it may help with higher FPS for OpenCV and faster key response time (I don't think it did...). Two is that in a video game, you will be pressing more than one button at a time at some point; so using threads is one way to allow different key presses performed simultaneously. 

