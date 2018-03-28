import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import csv

''' 
Default values for the bounds of payment sizes:
Small = 0 - 20, Medium = 21 - 100 Large = 100 - 500, XL = 500+
'''
MAX_SMALL = 20
MAX_MED = 100
MAX_LARGE = 500

'''
Counters for the number of purchases for each size
'''
num_small_purchases = 0
num_med_purchases = 0
num_large_purchases = 0
num_x_large_purchases = 0

'''
Lists to keep track of the count of each check type based on the payment size
Ex. check_type_count[small, medium, large, x-large]
'''
paper_check_count = [0, 0, 0, 0]
direct_deposit_count = [0, 0, 0, 0]
same_day_check_count = [0, 0, 0, 0]
virtual_card_count = [0, 0, 0, 0]

payment_list = [paper_check_count,
                direct_deposit_count,
                same_day_check_count,
                virtual_card_count]

'''
Costs for using one check:
    Paper and Same day - Big check cost
    Direct deposit and virtual card - Small check cost
'''
BIG_CHECK_COST = 7.43
SMALL_CHECK_COST = 4.50

'''
A dictionary to organize payment types. Will be called by csv.reader to 
determine which list to edit
'''
payments_dict = {"4": paper_check_count,
                 "A": direct_deposit_count,
                 "S": same_day_check_count,
                 "X": virtual_card_count}


'''
Reads the data and counts the number of purchases for each size and 
payment type
'''
with open("Sample_Data.csv", "r") as data:
    csv_reader = csv.reader(data)
    next(csv_reader, None)  # skips headers
    for line in csv_reader:
        amount_paid = int(float(line[3]))
        payment_type = line[8]
        if 0 < amount_paid <= MAX_SMALL:
            payments_dict[payment_type][0] += 1
            num_small_purchases += 1
        elif MAX_SMALL < amount_paid <= MAX_MED:
            payments_dict[payment_type][1] += 1
            num_med_purchases += 1
        elif MAX_MED < amount_paid <= MAX_LARGE:
            payments_dict[payment_type][2] += 1
            num_large_purchases += 1
        elif MAX_LARGE < amount_paid:
            payments_dict[payment_type][3] += 1
            num_x_large_purchases += 1

'''
Converts the count for each size into percentages
'''
for lists in payment_list:
    lists[0] /= num_small_purchases / 100
    lists[1] /= num_med_purchases / 100
    lists[2] /= num_large_purchases / 100
    lists[3] /= num_x_large_purchases / 100

'''
Strings for the labels on the graph's x-axis
'''
str_small = "Small" + "\n" + "\$0" + " - \$" + str(MAX_SMALL)\
             + "\n" + "(" + str(num_small_purchases) + " Total)"
str_med = "Medium" + "\n" + "\$" + str(MAX_SMALL + 1) + " - \$" + str(MAX_MED)\
           + "\n" + "(" + str(num_med_purchases) + " Total)"
str_large = "Large" + "\n" + "\$" + str(MAX_MED + 1) + " - \$" + str(MAX_LARGE)\
             + "\n" + "(" + str(num_large_purchases) + " Total)"
str_x_large = "X-Large" + "\n" + ">$" + str(MAX_LARGE + 1)\
               + "\n" + "(" + str(num_x_large_purchases) + " Total)"

sizes = [str_small, str_med, str_large, str_x_large]

'''
The first graph
'''
bar_width = 0.2
x_pos = np.arange(len(sizes))
plt.figure(figsize=(11, 6))
plt.subplot(1, 2, 1)
plt.bar(x_pos, paper_check_count, width=bar_width, zorder=2, color='blue')
plt.bar(x_pos + (1*bar_width), direct_deposit_count, width=bar_width, zorder=2,
        color='orange')
plt.bar(x_pos + (2*bar_width), same_day_check_count, width=bar_width, zorder=2,
        color='green')
plt.bar(x_pos + (3*bar_width), virtual_card_count, width=bar_width, zorder=2,
        color='red')
