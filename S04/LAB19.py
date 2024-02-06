# def create_function(kind='+'):
#     source = f'''
# def f(*args):
#     result = 0
#     for a in args:
#         result {kind}=a
#     return result
# '''
#     exec(source, globals())
#     return f
#
#
# f_add = create_function('+')
# print(f_add(1, 2, 3, 4))
#
# f_subs = create_function('-')
# print(f_subs(10, 20, 30))

from datetime import datetime


def time_between(time_unit):
    sec=0
    if time_unit == 'm':
        sec = 60
    elif time_unit=='h':
        sec = 3600
    elif time_unit=='d':
        sec=86400

    source=f'''
def f(start, end):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {sec})[0]
'''
    exec(source, globals())

    return f


start = datetime(2019, 1, 1, 0, 0, 0)
end = datetime.now()

f_minutes = time_between('m')
f_hours = time_between('h')
f_days = time_between('d')

print(f_minutes(start, end))
print(f_hours(start, end))
print(f_days(start, end))

