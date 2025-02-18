import datetime

# Get the current time and date
current_time = datetime.datetime.now()

# Append the time and date to an existing file
with open('output.log', 'a') as f:
    f.write('Chaos experiment run at ' + str(current_time) + '\n')
