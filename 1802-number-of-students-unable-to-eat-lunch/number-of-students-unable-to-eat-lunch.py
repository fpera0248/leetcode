class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ''' 
        U:
        queue of students fifo
        stack of sandiwhces lifo

        number of sandwhiches = number of students

        stops when none of the queue studetns want the top sandwhich and can't eat

        fgiven two int lists students and sandwhiches, i=0 top of stack, j=0 is front of queue
        sandwhich[i] == type of sandwhich
        student[i] = preferences
        
        students = [1,1,1], sandwiches = [0,1,1]
        output 3
        if students[i] == sandwhich[i] both are lists, and do not require actually stack and queue implementations but help to determine the behavior and output you should get

        M:
        stack

        P:
        both are lists, students list changes but sandwhich list is only removed iterms from, students list is updated

        use stack to keep track of students in list




        '''

        counter = 0

        while students:
            if counter > len(students):
                return len(students)

            if not students:
                return 0

            if sandwiches[0] != students[0]:
                students.append(students[0])
                students.remove(students[0])
                counter += 1

            elif sandwiches[0] == students[0]:
                students.remove(students[0])
                sandwiches.remove(sandwiches[0])
                counter = 0

        return len(students)

            

    
        