import re
count = 0
fo =  open("config.txt","r")
system = fo.readlines()
data = list(system)
#print data
#data = "D/aaa_state_camera_preview"
for val in data:
        if re.search(r"Displayed com.google.android.deskclock",val):
                print val
                count += 1

print count

