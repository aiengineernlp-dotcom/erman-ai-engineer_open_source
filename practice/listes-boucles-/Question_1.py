transactions = [1200, 3000, 250, 7800, 540, 3000, 9100, 250, 1500, 7800]

'''   Identify and display all transaction values that appear more than once. '''
# copy of the list for make easy the comparaison a the end
copy_transactions = transactions[:]
is_doubled = []  # here i created the list where i will save the double values
for i in copy_transactions:  # here i loop in to my copy list
    if copy_transactions.count(
            i) > 1:  # here is the key with  ".count(i)>" in order to know how many time a value is present in to my list
        if i not in is_doubled:  # i want to make sure that i did not yet add it in my list
            is_doubled.append(i)  # add to my list
            print(f"\n  {is_doubled}")  # final list with the values doubled added

print('\n')
"""Detect transactions greater than ₹5000 as these may require fraud monitoring. """
is_greater_than_5000 = []
for i in copy_transactions:
    if i > 5000:
        is_greater_than_5000.append(i)
        print(f"\n {is_greater_than_5000}")

print('\n')
"""Calculate the total spending for the day."""
total_spending = 0
for i in copy_transactions:
    total_spending = total_spending + i
print(f"\n The total spending for the day is  : ₹{total_spending} ")

"""Create a new list containing only unique transaction values."""

print('\n')
unique_transaction = []
for t in copy_transactions:
    if copy_transactions.count(t) == 1:
        unique_transaction.append(t)
        print(unique_transaction)

"""Sort the unique transaction list in descending order to view the largest transactions first."""

print('\n')
# pas besoin de boucle ici
sorted_transaction_descending = sorted(copy_transactions, reverse=True)
print(sorted_transaction_descending)

