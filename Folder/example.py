name = "Abebe"
count = 0
#here I used a global variable which can lead to a bug in larger programs, when multiple functions modify the global variable.
#It reduces clarity and modularity of the function.

#To avoid this problem, it's better to pass count as a parameter to the function.

#here I incremented the count in every recursive call, but recurssion is not memory efficient for this type of problem.
#It's better to use a loop to iterate through the list of names.

def Callname (count, name):
    if count == 5:
        return
    else:
        print (count+1,":", name)
        count += 1
        Callname (count, name)

Callname (count, name)

#Better way fo doing this
def Callname(count, name):
    if count == 5: #base case
        return
    else:
        print (count+1, ":", name) #prints with numbering
        Callname (count+1, name) #recursive call with updated count

Callname(count, name)
