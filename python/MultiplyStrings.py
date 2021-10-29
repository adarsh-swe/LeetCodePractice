class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        nums = { 
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
        }

        sum = 0

        for i in range(len(num1)):
            for j in range(len(num2)):
                sum += (10**(len(num1)-i-1))*(10**(len(num2)-j-1))*nums[num1[i]]*nums[num2[j]]

        return str(sum)