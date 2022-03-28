class clockTime:
    
    def __init__(self, hours, minutes, seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    #Set hours
    def setHours(self, hours):
        self.hours = hours

    #Set minutes
    def setMinutes(self, minutes):
        self.minutes = minutes
    
    #Set seconds
    def setSeconds(self, seconds):
        self.seconds = seconds
    
    #show time
    def showTime(self):
        print("The time is: {}:{}:{}".format(self.hours,self.minutes,self.seconds))

#User input
hour = input("Please enter hour:")
minute = input("Please enter minute:")
second = input("Please enter second: ")

#create a variable to pass in the parameters needed in the class clockTime
time = clockTime(hour, minute, second)

#Print the time 
time.showTime()
