# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.

target_sec = 2503

rähntiere = {}



with open("input14.txt") as f:
    for line in f.readlines():
        info = line.strip().split()
        rähntier = info[0]
        kmps = int(info[3])
        time = int(info[6])
        sleep = int(info[13])


        # vollständige Intervalle die Rähntier schafft 
        interval = time+sleep
        full_cycle = target_sec // interval
        distance_full_cycle = full_cycle*kmps*time

        # unvollständiges intervall
        remaining_sec = target_sec % interval

        remaining_distance = kmps* min(time, remaining_sec)

        rähntiere[rähntier] = distance_full_cycle + remaining_distance


print(rähntiere)
print(max(rähntiere))

 