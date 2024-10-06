class Solution:
    def average(self, salary: List[int]) -> float:

        '''
        U:




        M:


        P:


        I:
        '''
        count = 0

        maximum, minimum = max(salary), min(salary)
       
        salary.remove(maximum)
        salary.remove(minimum)
        print(salary)

        for wage in salary:
            count += wage
        
        return float(count / len(salary))

        '''
        R:



        E:





        '''
        