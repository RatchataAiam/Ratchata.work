# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("Archen Aydin", 24, "AngThong", "Thailand")  # name, age, city, country
    hobbies = ['Dancing','Singing']
    name,age,city,country=person
    while True:
        # Your code here
        print("Your Profile")
        print(f"Name:{name} Age:{age} City:{city} Country:{country}")
        print(f"Hobbies:{hobbies}")
        X=int(input("Choose Any Faction 1.To Add Your Hobbies 2.Remove Your hobbies 3.Update Your age 4.Exit:"))
        if(X==1):
            NewHobby=input("Add Your New Hobbies:")
            hobbies.append(NewHobby)
        elif(X==2):
            print(f"Now You Have Hobbies:{hobbies}")
            hobbies.remove(input("Witch one You want to remove?:"))
        elif(X==3):
            age=input("Add Your New age:")
            person_list=list(person)
            person_list[1]=age
            person=tuple(person_list)
        elif(X==4):
            print("All Done Thank You!")
            break
        else:
            print("Something Is Wrong Pls Try Again...")
if __name__ == "__main__":
    personal_info_manager()