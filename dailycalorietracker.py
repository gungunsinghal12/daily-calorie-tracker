# Name- Gungun
# Date- 11/29/2025
# Project Title- Daily Calorie Tracker CLI

while True:

    # TASK 1: Setup and Introduction
    print("---Welcome to Daily Calorie Tracker---")
    print()
    print("This tool helps you log your meals, track total calories,\n compare them with your daily limit, and save a report.\n")
    
    # TASK 2: Input and Data Collection
    meal_name=[]
    calorie_amount=[]
    
    n= int(input("Enter the number of meals you ate today: "))
    
    for i in range(n):
        meal= input("Enter meal name: ")
        calorie= int(input("Enter calorie amount: "))
        meal_name.append(meal)
        calorie_amount.append(calorie)
        
    # TASK 3: Calorie Calculations
    total= sum(calorie_amount)
    print("The toal calorie intake is",total,sep=" ")
    
    avg= int(total/n)
    print("The average calorie per meal is",avg,sep=" ")
    
    daily_limit= int(input("Enter daily limit: "))
    
    # TASK 4: Exceed Limit Warning System
    if daily_limit<total:
        print("You have exceeded your daily limit.")
    else:
        print("You are within your daily limit.")
        
    # TASK 5: Neatly Formatted Output
    print("Meal Name\tCalories")
    print("-----------------------------------")
    
    for i in range(len(meal_name)):
        print(f"{meal_name[i]}\t\t{calorie_amount[i]}")
        
    print(f"Total\t\t{total}")
    print(f"Average\t\t{avg}")
    
    # TASK 6 (Bonus): Save Session Log to File
    save= input("Do you want to save the report? (yes/no)").lower()
    
    if save=="yes":
        import datetime as dt
        filename = "calorie_log.txt"
        timestamp = dt.datetime.now()
        
        with open(filename, "a") as file:
            file.write("---DAILY CALORIE TRACKER LOG---\n")
            file.write(f"Timestamp: {timestamp}\n\n")
            file.write("Meal Name\tCalories\n")
            file.write("--------------------------------------\n")
            
            for i in range(len(meal_name)):
                file.write(f"{meal_name[i]}\t\t{calorie_amount[i]}\n")
                
            file.write("--------------------------------------\n")
            file.write(f"Total:\t\t{total}\n")
            file.write(f"Average:\t{avg}\n")
        
        print(f"\nSession saved to {filename}")
        
    print("\nThank you for using the Daily Calorie Tracker!")

    cont= input("Do you want to continue? (yes/no)").lower()

    if cont=="no":
        break


    
