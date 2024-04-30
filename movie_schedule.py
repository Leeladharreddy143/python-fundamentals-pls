current_movies = {'The Grinch':'11:00am',
                   'RRR':'12:00pm',
                   'Master':'2:00pm'
                                   }

print("We're showing the following movies:")
for key in current_movies:
    print(key)



movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't palying")
else:
    print(movie,'is playing at',showtime)
