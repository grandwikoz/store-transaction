from tabulate import tabulate
from dataclasses import dataclass
import pandas as pd

@dataclass
class Transaction:
    '''
    This class will be used to store transactions as instances.
    Input: transaction ID
    '''
    id : str
    purchase_list = {} #creating an empty dictionary to store all transactions made by users
        
    def add_item(self, item_name, item_amount, item_price):
        '''
        Input: item name, item amount and item price.
        
        Process:
        1. Method will check whether item amount and price are positive number. if not, a notification will be given.
        2. After that, method will check whether the ID is a new or existing one.
        If it is new, then a new dictionary will be built, and if the latter then input data will be appended to existing ID.
        
        Output: 
        A dictionary with transaction ID as key and purchase list (name, amount and price) as value.
        
        '''
        if type(item_amount) == int or type(item_amount) == float:
            if item_amount < 0:
                print("Amount must be greater than zero.")
                return
            pass
        else:
            print("Amount must be numeric.")
            return
        if type(item_price) == int or type(item_price) == float:
            if item_price < 0:
                print("Price must be greater than zero.")
                return
            pass
        else:
            print("Price must be numeric.")
            return
        purchase = [item_name, item_amount, item_price]
        if self.id not in self.purchase_list.keys():
            self.purchase_list[self.id] = [purchase]
        else:
            prev_purchase = self.purchase_list[self.id]
            prev_purchase.append(purchase)
            self.purchase_list[self.id] = prev_purchase
    
    def update_item_name(self, item_name, updated_item_name):
        '''
        Input:
        1. Item name
        2. Updated item name
        Process: overwriting item name with updated one
        Output: new item name
        '''
        list = self.purchase_list[self.id]
        for item in list:
            if item[0] == item_name:
                item[0] = updated_item_name
    
    def update_item_amount(self, item_name, updated_item_amount):
        '''
        Input:
        1. Item name
        2. Updated item amount
        Process: overwriiting item amount with updated one. Updated value must be positive number.
        Output: updated amount
        '''
        if type(updated_item_amount) == int or type(updated_item_amount) == float:
            if updated_item_amount < 0:
                print("Amount must be greater than zero.")
                return
            pass
        else:
            print("Amount must be numeric.")
            return
        list = self.purchase_list[self.id]
        for item in list:
            if item[0] == item_name:
                item[1] = updated_item_amount

    def update_item_price(self, item_name, updated_item_price):
        '''
        Input:
        1. Item name
        2. Updated item price
        Process: overwriiting item price with updated one. Updated value must be positive number.
        Output: updated price
        '''
        if type(updated_item_price) == int or type(updated_item_price) == float:
            if updated_item_price < 0:
                print("Price must be greater than zero.")
                return
            pass
        else:
            print("Price must be numeric.")
            return
        list = self.purchase_list[self.id]
        for item in list:
            if item[0] == item_name:
                item[2] = updated_item_price
                
    def delete_item(self, item_name):
        '''
        Input: item name
        Process: deleting certain item based on given name
        Output: deleted item
        '''
        list = self.purchase_list[self.id]
        index_check = 0
        for item in list:
            if item[0] == item_name:
                index_check = item
        item_index = list.index(index_check)
        del list[item_index]
        
    def reset_transaction(self):
        '''
        Input: none (using instance)
        Process: deleting used instance
        Output: deleted instance
        '''
        del self.purchase_list[self.id]
        
    def total_price(self):
        '''
        Input: none (using instance)
        Process:
        1. Calculating sub total for each item
        2. Totalling all purchases
        3. Determining discount
        4. Determining final price
        5. Show purchase list and final price in tabular view
        Output:
        Purchase list and final price in tabular view
        '''
        list = self.purchase_list[self.id]
        total_price = 0
        for item in list:
            sub_total_price = float(item[1]) * float(item[2])
            item.append(sub_total_price)
            total_price += item[3]  
        df = pd.DataFrame(list, columns=("Item", "Amount", "Price", "Sub Total"))
        df.index = [x for x in range(1, len(df.values)+1)]
        df.index.name = "No."
        disc = 0
        if total_price >500_000:
            disc = 0.1
        elif total_price > 300_000:
            disc = 0.08
        elif total_price > 200_000:
            disc = 0.05
        else:
            disc = 0
        disc_price = disc * total_price
        final_price = total_price - disc_price
        print("")
        print(df)
        print("=============================================")
        print("")
        print(f"Total Price: {total_price}\nDiscount Price: {disc_price}\nFinal Price: {final_price}") 