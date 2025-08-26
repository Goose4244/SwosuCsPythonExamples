class Triangle:   
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height
   
    def get_area(self):
        area = 0.5 * self.base * self.height
        return area
   
    def print_info(self):
        print(f'Base: {self.base:.2f}')
        print(f'Height: {self.height:.2f}')
        print(f'Area: {self.get_area():.2f}')

if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    # TODO: Read and set base and height for triangle1
    triangle1_base = int(input('Enter the base length of triangle 1: '))
    triangle1_height = int(input('Enter the height of triangle 1: '))
    triangle1.set_base(triangle1_base)
    triangle1.set_height(triangle1_height)

    # TODO: Read and set base and height for triangle2
    triangle2_base = int(input('Enter the base length of triangle 2: '))
    triangle2_height = int(input('Enter the height of triangle 2: '))
    triangle2.set_base(triangle2_base)
    triangle2.set_height(triangle2_height)
      
    print('Triangle with smaller area:')  
    
    # TODO: Determine smaller triangle
    #       and output smaller triangle's info
    if triangle1.get_area() < triangle2.get_area():
        print(triangle1.get_area(),'\n', triangle1.print_info())
    elif triangle1.get_area() == triangle2.get_area():
        print("The two triangles have the same area.")
    else:
        print(triangle2.get_area(),'\n', triangle2.print_info())
