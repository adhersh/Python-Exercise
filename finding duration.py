hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins= mins+dura
hour= hour + mins//60
mins = mins % 60

print("the time of ending is",hour,mins,sep=":")