class c_math:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def f_mod_numbers(self):
        numbers = []
        for i in range(self.x, self.y):
            if (i % 7 == 0) and (i % 5 != 0):
                numbers.append(str(i))
        return numbers

if __name__ == "__main__":
    input_str = input("Enter two numbers separated by a space: ")
    x, y = map(int, input_str.split())
    obj= c_math(x,y);
print("List of numbers that are divisible by 7 and not 5 between ",x," and ",y," are :",obj.f_mod_numbers())