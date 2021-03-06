# hand_gesture_rocket_league
demo: https://www.youtube.com/watch?v=EEld33B7Jdc

I used the MediaPipe library by Google which uses machine learning to provide a variety of face and body tracking methods. Using their hand gesture library, and OpenCV, you can track the location of 21 points (hand landmarks) drawn on the hand which I then used to recognize what hand gesture was being displayed. Then, I used the pynput library to simulate keyboard presses while I had Rocket League open. The keyboard keys pressed are W, A, S, D allowing for basic ground movement.

## How it roughly works
You make a high five gesture with one hand and fist with the same hand to move forward and backward respectively. On the other hand (pun intended), a fist with thumb to the right or left moves the car right or left, and a fist keeps it straight. Surprisingly, the hardest part was extracting the hand landmarks for both hands and having them not switch. Unfortunately, the code chooses any hand for front and back movement and the other hand for lateral movement, so if you take your hands off, it takes some fiddling to re-adjust.

## Areas of improvements
This code is far from perfect and I hope I can find ways to optimize it later. When I ran the program, not only were the OpenCV FPS dropping but Rocket League was also slowing down along with my computer. Having the program on longer made it slower and slower. Of course with the code itself, there is the inaccuracy with the gesture detecting as well. The biggest trouble is not being able to test the program properly when it begins to hog your RAM 50 seconds in

## Files
The gesture_initiator.py is the module I wrote for initializing and abstracting MediaPipe and OpenCV methods which return location of landmarks from both hands. gesture_calculator_and_actuator.py classifies these hands into pre-defined gestures by calculating the position of landmarks and algorithmically checking if they classify as the pre-defined gestures. Finally, the recognized gestures send keyboard presses using threads. 

I used threads where each thread was responsible for one or more keyboard press. I chose this for two reasons. One is that it may help with higher FPS for OpenCV and faster key response time (I don't think it did...). Two is that in a video game, you will be pressing more than one button at a time at some point; so using threads is one way to allow different key presses performed simultaneously. That being said, threads actually for some reason made my gesture detecting more inaccurate.

# the future?
Maybe turning the entire game of rocket league (or other games) fully controllable with body gestures. This would be a fun and whacky thing to try and definitely calorie-burning and pointless.
