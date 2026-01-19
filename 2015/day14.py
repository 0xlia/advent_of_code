from pprint import pprint


# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# fill reindeer dict
rähntiere = []
with open("input14.txt") as f:

    for line in f.readlines():
        info = line.strip().split()

        rähntier = {
            "name": info[0],
            "kmps": int(info[3]),
            "time": int(info[6]),
            "sleep": int(info[13]),
            "current_km": 0,
            "points": 0,
        }
        rähntiere.append(rähntier)

target_sec = 2503

for current_sec in range(1,target_sec + 1):
    current_winner = 0
    for rähntier in rähntiere:
        time = rähntier["time"]
        kmps = rähntier["kmps"]
        # vollständige Intervalle die Rähntier schafft
        interval = time + rähntier["sleep"]
        rähntier["current_km"] = (current_sec // interval) * kmps * time
        # unvollständiges intervall
        remaining_sec = current_sec % interval
        rähntier["current_km"] += kmps * min(time, remaining_sec)
        # winner?
        if rähntier["current_km"] > current_winner:
            current_winner = rähntier["current_km"]
        

    for rähntier in rähntiere:
        if rähntier["current_km"] == current_winner:
            rähntier["points"] += 1 

pprint(rähntiere)

print(max([rähntier["points"] for rähntier in rähntiere]))
    


# # vollständige Intervalle die Rähntier schafft 
# interval = time+sleep
# full_cycle = target_sec // interval
# distance_full_cycle = full_cycle*kmps*time

# # unvollständiges intervall
# remaining_sec = target_sec % interval

# remaining_distance = kmps* min(time, remaining_sec)

# rähntiere[rähntier] = distance_full_cycle + remaining_distance


#print(rähntiere)
#print(max(rähntiere))

 