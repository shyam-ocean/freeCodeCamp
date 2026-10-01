"""create a rectangle and square class with methods to calculate 
area, perimeter, diagonal, and draw the shape using * """

class Rectangle:
    #set up the rectangle
    def __init__(self,width, height):
        self.width = width
        self.height =height

    def set_width(self,width):
        self.width =width

    def set_height(self,height):
        self.height =height

    # area
    def get_area(self):
        return self.width *self.height

    #perimeter= 2*width + 2*height
    def get_perimeter(self):
        return 2*self.width + 2*self.height

    #diagonal = root(width squared + height squared)
    def get_diagonal(self):
        return (self.width **2 +self.height **2) **0.5

    # draw rectangle using *
    def get_picture(self):
        # too big for width or height> 50
        if self.width >50 or self.height >50:
            return "Too big for picture."

        # make one line of * for each row
        str_line = ""
        for _ in range(self.height):
            str_line += "*" * self.width + "\n"
        return str_line

    #count how many times a shape fits in rectngle
    def get_amount_inside(self,shape):
        # how many fit across and how many fit down (horizontal, vertical)
        h_fit =self.width//shape.width
        v_fit = self.height //shape.height

        # multiply to get the total
        return h_fit*v_fit

    #text version of the rectangle
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    # set both width and height to the new side
    def set_side(self,side):
        self.width =side
        self.height = side

    # keep the square equal when width/height changes
    def set_width(self, width):
        self.set_side(width)

    def set_height(self,height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"

print("Rectangle and Square Area Calculator")

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))