def ChangeTimeFormat12to24(GivenTime: str):
    lstTime = GivenTime.split(" ")
    HourTime = lstTime[0]
    t = HourTime.split(":")
    tFormat = lstTime[1]
    h = int(t[0])
    m = int(t[1])
        
    if(tFormat == "AM" and h == 12):
        h = 0
    elif(tFormat == "PM"):
        h += 12
    
    return [h,m]
    
def ChangeTimeFormat24to12(h,m):
    hString = ""
    mString = str(m)
    fStr = ""
    DayString = ""
    
    if(m < 10) : mString = "0" + str(m)
    hString = str(h)
    
    if h < 12:
        if h == 0: hString = "12"
        fStr = "AM"
    elif h == 12: fStr = "PM"
    elif h > 12 :
        hString = str(h - 12)
        
        fStr = "PM"
    
    return "{0}:{1} {2}".format(hString,mString,fStr)

def add_time(StartTime: str,Duration: str,StartDayOfWeek: str = None):
    weekDays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    leftMinute = 0
    newIndex = 0    
    dayOfWeek = ""
    DayString = ""
   
    hm = ChangeTimeFormat12to24(StartTime)
    h = hm[0]
    m = hm[1]
    
    DurationList = Duration.split(":")
    
    try:
        AddHour = int(DurationList[0])
        AddMinute = int(DurationList[1])
    except:
        print("Value must be digit")
        return
    if(AddMinute > 59) :
        print("Minutes must be less than 59")
        return
    
    leftMinute = m + AddMinute
    if(leftMinute > 59 ):
        leftMinute -= 60
        AddHour += 1
           
    AddDays = 0
    leftHour = AddHour % 24
    if AddHour > 24: AddDays = int((AddHour - leftHour) / 24)
    
    h += leftHour
    mh = h % 24
    if h >= 24: AddDays += int((h - mh) / 24)
        
    if(StartDayOfWeek is not None):
        indexOfDay = weekDays.index(StartDayOfWeek.lower())
        newIndex = (indexOfDay + AddDays) % 7
        
        dayOfWeek = " " + str.capitalize(weekDays[newIndex])        
        DayString = "," + dayOfWeek if dayOfWeek != "" else ""
    
    if (AddDays == 0):
        DayString += ""
    elif(AddDays == 1):
        DayString += " (next day)"
    else:
        DayString += " ({0} Days Later)".format(AddDays)
        
    FinalTime = ChangeTimeFormat24to12(mh,leftMinute)
    
    print(FinalTime + DayString)
    
def time_calculator():
    add_time("3:00 PM", "3:10")
    # Returns: 6:10 PM

    add_time("11:30 AM", "2:32", "Monday")
    # Returns: 2:02 PM, Monday

    add_time("11:43 AM", "00:20")
    # Returns: 12:03 PM

    add_time("10:10 PM", "3:30")
    # Returns: 1:40 AM (next day)

    add_time("11:43 PM", "24:20", "tueSday")
    # Returns: 12:03 AM, Thursday (2 days later)

    add_time("6:30 PM", "205:12")
    # Returns: 7:42 AM (9 days later)
    
time_calculator()
