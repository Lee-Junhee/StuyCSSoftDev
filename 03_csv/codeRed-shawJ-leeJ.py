import random
#just a string of numbers and other junk
garbage = " 1234567890.,\n"

#processing the csv file
csv = open("occupations.csv", "r") #opens the file for reading
occupations = csv.readlines(); #reads the lines into a list
dictionary = {} #creates empty dictionary
for job in occupations:
    char = len(job) #sets length as variable
    for num in range(1, char + 1):
        #print(num) #verify that code is counting proper integers
        if job[-num] == ",": #looks from the right to left for first comma
            percent = job[char - num:]
            #print("comma found") #verifies it finds commas
            break
    if percent.strip(garbage) == "": #if the percent is a valid float        
        #add the key/value pair to dictionary
        dictionary[job[:char-num].strip(' \"')] = float(percent.strip(",\n "))
#print(dictionary) #checks that the dictionary is created properly

#checking stats - setup
data = {}
for occupation in dictionary.keys():
    data[occupation] = 0

#choosing weighted occupation
def choose(verbose = False):
    chosen = random.random() * dictionary['Total']
    #print(chosen) #verification step
    for occupation in dictionary.keys():
        chosen -= dictionary[occupation]
        if chosen <= 0:
            if verbose:
                print("Randomly selected occupation: " + occupation)
            data[occupation] += 1 #gather data
            data['Total'] += 1
            break
choose(verbose = True)

#process stats
def process(verbose = False):
    for x in range(100000):
        choose()
    for occupation in dictionary.keys():
        data[occupation] /= float(data['Total']) / 100
        if verbose:
            print(occupation + "\tweight: " + str(dictionary[occupation]) + "\tsample: " +str(data[occupation]))
#process(verbose = True)
