str_seconds = input("please type number of seconds:\n")
int_seconds = int(str_seconds)
minutes = int_seconds // 60
seconds = int_seconds % 60
hours = minutes // 60
minutes = minutes % 60
hours = hours % 24
print(f"the time is:  {hours} hours, {minutes} minutes and {seconds} seconds long ")
minutes = input("please type number of minutes:\n")
int_minutes = int(minutes)
minutes = int_minutes // 60
hours = int_minutes % 60
print(f"the time is: = {hours} hours and {minutes} minutes long ")
seconds = int(input("please type number for seconds:\n"))
hours = seconds // 3600
minutes = (seconds % 3600)//60
remaining_seconds = seconds % 60
print(f"the time is: {hours} hours, {minutes} minutes and {remaining_seconds} seconds long")
 