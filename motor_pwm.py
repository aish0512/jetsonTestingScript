import Jetson.GPIO as GPIO
import time

# Define GPIO pins for motor control
right_motor_a = 35
right_motor_b = 36
right_motor_en = 32
left_motor_a = 37
left_motor_b = 38
left_motor_en = 33             

# Setup GPIO mode
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Setup motor control pins as output
GPIO.setup(right_motor_a, GPIO.OUT)
GPIO.setup(right_motor_b, GPIO.OUT)
GPIO.setup(right_motor_en, GPIO.OUT)
GPIO.setup(left_motor_a, GPIO.OUT)
GPIO.setup(left_motor_b, GPIO.OUT)
GPIO.setup(left_motor_en, GPIO.OUT)

# Initialize PWM variables to None
pwm_r = None
pwm_l = None

try:
    # Initialize PWM on motor enable pins
    pwm_r = GPIO.PWM(right_motor_en, 1000)
    pwm_l = GPIO.PWM(left_motor_en, 1000)
    pwm_r.start(0)
    pwm_l.start(0)
except Exception as e:
    print(f"Error initializing PWM: {e}")

def forward(seconds):
    print("Moving forward")
    GPIO.output(right_motor_a, GPIO.HIGH)
    GPIO.output(right_motor_b, GPIO.LOW)
    GPIO.output(left_motor_a, GPIO.LOW)
    GPIO.output(left_motor_b, GPIO.HIGH)
    if pwm_r and pwm_l:
        pwm_r.ChangeDutyCycle(75)
        pwm_l.ChangeDutyCycle(75)
    time.sleep(seconds)
    if pwm_r and pwm_l:
        pwm_r.ChangeDutyCycle(0)
        pwm_l.ChangeDutyCycle(0)


# Main function to control motors
def main():
    forward(2)


if __name__ == "__main__":
    main()
