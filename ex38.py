# string
ten_things = "Apples Oranges Crows Telephone Light Sugar"
# print this statement
print("Wait there are not 10 things on this list. Let\'s fix that.")

# take ten_things and split into list/array by spaces.
stuff = ten_things.split(' ')
# seperate list / array.
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while length of stuff is not equal to 10.
while len(stuff) != 10:
    # next_one is going to be the last item on more_stuff
    next_one = more_stuff.pop()
    # print adding + the last thing popped off.
    print("Adding: ", next_one)
    # add next_one to the stuff array / list.
    stuff.append(next_one)
    # print the length of the stuff array / list.
    print(f"There are {len(stuff)} items now.")

# print there we go plus the whole stuff array / list
print("There we go: ", stuff)

# print statement.
print("Let\'s do some things with stuff.")

# print the second item
print(stuff[1])
# print the last item
print(stuff[-1])
# pop off the last
print(stuff.pop())
# joins back into string
print(' '.join(stuff))
# joins a slice of the 3 and 4th objects with a \# works like range(3,5)
print('#'.join(stuff[3:5]))
