# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movies = []
mov1, mov2, mov3 = (
    input("Enter 1st favorite movie name: "),
    input("Enter 2nd favorite movie name: "),
    input("Enter 3rd favorite movie name: "),
)
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
