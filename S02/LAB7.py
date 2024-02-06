colors = ['red', 'orange', 'green', 'violet', 'blue', 'yellow']


def get_n_colors(n: int) -> list:
    return colors[:n]


for i in range(1, len(colors) + 1):
    print(get_n_colors(i))


definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.'

print(definition[definition.index('(')+1:definition.index(')')])
