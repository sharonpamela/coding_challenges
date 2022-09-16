    '''
    # The knows API is already defined for you.
    # return a bool, whether a knows b
    # def knows(a: int, b: int) -> bool:
    '''

    def findCelebrity(self, n):
        def isCeleb(i):
            for j in range(n):
                if (i == j): continue
                if knows(i,j) or not knows(j,i):
                    return False
            return True

        possible_celeb = 0
        for i in range(1,n):
            if knows(possible_celeb, i):
                possible_celeb = i
        if isCeleb(possible_celeb):
            return possible_celeb
    return -1