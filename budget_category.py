class BudgetCategory:
    def __init__ (self, category_name, budget):
        
        self.__category_name = category_name
        self.__budget = budget
        self.__expenses = {}

    def get_category(self):
        return self.__category_name

    def get_budget(self):
        return self.__budget
    
    def set_budget(self):
        while True:
            new_budget = input("Enter new Budget: ")
            try:
                if new_budget.isalpha():
                    print("Error: budget can only be positive intergers")
                    continue

                new_budget_int = int(new_budget)
                
                if new_budget_int < 0:
                    print("Budget can't be less than 0")
                    continue

                if new_budget_int > 0:
                    self.__budget = new_budget
                    print(f"New Budget: {new_budget}")
                    break

            except Exception as e:
                print(f"An Error occured: {e}")
                continue


    
    def set_category(self):
        while True:
            new_category = input("Rename budget: ").strip()
            try:

                if new_category == "":
                    print("Error: name can't be empty")
                    continue

                if any(char.isdigit()for char in new_category):
                    print("Error: Name can not contain digits")
                    continue

                else:
                    self.__category_name = new_category
                    print(f"Updated Category: {new_category}")
                    break

            except Exception as e:
                print(f"An error occured: {e}")
                continue


    def get_expenses(self):
        return self.__expenses
    

    def add_expenses(self, expense_name, amount):
        try:
            amount = int(amount)
            if amount > self.__budget:
                print("Error: you don't have enough in the budget for that")
                return
            
            if amount < 0:
                print("Error: a budget can't be less than 0")
                return

            
            self.__budget -= amount
            expense_dictionary = self.__expenses

            if expense_name not in expense_dictionary:
                self.__expenses[expense_name] = []
            
            self.__expenses[expense_name].append(amount)
            print(self.__expenses)
        except ValueError:
            print("Amount has to be positive Interger")


        while True:
            try:
                additonal_expenses = input("add more expenses: enter('done') when finished ").strip()
                
                if additonal_expenses.lower() == 'done':
                    return self.__expenses
                    


                additonal_amount = int(input("Enter amount cost: ")) 
                if additonal_amount > self.__budget:
                    print("Error: you don't have enough in the budget for that")
                    continue

                if additonal_amount < 0:
                    print("Error: a budget can't be less than 0")
                    continue

                self.__budget -= additonal_amount
                if additonal_expenses not in self.__expenses:
                    self.__expenses[additonal_expenses] = []

                self.__expenses[additonal_expenses].append(additonal_amount)
                print(self.__expenses)

            except ValueError:
                print("Error: additonal amount has to be poitive integers")
                continue
                    
      
            
    def display_details(self):
        # expenses_dict = self.expenses
        
        while True:
            try:
                expense_name = input("Enter expense name: (enter 'done' when finished) ").strip()

                if expense_name.lower() == 'done':
                    break

                amount = int(input("Enter amount: "))

                if amount < 0:
                    print("Error: amount has to be more than 0")
                    continue
                
                if amount > self.__budget:
                    print(f"Error: amount can't be higher than expense")
                    continue
                
                self.add_expenses(expense_name, amount)

            except ValueError:
                print("Error: amount has to be positive integer")
                continue
            
            print("expenses: ",self.get_expenses())
            print("Remaining Budget: ", self.get_budget())
            
        