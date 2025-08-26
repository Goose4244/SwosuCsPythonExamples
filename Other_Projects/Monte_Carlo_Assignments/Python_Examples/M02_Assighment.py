#print('hello.')

# imports
from random import randint

# importing the module
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()

import numpy as np
import matplotlib.pyplot as plt


#  select distribution to simulate rolling a six sided die that is fair
# here is an example code:
# https://discuss.python.org/t/how-to-use-randit-with-the-random-module-to-create-a-six-sided-dice/9724
def roll_die():
    number_of_sides = 6
    roll = randint(1, number_of_sides   )
    #print(f'our roll was {roll}, ', end = '')
    return roll

# set the bounds


#  Save the output
#we are going to save this to an array.
# creating the list
roll_result_25 = [0, 0, 0, 0, 0, 0]
roll_result_100 = [0, 0, 0, 0, 0, 0]
roll_result_100000 = [0, 0, 0, 0, 0, 0]

# creating 1-d array
n = np.array(roll_result_25)
#print(n)





# make a table for 25, 100, and 100,000 trials
# https://www.w3schools.com/python/python_for_loops.asp

number_of_rolls = 25

for roll_index in range (number_of_rolls):
    #print(f'roll index {roll_index} ', end = '')
    roll = roll_die()
    roll_result_25[roll - 1] += 1
    n = np.array(roll_result_25)
    #print(n)


n_25 = n
print(f'after 25 rolls, we see {n}.')

# make a chart that shows the probability of each number
# occuring for each of these three scenarios

number_of_rolls = 100

for roll_index in range (number_of_rolls):
    #print(f'roll index {roll_index} ', end = '')
    roll = roll_die()
    roll_result_100[roll - 1] += 1
    n = np.array(roll_result_100)
    #print(n)


n_100 = n
print(f'after 100 rolls, we see {n}.')

number_of_rolls = 100000

for roll_index in range (number_of_rolls):
    roll = roll_die()
    roll_result_100000[roll - 1] += 1

n = np.array(roll_result_100000)
n_100000 = n
print(f'after 100,000 rolls, we see {n}.')


probability_25 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
probability_100 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
probability_100000 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
for index in range(len(roll_result_25)):
    print(f'index is {index}.')
    probability_25[index] = float(roll_result_25[index]) / float(25)
    probability_100[index] = float(roll_result_100[index]) / float(100)
    probability_100000[index] = float(roll_result_100000[index]) / float(100000)


objects = ('1', '2', '3', '4', '5', '6')
y_pos = np.arange(len(objects))

plt.bar(y_pos, probability_25, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Probability of occurance')
plt.title('Data from 25 dice rolls')

plt.show()
