from datetime import datetime


time_1 = datetime.strptime('00:00:00', '%H:%M:%S')
time_2 = datetime.strptime('23:59:59', '%H:%M:%S')

time_diff = time_2 - time_1

if time_diff.seconds < 60:
    print(int(time_diff.seconds / 60), 'minutes ago.')
elif time_diff.seconds > 3600:
    print(int(time_diff.seconds / 3600), 'hours ago.')



