import random
list = []
list = ['red', 'green', 'blue']
list[0] #red
list[-1] #blue
list[:] #the entire list
list[::-1] #the elements of list in reverse order

list[3] = 'black' #overwrites list
list + [yellow', 'grey'] #adds 2 new items to end
list.append(2**4) #adds new item to end of list
list.insert(index, elem) #adds element at index loc
list.index(x) #finds the position in a list
list.extend(['new','items']) #adds these to end, similar to + or +=
list[2:5] = ['new', 'replace', 'item'] #items will replace slice
list[2:5] = [] #removes items
list[:] = [] #clears entire list
len(list) #will tell you how many items in list
len(''.join(list)) #the number of characters in the list
list[0][1] #access the 2nd letter of the first element in list
list[0][-1] #access the last letter of the first element in list
list[-1][-1] #access the last letter of the last element in list
list[::-1][0][::-1] #this would bring the first list element spelled backwards
list[::-1][::-1] #this is just the original list again
''.join(list)[::-1] #This would concatenate the list and reverse it


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
''.join(letters) # 'abcdefg' this will concetenate a list

list2 = [num for num in range(5)] #create quick sequential list

for num2 in range(5): #create list
      list2 +=[num2]

#create random list
#import random
random.sample(range(30), 4)
[3, 1, 21, 19]

#import random
ls = random.sample(range(30), 4)
ls

''.join()

[n for n in range(min(list),max(list))] #build list of sequential numbers
                                        #base on min.max in other list
tlist = list(zip(*alist)) #a handy 'idiom' for transposing a nested list,
                                      #    turning 'columns' into 'rows':



