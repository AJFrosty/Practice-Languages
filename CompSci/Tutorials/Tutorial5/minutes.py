mins = int(input("Please enter the numbe of minutes: "))

years = mins // 525600

mins = mins - (years*525600)

days = mins//1440
remain = mins - (days*1440)

print ("The time left until we get to", mins, "minutes from now are", years,"years, ", days,"days and", remain, "minutes")
