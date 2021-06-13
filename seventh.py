'''
You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
How long will the bus journey take? Alternatively, you could run to university. You jog the first mile at 7mph;
then run the next two at15mph; before jogging the last at 7mph again.
Will this be quicker or slower than the bus?
'''
distance = 4
speed = 25
time_taken = (distance // speed) + 60
#bus spends 2 mins at each stop
time_spent = 20
total_time_by_bus = time_spent + time_taken
print(f"the time taken by bus is {total_time_by_bus}")
jog_first_mile = (1/7) + 60
jog_second_mile = (2/15) + 60
jog_last_mile = (1/7) + 60
total_walk_time = jog_first_mile + jog_second_mile + jog_last_mile
print(f"the total time taken by walk is {total_walk_time}")
if total_walk_time > total_time_by_bus:
    print("walk is quicker")
else:
    print("walk is slower")