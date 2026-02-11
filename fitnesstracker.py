class FitnessTracker:
    def __init__(self):
        self.__steps = 0
        self.__calories = 0.0

    def addSteps(self, steps):
        if steps > 0:  
            self.__steps += steps

    def addCalories(self, calories):
        if calories > 0:  
            self.__calories += calories

    def getSummary(self):
        return f"Steps: {self.__steps}, Calories Burned: {self.__calories:.2f}"