projects = ["Brexit", "Nord Stream", "US Mexico Border"]
leaders = ["Theresa May", "Wladimir Putin", "Donald Trump and Bill Clinton"]

for project, leader in zip(projects, leaders):
    print(f"The leader of {project} is {leader}.")

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for num, (project, date, leader) in enumerate(zip(projects, dates, leaders)):
    print(f"{num} - The leader of {project} started {date} is {leader}.")
