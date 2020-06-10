
class Icp1:
    def rev(self):
        """take input from the user"""
        print('This is to reverse the string')
        str = input('Enter a string----->')
        """stats with 0th index char to last del every 2nd index char"""
        offset = str[0: :2]
        """reverse the string in the offset"""
        revstr = offset[::-1]
        """print the reversed str"""
        print('reversed string after deletion of some char is--->', revstr)
    def add(self):
        """take two numbers from user as input and convert it to float data type"""
        print("Addition of two numbers")
        num1 = float(input("Enter a number-->"))
        num2 = float(input("Enter other number-->"))
        """addtion of two user input number"""
        print("The result is")
        sum = num1+num2
        """print the sum"""
        print(num1, '+', num2, '=', sum)
        print(num1, '-', num2, '=', num1-num2)
        print(num1, '*', num2, '=', num1*num2)
    def rep(self):
        str = input("Enter the string--->")
        print("Given input is-->", str)
        repstr = str.replace("python", "pythons")
        print("Output is-->", repstr)

if __name__ == '__main__':
    my_icp = Icp1()
    my_icp.add()
    print("\n")
    my_icp.rep()
    print("\n")
    my_icp.rev()

