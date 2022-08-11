'''
Animal Shelter: An animal shelter, which holds only dogs and 
cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on 
arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat 
(and will receive the oldest animal of
that type). They cannot select which specific animal they would 
like. Create the data structures to
maintain this system and implement operations such as enqueue, 
dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked list data 
structure
'''
import time
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class ShelterQueue:
    '''
    implements a queue with a linked list
    '''

    def __init__(self):
        self.head = None
        self.last = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def enqueue(self, pet):
        if self.head is None:
            self.head = Node(pet)
            self.last = self.head
        else:
            self.last.next = Node(pet)
            self.last = self.last.next

    def dequeueAny(self):
        next_pet = self.head
        self.head = self.head.next
        return next_pet

    def dequeueCat(self):
        return self.dequeueType('cat')

    def dequeueDog(self):
        return self.dequeueType('dog')

    def dequeueType(self, pet_type):
        next_pet = self.head
        prev = None
        while (next_pet is not None and 
            next_pet.next is not None and 
            next_pet.data['animal_type'] != pet_type):
            prev = next_pet
            next_pet = next_pet.next

        if (next_pet is not None and 
            next_pet.data['animal_type'] == pet_type):
            if self.head == next_pet:
                self.head = self.head.next
            else:
                prev.next = next_pet.next
            return next_pet
        else:
            raise Exception(f"No {pet_type}s are found in the system")



firstAnimal = {'animal_name':'louie','animal_type':'cat', 'arrival_time':time.time()}
secondAnimal = {'animal_name':'grunter','animal_type':'dog', 'arrival_time':time.time()}
thirdAnimal = {'animal_name':'anny','animal_type':'dog', 'arrival_time':time.time()}
fourthAnimal = {'animal_name':'seashella','animal_type':'cat', 'arrival_time':time.time()}
fithAnimal = {'animal_name':'pulguita','animal_type':'dog', 'arrival_time':time.time()}

animalQueue = ShelterQueue()
animalQueue.enqueue(firstAnimal)
animalQueue.enqueue(secondAnimal)
animalQueue.enqueue(thirdAnimal)
animalQueue.enqueue(fourthAnimal)
# animalQueue.enqueue(fithAnimal)
# print(animalQueue)
print("First Pet to get adopted is: ",str(animalQueue.dequeueAny().data['animal_name']))
print("The next cat in line is: ", str(animalQueue.dequeueCat().data['animal_name']))
print("The next dog in line is: ", str(animalQueue.dequeueDog().data['animal_name']))
print("The next cat in line is: ", str(animalQueue.dequeueCat().data['animal_name']))
print("The next dog in line is: ", str(animalQueue.dequeueDog().data['animal_name']))
# print("The next dog in line is: ", str(animalQueue.dequeueDog().data['animal_name']))