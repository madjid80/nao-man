#navstates.py
GOTO_FORWARD_SPEED = 7
GOTO_BACKWARD_SPEED = -4
GOTO_STRAFE_SPEED = 6
GOTO_SPIN_SPEED = 20
GOTO_STRAIGHT_SPIN_SPEED = 20
GOTO_SPIN_STRAFE = 0
GOTO_SURE_THRESH = 3

WALK_TO_MAX_X_SPEED = 7.0
WALK_TO_MIN_X_SPEED = -4
WALK_TO_MAX_SPIN_SPEED = 10.0
WALK_TO_MIN_SPIN_SPEED = -WALK_TO_MAX_SPIN_SPEED

OMNI_GOTO_FORWARD_SPEED = 5
OMNI_GOTO_STRAFE_SPEED = 4
GOTO_FORWARD_GAIN = 0.05
GOTO_STRAFE_GAIN = 0.5
GOTO_SPIN_GAIN = 0.8
OMNI_GOTO_X_GAIN = .2
OMNI_GOTO_Y_GAIN = .4

OMNI_MAX_X_SPEED = 5.0
OMNI_MIN_X_SPEED = -OMNI_MAX_X_SPEED
OMNI_MAX_Y_SPEED = 5.0
OMNI_MIN_Y_SPEED = -OMNI_MAX_Y_SPEED
OMNI_MAX_SPIN_SPEED = 20.0
OMNI_MIN_SPIN_SPEED = -OMNI_MAX_SPIN_SPEED

OMNI_MIN_X_MAGNITUDE = 1.5
OMNI_MIN_Y_MAGNITUDE = 1.5
OMNI_MIN_SPIN_MAGNITUDE = 4

CHANGE_SPIN_DIR_THRESH = 6

# orbitPoint values
ORBIT_SPIN_SPEED = -20
ORBIT_STRAFE_SPEED = 8

ORBIT_LEFT = -1
ORBIT_RIGHT = 1
ORBIT_SMALL_ANGLE = 35
ORBIT_SMALL_GAIN = .5
ORBIT_MID_GAIN = 1
ORBIT_LARGE_ANGLE = 90
ORBIT_LARGE_GAIN = 1
MIN_ORBIT_ANGLE = 10

#navigator.py
LOC_IS_ACTIVE_H  = 720
CLOSE_ENOUGH_XY = 25.0
CLOSER_XY = 8.0
CLOSE_ENOUGH_H = 10.0
ALMOST_CLOSE_ENOUGH_H = 30.0

AT_HEADING_GOTO_DEG = 20

HEADING_NEAR_THRESH = 10.
HEADING_MEDIUM_THRESH = 30.

HEADING_NEAR_SCALE = 0.3
HEADING_MEDIUM_SCALE = 0.6
HEADING_FAR_SCALE = 1.0
SPIN_EPSILON = 2.0
FORWARD_EPSILON = 0.3
STRAFE_EPSILON = 0.5

POSITION_NEAR_THRESH = CLOSER_XY
POSITION_MEDIUM_THRESH = CLOSE_ENOUGH_XY
POSITION_NEAR_SCALE = 0
POSITION_MEDIUM_SCALE = 0.6
POSITION_FAR_SCALE = 1.0

FRAME_RATE = 20                 # Rough estimate. fps

MIN_SPIN_SPEED = 3.0
