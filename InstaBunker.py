import sys, time, random
print("")
print("")
print("ㄒ几ㄚㄒ匚ㄖᗪ乇尺")
print("")
print("INSTABURST✓")
print("")
InstaUid = input("Enter Username --- @ ")
def progressBar(count_value, total, suffix=''):

    bar_length = 100

    filled_up_Length = int(round(bar_length* count_value / float(total)))

    percentage = round(100.0 * count_value/float(total),1)

    bar = '=' * filled_up_Length + '-' * (bar_length - filled_up_Length)

    sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percentage, '%', suffix))

    sys.stdout.flush()

for i in range(11):

    time.sleep(random.random())

    progressBar(i,10)
    
print("@" + InstaUid + "    Patched Successfully !!")
print("")
print("")
print("@TnYtCoder Github !!")
print("")
