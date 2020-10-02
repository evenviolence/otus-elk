data = [
                 'drogozina_user',
                   'drogozina_nice',
                   'drogozina_system',
                   'drogozina_idle',
                   'drogozina_iowait',
                   'drogozina_irq',
                   'drogozina_softirq',
                   'drogozina_steal',
                   'drogozina_quest',
                   'drogozina_guest_nice'
]

metrics = {}

try:
    with open('/proc/stat', 'r') as procfile:
        cputimes = procfile.readline()
        j = 0
        for i in cputimes.split(' ')[2:]:
            i = int(i)
            metrics[data[j]] = i
            j = j+1


except IOError as e:
    print('ERROR: %s' % e)
    sys.exit(3)

for key in metrics:
    print("# HELP ", key, "from /proc/stat")
    print("# TYPE ", key, "gauge")
    print(key, metrics[key])

