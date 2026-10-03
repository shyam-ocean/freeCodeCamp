

"""creating a class called Hat that will be used to simulate a hat containing balls 
of different colors. The class will have methods to draw balls from the hat and to 
conduct experiments to calculate probabilities based on the drawn balls."""

import copy
import random

class Hat:
    def __init__(self, **balls):  # **kwargs, short for "keyword arguments"
        # ** before a parameter name tells the function to accept any no of named keyword arguments
        self.contents = []
        for color, count in balls.items():
            for _ in range(count):
                self.contents.append(color)

    def draw(self,num_balls):
        #if we ask for more balls than exist, return everything and empty the hat
        if num_balls >=len(self.contents):
            all_balls = list(self.contents)
            self.contents.clear()
            return all_balls

        # pick random balls one by one no replacement
        drawn_balls =[]
        for _ in range(num_balls):
            ball =random.choice(self.contents)
            self.contents.remove(ball)
            drawn_balls.append(ball)

        return drawn_balls


def experiment(hat, expected_balls,num_balls_drawn,num_experiments):
    #track how many runs meet all target criteria
    success_count  =0

    for _ in range(num_experiments):
        #make an exact, independent copy of the hat for trial
        hat_copy = copy.deepcopy(hat)
        
        #draw the requested count of balls
        drawn =hat_copy.draw(num_balls_drawn)

        # check if drawn balls meet or exceed required counts for all colors
        success = True
        for color, count in expected_balls.items():
            if drawn.count(color)<count:
                success=False
                break

        # increment success tally if all conditions passed
        if success:
            success_count +=1

    # prob = successful /total trials
    return success_count/num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)
