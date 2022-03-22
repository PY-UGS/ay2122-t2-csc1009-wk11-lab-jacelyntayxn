class clockTime:
    
    def __init__(self, hours, minutes, seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def setHours(self, hours):
        self.hours = hours

    def setMinutes(self, minutes):
        self.minutes = minutes
    
    def setSeconds(self, seconds):
        self.seconds = seconds
    
    def showTime(self):
        print("The time is: {}:{}:{}".format(self.hours,self.minutes,self.seconds))

#User input
hour = input("Please enter hour:")
minute = input("Please enter minute:")
second = input("Please enter second: ")

time = clockTime(hour, minute, second)
time.showTime()