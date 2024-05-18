class BudgetCategory:
    def __init__ (self, category_name, budget):
        
        self.__category_name = category_name
        self.__budget = budget
        self.expenses = {}

    def get_category(self):
        print(self.__category_name)

    def get_budget(self):
        print(self.__budget)
    
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
        return self.expenses
    

    def add_expenses(self, expense_name, amount):
        budget_counter = self.__budget
        try:
            amount = int(amount)
            if amount > budget_counter:
                print("Error: you don't have enough in the budget for that")
                return
            
            if amount < 0:
                print("Error: a budget can't be less than 0")
                return

            
            budget_counter -= amount
            expense_dictionary = self.expenses

            if expense_name not in expense_dictionary:
                expense_dictionary[expense_name] = []
            
            expense_dictionary[expense_name].append(amount)
            print(expense_dictionary)
        except ValueError:
            print("Amount has to be positive Interger")


        while True:
            try:
                additonal_expenses = input("add more expenses: enter('done') when finished ").strip()
                
                if additonal_expenses.lower() == 'done':
                    print(expense_dictionary)
                    break


                if additonal_expenses not in expense_dictionary:
                    additonal_amount = int(input("Enter amount cost: ")) 
                    
                    expense_dictionary[additonal_expenses] = []

                    if additonal_amount > budget_counter:
                        print("Error: you don't have enough in the budget for that")
                        continue

                    if additonal_amount < 0:
                        print("Error: a budget can't be less than 0")
                        continue

                    budget_counter -= additonal_amount

                    if additonal_expenses not in expense_dictionary:
                        expense_dictionary[additonal_expenses] = []

                    expense_dictionary[additonal_expenses].append(additonal_amount)
                    print(expense_dictionary)

                    print(expense_dictionary)
            except ValueError:
                print("Error: additonal amount has to be poitive integers")
                continue
                    
        #     else:
        #         expense_dictionary[additonal_expenses].append(additonal_amount)
        #         print(expense_dictionary)

            
