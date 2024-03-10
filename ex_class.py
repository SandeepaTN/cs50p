class Student:
    def __init__(self,name,branch) :
        if not name:
            raise ValueError("name not entered")
        
        self.name=name
        self.branch=branch

    def __str__(self) -> str:
        return f"{self.name} from {self.branch}"  
    
    @property
    def branch(self): 
        return self._branch  
    @branch.setter
    def branch(self,branch):
        if  branch not in ["is","cs","ec"]:
            raise ValueError("missing branch")
        self._branch= branch
         

def main():  
    student=get_student()
    try:
        student.branch='cv'
    except ValueError:
        get_student()
    print(student)
    

def get_student():
    name=input("Enter name ")
    branch=input("Enter branch ")
    try:
        return Student(name,branch) 
    except ValueError:
        get_student()
   
if __name__=="__main__":
    main()   