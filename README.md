# store-transaction
A simple mechanism to record store transaction
# Background
A newly established store has no database regarding its item, type, amount or price. Therefore, this project is intended to help it set up a simple mechanism to record transaction.
# Requirement
Class Object:
1. Transaction ID
Class Attribute:
1. Item name
2. Item amount
3. Item price
# Flow
1. This project uses to `transaction ID` to create an object which then will be filled with three attributes namely `item name`, `item amount` and `item price` to record purchase
2. Since this project uses a class, then users are allowed to create many instances
3. User input will be processed to generate output in form of dictionary with `transaction ID` as key and `item name`, `item amount` and `item price` as value nested in a list
4. This input could be manipulated through update and delete module (explained below)
![Screenshot (1265)](https://user-images.githubusercontent.com/122712029/216047764-e2e6f0a7-9da6-473d-a1f3-e746fa5ddee6.png)
#Functions/Attributes Explanation
This project is made up of only two files namely `main.py` and `transaction.py` with all processes in the latter.
`transaction.py` is consisted of a class (Transaction) with four general methods, namely:
1. update, used to update item details (name, amount and/or price)
2. delete, used to delete transaction and/or item
3. total, used to show purchase summary and price to pay
#Demonstration

