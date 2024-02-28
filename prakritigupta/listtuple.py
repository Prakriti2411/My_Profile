my_list = []
movie = input("Enter a name of your favorite movie:")
name = str(movie)
my_list.append(name)
while True:
    movie = input("Enter a name of movie (or Enter the at empty space):")
    if movie == "":
        break
    name = str(movie)
    my_list.append(name)
print(my_list)


