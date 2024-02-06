# Generatory

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
print("LAB11")

counter = 0
connections = ((start, end) for start in ports for end in ports)
print("All connections")
for (start, end) in connections:
    print(f"{start} -> {end}")
    counter += 1
print(counter)


counter = 0
connections_no_self = ((start, end) for start in ports for end in ports if start != end)
print("All connections")
for (start, end) in connections_no_self:
    print(f"{start} -> {end}")
    counter += 1
print(counter)


counter = 0
routes = [(start, end) for start in ports for end in ports if start < end]
print("All connections")
for (start, end) in routes:
    print(f"{start} -> {end}")
    counter += 1
print(counter)
