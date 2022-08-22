from collections import Counter

def totalFruit(fruits):
    
    counts = Counter()
    low_position = 0
    for high_position in range(len(fruits)):
        counts[fruits[high_position]] +=1
        if len(counts) > 2:
            # third fruit has been encountered

            #reduce count for fruit at low position
            counts[fruits[low_position]] -=1

            # if the count went to 0, remove the fruit
            if not counts[fruits[low_position]]:
                counts.pop(fruits[low_position])
            # increment low position bc there are >2 fruits 
            # currently in window and until that is not true
            # must take a fruit out for every fruit in to keep 
            # best window seen accurate                                        
            low_position += 1
    return (high_position - low_position + 1)
    

# f = [1,2,3,2,1,1]
# f = [0,0,0,0,3,2,2,2,2,2,2,4,7,7]
f = [1,2,3,1,2,3,1,1,2,3,1,2,1]

print(totalFruit(f))




# aproach that exceeds time

# def totalFruit(fruits):
#     if len(fruits) == 0:
#         return 0

#     basket_totals = set()
#     b1_fruit_type = None
#     b2_fruit_type = None
#     b1_count = 0
#     b2_count = 0
#     starting_pos = 0
#     while starting_pos < len(fruits):
#         for i in range(starting_pos, len(fruits)):
#             curr_fruit = fruits[i]
#             if b1_fruit_type is None:
#                 b1_fruit_type = curr_fruit
#                 b1_count = 1
#             elif b1_fruit_type == curr_fruit:
#                 b1_count +=1
#             elif b2_fruit_type is None:
#                 b2_fruit_type = curr_fruit
#                 b2_count = 1
#             elif b2_fruit_type == curr_fruit:
#                 b2_count +=1
#             else:
#                 # must document where we would have had to stop
#                 basket_totals.add(b1_count+b2_count)
#                 b1_count = 0
#                 b2_count = 0
#                 b1_fruit_type = None
#                 b2_fruit_type = None
#                 break
#         starting_pos += 1 # try again starting from next position
#         basket_totals.add(b1_count+b2_count)
#         b1_count = 0
#         b2_count = 0

#     return max(basket_totals)