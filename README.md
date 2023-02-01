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

# Functions/Attributes Explanation
This project is made up of only two files namely `main.py` and `transaction.py` with all processes in the latter.
`transaction.py` is consisted of a class (Transaction) with four general methods, namely:
1. update, used to update item details (name, amount and/or price)
2. delete, used to delete transaction and/or item
3. total, used to show purchase summary and price to pay

# Demonstration
1. Starting program
![Screenshot (1287)](https://user-images.githubusercontent.com/122712029/216049401-0fdd1a9d-29d3-4093-bcdb-78c90e34fba4.png)

2. Creating instances
![Screenshot (1288)](https://user-images.githubusercontent.com/122712029/216049539-d3159de4-69a5-4e42-b3cb-97895df4e879.png)

3. Adding item
![Screenshot (1288)](https://user-images.githubusercontent.com/122712029/216049606-db3dc831-f7df-43bb-b11d-cdfb0e11e86c.png)

4. Updating item
![Screenshot (1289)](https://user-images.githubusercontent.com/122712029/216049728-0a4617a5-c956-4b4c-bf57-b1bc9d591485.png)

5. Deleting item
![Screenshot (1290)](https://user-images.githubusercontent.com/122712029/216049887-9e75c6f3-f1c8-4af6-993d-99f143f3d7eb.png)

6. Resetting transaction
![Screenshot (1291)](https://user-images.githubusercontent.com/122712029/216050033-3cfaba22-d3e1-41dd-8136-0c5bf57b7cb5.png)

7. Showing purchase summary
![Screenshot (1292)](https://user-images.githubusercontent.com/122712029/216050140-db1cc508-4c7b-43e9-affd-c70fcab35b39.png)

# Limitation
1. Using an empty dictionary to store all inputs, which mean this dictionary stores inputs from all instances no matter which instance is currently being used to show the purchase list. This might come as quite confusing at first.
2. This project is unable to show summary from all instances.
