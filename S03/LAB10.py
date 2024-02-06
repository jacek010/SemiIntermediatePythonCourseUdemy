
ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
print("LAB10")

connections = [(start, end) for start in ports for end in ports]
print("All connections", len(connections))
print(connections)


connections_no_self = [(start, end) for start in ports for end in ports if start != end]
print("All connections without self-connections", len(connections_no_self))
print(connections_no_self)


routes = [(start, end) for start in ports for end in ports if start < end]
print("All routes without self-connections and doubled connections", len(routes))
print(routes)
