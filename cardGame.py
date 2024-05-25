# Define suits and ranks
import random
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1]
Perm=[('s','m','l'),('s','l','m'),('m','s','l'),('m','l','s'),('l','s','m'),('l','m','s')]

# Create a list to hold all the cards
deck = []

def show(hide,disp,perm,Rc):
    high = 0
    low = 14
    mid=0
    for ele in Rc:
        if ele[0] < low and != hide and != disp:
            low=ele[0]
        if ele[0] > high and != hide and != disp:
            high = ele[0]
    
    for ele in Rc:
        if ele[0] != high and != low and != high:
            mid = ele[0]
    
    
    for ele in Perm[perm]:
        if ele == 's':
            ele = low
        else if ele == 'm':
            ele = mid
        else:
            ele = high
            
    print("hey this is your thing: ",disp)
    for ele in Perm[perm]:
        print(ele)
    
    (r,j) = input("can you take a guess: ")
    if(r,j) == hide:
        print("you got it right")
    else:
        print("ah bad guess!")

# Populate the deck with cards
for suit in suits:
    for rank in ranks:
        card = (rank,suit)  # Using the first letter of the suit
        deck.append(card)

# Print the deck
randomCards = random.sample(deck, 5)
    
count = 0 
array=set()
while count <=2:
    for i in range(3):
        for j in range(3):
            if i!=j and randomCards[i][1]==randomCards[j][1]:
                array.add(randomCards[i])
                count+=1

print(array)
high = 0
for i, ele in enumerate(array):
    if ele[0] > high:
        high = ele[0]
        index = i
        
        
print(index)

otherIndex=0 if index==1 else 1

print(otherIndex)

if(array[index]-array[otherIndex] <= 6){
    hide = array[Index]
    disp = array[otherIndex]
    perm = array[index]-array[otherIndex]
    show(hide,disp,perm,randomCards)
}else{
    hide = array[otherIndex]
    disp = array[index]
    perm = 13 -array[index]-array[otherIndex]
    show(hide,disp,perm,randomCards)
}




# print(randomCards)
    
    
