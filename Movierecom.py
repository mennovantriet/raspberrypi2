# importing csv and numpy
import csv as csv
import numpy as np

# importing the user reviews
import csv
with open ('userReviews.csv', encoding='utf-8-sig') as df:
    reader = csv.DictReader(df, delimiter=';')
    df = list(reader)

# stating favorite movie
FavoriteMovie = 'inception'

# analysing the data by printing the header and first value
print(df[:1])

# making a list for Metascore as X
X = []
for row in df:
    X.append(row['Metascore_w'])
# making datatype float
X = np.array(X, dtype=np.float32)
# check data type of array
print('The datatype of the Metascore is:',X.dtype)
# printing average and median score of all movies
print('The average of all movies is:',np.average(X))
print('The median of all movies is:',np.median(X))

# making a list for Metascore of FavoriteMovie as A
A = []
for row in df:
    if row['movieName'] == FavoriteMovie:
        A.append(row['Metascore_w'])
# making datatype float
A = np.array(A, dtype=np.float32)
#check datatype of array
print('The datatype of the Metascore is:',A.dtype)
# printing average, my score and median score of the FavoriteMovie
print('The average score for',FavoriteMovie,'is:',np.average(A))
print('The score that i would give',FavoriteMovie,'is : 9')
print('The median score for',FavoriteMovie,'is:',np.median(A))

# the score that i gave was a bit higher than the average but below  the median

# printing all the scores given by revewers of the FavoriteMovie
print(*A, sep = ", ")

# making a list for Authors as B
B = []
for row in df:
    B.append(row['Author'])

# making a list for C all users that reviewed the FavoriteMovie.
C = []
for row in df:
    if row['movieName'] == FavoriteMovie:
        C.append(row['Author'])
print(C)

# definging average score of the FavoriteMovie as AA for later compute
AA = np.average(A)
print(AA)

# a printed list of all movies recommendations that have been seen by a reviewer that also saw the FavoriteMovie and have a score equal or greater than the FavoriteMovie:
author = str(C)
average = str(AA)
D = []

for row in df:
    if (row['Author']) in C:
        if row['Metascore_w'] >= average:
                D.append(row['movieName'])

# removing duplicate movies from list
D = list(dict.fromkeys(D)) 
# removing inception by finding its index number
del D[D.index(FavoriteMovie)]

print(D)

# a printed list of all movies recommendations that have been seen by a reviewer that also saw the FavoriteMovie and have a score equal or greater than the FavoriteMovie,
# but without removing the duplicates, FavoriteMovie and by adding a counter of times recommended:
E = []
for row in df:
    if (row['Author']) in C:
        if row['Metascore_w'] >= average:
                E.append(row['movieName'])

from collections import Counter
cnt = Counter(E)
F = cnt
print(F)

# the first 5 recommended movies by count 'django-unchained': 27, 'the-dark-knight': 27, 'the-dark-knight-rises': 24, 'the-social-network': 23 and 'avatar': 20,
# have i actually already seen and found them all really good, so that means that it works quite well. Only the 6th ('toy-story-3') with which has been scored by 19 reviewers
# is a movie that i haven't seen, so i will put that on my list.

# saving movies recommendations (D) as a CSV file
np.savetxt("recommendations.csv", D, delimiter=",", fmt='% s')
