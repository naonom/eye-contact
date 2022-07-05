from sys import stdin
import math

class GetAngle():
    base_data:list = []
    gaze_angle_data:list = []

    def __init__(self) -> None:
        print("get angle class")

    def get_data(self):
        try:
            line = stdin.readline()
            self.base_data = line.split(',')
        
        except:
            print('tail fail')
            fake = []
            for i in range(497):
                fake.append('0')
            self.base_data = fake

        #print(self.base_data)

    def pick_angle(self):
        try:
            if self.base_data[4] == '1':
                self.gaze_angle_data.clear()
                self.gaze_angle_data.append(float(self.base_data[11]))
                self.gaze_angle_data.append(float(self.base_data[12]))

            else:
                self.gaze_angle_data.clear()
                for i in 6:                  
                    self.gaze_angle_data.append(0.0)
                print('tracking fail')
        except:
            self.gaze_angle_data.clear()
            for i in range(2):                  
                    self.gaze_angle_data.append(0.0)
            print('check data fail')
            return
        print(self.gaze_angle_data)