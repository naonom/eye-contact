import time
import get_angle

def main():
    eye_angle:get_angle.GetAngle
    eye_angle = get_angle.GetAngle()

    print("success")
    while True:
        eye_angle.get_data()
        eye_angle.pick_angle()
        if abs(float(eye_angle.gaze_angle_data[0])) <= 0.18 and abs(float(eye_angle.gaze_angle_data[1])) <= 0.18:
            print("contact!")
        time.sleep(1)

if __name__ == "__main__":
    main()