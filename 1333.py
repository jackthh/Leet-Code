# Filter Restaurants by Vegan-Friendly, Price and Distance
# Given the array restaurants where  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]. You have to filter the restaurants using three filters.
# The veganFriendly filter will be either true (meaning you should only include restaurants with veganFriendlyi set to true) or false (meaning you can include any restaurant). In addition, you have the filters maxPrice and maxDistance which are the maximum value for price and distance of restaurants you should consider respectively.
# Return the array of restaurant IDs after filtering, ordered by rating from highest to lowest. For restaurants with the same rating, order them by id from highest to lowest. For simplicity veganFriendlyi and veganFriendly take value 1 when it is true, and 0 when it is false.


class Solution:
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        restaurants1 = restaurants
        restaurants2 = []
        restaurants3 = []
        restaurants4 = []
        restaurants5 = []
        restaurants6 = []

        # Check null
        if restaurants is None:
            return restaurants2

        # Check vegan
        if veganFriendly == 1:
            for i in range(len(restaurants1)):
                if restaurants1[i][2] == 1:
                    restaurants2.append(restaurants1[i])
        else:
            restaurants2 = restaurants1

        # Check maxPrice
        for i in range(len(restaurants2)):
            if restaurants2[i][3] <= maxPrice:
                restaurants3.append(restaurants2[i])

        # Check maxDistance
        for i in range(len(restaurants3)):
            if restaurants3[i][4] <= maxDistance:
                restaurants4.append(restaurants3[i])

        # Sort by rating and Id
        restaurants5 = self.descendantSort(restaurants4, 1, 0)

        for item in restaurants5:
            restaurants6.append(item[0])

        return  restaurants6





    def descendantSort(self, resList, y, z): # Selection sort
        for x in range(len(resList) - 1):
            for t in range(x + 1, len(resList)):
                # First property to compare
                if resList[t][y] >  resList[x][y]:
                    # Swap
                    temp = resList[x]
                    resList[x] = resList[t]
                    resList[t] = temp
                # Second property to compare
                elif resList[t][y] == resList[x][y]:
                    if resList[t][z] > resList[x][z]:
                        # Swap
                        temp = resList[x]
                        resList[x] = resList[t]
                        resList[t] = temp

        return resList


resList = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
temp = Solution()
print(temp.filterRestaurants(resList, 1, 50, 10))