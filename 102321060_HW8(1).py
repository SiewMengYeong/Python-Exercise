from math import pi, sin, cos

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0, time)
    
    while cball.getY()>= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))
    
    if time > (vel * sin(pi * angle / 180.0))/9.8:
        print("Maximun height: {0:0.1f} meters.".format(cball.getMaxHeight1()))
    else:
        print("Maximun height: {0:0.1f} meters.".format(cball.getMaxHeight2()))

def getInputs():
    angle = eval(input("Enter the launch angle (in degrees): "))
    vel = eval(input("Enter the initial velocity (in meters/sec): "))
    h0 = eval(input("Enter the initial height (in meters): "))
    time = eval(input("Enter the time interval between position calculations: "))
    return angle, vel, h0, time

class Projectile: 
    def __init__(self, angle, velocity, height, time):
        self.xpos = 0.0
        self.ypos = height
        theta = pi * angle / 180.0
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        self.maxHeight1 = ((velocity **2 * (sin (theta))**2)/(2*9.8)) + height
        self.maxHeight2 = self.xvel * time

    def getY(self):
        return self.ypos

    def getX(self):
        return self.xpos

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1
        
    def getMaxHeight1(self):
        return self.maxHeight1

    def getMaxHeight2(self):
        return self.maxHeight2

main()
