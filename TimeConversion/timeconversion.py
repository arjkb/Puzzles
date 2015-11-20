# Program to convert time given in AM/PM format to 24-hour format

# AUTHOR	: Arjun Krishna Babu
# DATE		: Wed Nov 18 14:21:26 IST 2015
# OS		: openSUSE Leap 42.1

def convertTime(currentTime, m)	:
	getAM = {"12":"00", "01":"01", "02":"02", "03":"03", 
				"04": "04", "05":"05", "06":"06", "07":"07", 
				"08":"08", "09":"09", "10":"10", "11":"11"  }
				
	getPM = {"12":"12", "01":"13", "02":"14", "03":"15",
				"04": "16", "05":"17", "06":"18", "07":"19",
				"08":"20", "09":"21", "10":"22", "11":"23"  }
	   	
	if m == "AM" :
		currentTime[0] = getAM[currentTime[0]]
	elif m == "PM" :
		currentTime[0] = getPM[currentTime[0]]
	
	return currentTime
	
timestring = input()
timepure = timestring[:-2]
meridian = timestring[-2:]
timeactual = ""

giventime = timepure.split(":")

timeactual = convertTime(giventime, meridian)

print(':'.join(timeactual))
