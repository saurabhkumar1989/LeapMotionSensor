import os, sys, inspect, thread, time
sys.path.append("C:/Users/Ramanuja/Documents/python/leap/LeapSDK/lib")
sys.path.append("C:/Users/Ramanuja/Documents/python/leap/LeapSDK/lib/x86")
sys.path.append("C:/Users/Ramanuja/Documents/python/leap/LeapSDK/lib/Leap.py")

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

def main():
	class SampleListener(Leap.Listener):
		
		# when sensor connected -  invoke when sensor connected 
		def on_connect(self, controller):
			print "Connected"
			controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)


		def on_frame(self, controller):
			#count = count + 1
			frame = controller.frame()
			hand = frame.hands.rightmost
			rotation_y = hand.palm_position
			for hand in frame.hands:
				handType = "left hand" if hand.is_left else "right hand"
				print handType + "palm position : " + str(hand.palm_position)
				print " "
				normal = hand.palm_normal
				direction = hand.direction
				print "Pitch : " + str(direction.pitch*Leap.RAD_TO_DEG) + "   Roll : "+str(normal.roll*Leap.RAD_TO_DEG)+ str(direction.yaw*Leap.RAD_TO_DEG)
#			print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))
#			print "grab strength hand x: %d, palm position: %d, hands: %d,rotation: %d, tools: %d, gestures: %d" % (hand.grab_strength, hand.palm_position, len(frame.hands), rotation_y, len(frame.tools), len(frame.gestures()))

	listener = SampleListener()
	controller = Leap.Controller()

	# Have the sample listener receive events from the controller
	controller.add_listener(listener)

	# Keep this process running until Enter is pressed
	
	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
if __name__ == "__main__":
	main()