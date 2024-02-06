def calculate_paint(efficency_ltr_per_m2, *rooms):
    total_area = sum(rooms)
    paint = total_area * efficency_ltr_per_m2
    return paint


rooms = [42, 28, 30]

print(calculate_paint(0.25, *rooms))


def log_it(**kwargs):
    path = "LAB16_log.txt"
    with open(path, "a") as f:
        for key in kwargs.keys():
            f.write(f"{key} -> {kwargs[key]}  |  ")

        f.write("\n")


log_it(info='Starting processing forecasting')
log_it(type='ERROR', info='Not enough data', file='invoices', date='2020')
