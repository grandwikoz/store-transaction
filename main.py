trsnct1 = Transaction("wik")
trsnct1.add_item("sugar", 44, 90)
trsnct1.add_item("choco", 11, 22)
trsnct1.add_item("tea", 33, 98)

trsnct2 = Transaction("peb")
trsnct2.add_item("shirts", 11, 12)
trsnct2.add_item("pants", 33, 44)
trsnct2.add_item("hats", 55, 66)

user1.purchase_list
user1.update_item_name("sugar", "lollipop")
user1.purchase_list
user1.update_item_amount("choco", 100000)
user1.purchase_list
user1.update_item_price("tea", 70000)
user1.purchase_list
user2.delete_item("hats")
user1.purchase_list
user2.reset_transaction()
user1.purchase_list
user1.total_price()