plt.xticks(x_pos + (1.5*bar_width), sizes)
plt.title("PERCENTAGE OF PURCHASE SIZE DEVOTED" + "\n" +
          " TO EACH PAYMENT TYPE")
plt.xlabel("Payment Size Categories")
plt.ylabel("Percentage" + "\n" + "(# of Payment checks in Category / " +
           "Category size * 100)")

'''
The legend for the graphs
'''
blue_handle = patches.Patch(color='blue', label="Paper Check")
orange_handle = patches.Patch(color='orange', label="Direct Deposit")
green_handle = patches.Patch(color='green', label="Same Day Check")
red_handle = patches.Patch(color='red', label="Virtual Card")
plt.legend(handles=[blue_handle, orange_handle, green_handle, red_handle])
plt.grid(axis='y')

'''
Converts the count for each size to the original amount of orders and calculates
the money spent for each payment size
'''
money_spent = [0, 0, 0, 0]
for lists in payment_list:
    lists[0] *= num_small_purchases / 100
    lists[1] *= num_med_purchases / 100
    lists[2] *= num_large_purchases / 100
    lists[3] *= num_x_large_purchases / 100

    if lists == paper_check_count or lists == same_day_check_count:
        money_spent[0] += lists[0] * BIG_CHECK_COST
        money_spent[1] += lists[1] * BIG_CHECK_COST
        money_spent[2] += lists[2] * BIG_CHECK_COST
        money_spent[3] += lists[3] * BIG_CHECK_COST
    elif lists == direct_deposit_count or lists == virtual_card_count:
        money_spent[0] += lists[0] * SMALL_CHECK_COST
        money_spent[1] += lists[1] * SMALL_CHECK_COST
        money_spent[2] += lists[2] * SMALL_CHECK_COST
        money_spent[3] += lists[3] * SMALL_CHECK_COST

'''
Calculates the money spent on each payment type by multiplying the cost of check
'''
paper_check_count = [x*BIG_CHECK_COST for x in paper_check_count]
same_day_check_count = [x*BIG_CHECK_COST for x in same_day_check_count]
direct_deposit_count = [x*SMALL_CHECK_COST for x in direct_deposit_count]
virtual_card_count = [x*SMALL_CHECK_COST for x in virtual_card_count]

'''
Reedits the labels for the second graph to display money spent on the check
for each size
'''
str_small = "Small" + "\n" + "\$0" + " - \$" + str(MAX_SMALL)\
             + "\n" + "($" + str(money_spent[0]) + ")"
str_med = "Medium" + "\n" + "\$" + str(MAX_SMALL + 1) + " - \$" + str(MAX_MED)\
           + "\n" + "($" + str(money_spent[1]) + ")"
str_large = "Large" + "\n" + "\$" + str(MAX_MED + 1) + " - \$" + str(MAX_LARGE)\
             + "\n" + "($" + str(money_spent[2]) + ")"
str_x_large = "X-Large" + "\n" + ">$" + str(MAX_LARGE + 1)\
               + "\n" + "($" + str(money_spent[3]) + ")"
sizes = [str_small, str_med, str_large, str_x_large]

'''
The second graph
'''
plt.subplot(1, 2, 2)
plt.bar(x_pos, paper_check_count, width=bar_width, zorder=2, color='blue')
plt.bar(x_pos + (1*bar_width), direct_deposit_count, width=bar_width, zorder=2,
        color='orange')
plt.bar(x_pos + (2*bar_width), same_day_check_count, width=bar_width, zorder=2,
        color='green')
plt.bar(x_pos + (3*bar_width), virtual_card_count, width=bar_width, zorder=2,
        color='red')
plt.xticks(x_pos + (1.5*bar_width), sizes)
plt.title("TOTAL MONEY SPENT ON EACH " + "\n" + "PAYMENT TYPE")
plt.xlabel("Payment Size Categories")
plt.ylabel("Money spent")
plt.legend(handles=[blue_handle, orange_handle, green_handle, red_handle])
plt.grid(axis='y')

plt.tight_layout()
plt.show()
