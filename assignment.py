print("===  GROCERY COST COMPARISON TOOL  ===")

rice_price = 12
milk_price = 4
fruit_price = 8
num_of_baskets = 2
family_members = 4

print("===  PART ONE: THE EXAMPLE ORDER   ===")
print("The price of rice:", end=" $")
print(rice_price)
print("The price of milk:", end=" $")
print(milk_price)
print("The price of fruit:", end=" $")
print(fruit_price)
print("The number of baskets:", num_of_baskets)
print("The number of family members:", family_members)

total_cost = num_of_baskets * (rice_price + milk_price + fruit_price)
print("\nTotal cost:", end=" $")
print(total_cost)
cost_per_person = total_cost / family_members
print("Cost per family member:", end=" $")
print(cost_per_person)

print("\n===  PART TWO: THE USER'S ORDER    ===")
total_items = int(input("How many items have you ordered? "))
total_people = int(input("How many people will you be sharing with? "))

if total_people == 0:
    print(f"\nYou cannot share between {total_people} people")
elif (total_items % total_people) == 0:
    print(f"\nYou can share evenly between everyone, giving {total_items // total_people} items to each person")
elif (total_items % total_people) == 1:
    print(f"\nYou cannot share evenly between everyone, you will have {total_items % total_people} item left over")
else:
    print(f"\nYou cannot share evenly between everyone, you will have {total_items % total_people} items left over")

print("\n=== PART THREE: THE WEEKLY AVERAGE ===")
recorded_average = 65
total_weeks = 4
wrong_cost = 50
right_cost = 80

print("Recorded weekly average:", end=" $")
print(recorded_average)
print("Total weeks:", total_weeks)
print("Incorrect cost in average:", end=" $")
print(wrong_cost)
print("Correct cost meant to be in average:", end=" $")
print(right_cost)

og_sum = 65 * 4
print(f"\nThe original sum:", end=" $")
print(og_sum)
new_sum = og_sum - (wrong_cost - right_cost)
print(f"The new sum:", end=" $")
print(new_sum)

new_average = new_sum / total_weeks
print("\nThe new weekly average:", end=" $")
print(new_average)

print("\n===  PART FOUR: STORE COMPARISON   ===")
store_a_average = 70
store_b_average = 75
store_c_average = 80

print("Average spending in store A:", end=" $")
print(store_a_average)
print("Average spending in store B:", end=" $")
print(store_b_average)
print("Average spending in store C:", end=" $")
print(store_c_average)

all_store_average = (store_a_average + store_b_average + store_c_average) / 3
print("\nAverage of all three stores:", end=" $")
print(all_store_average)

print("Is store A above the average? ", store_a_average > all_store_average)
print("Is store B above the average? ", store_b_average > all_store_average)
print("Is store C above the average? ", store_c_average > all_store_average)

verdict = (store_a_average > all_store_average and store_b_average > all_store_average and store_c_average > all_store_average)

print("\n===  PART FIVE: PURCHASE SUMMARY   ===")
print("Cost per family member:", end=" $")
print(cost_per_person)
print("The new weekly average:", end=" $")
print(new_average)
print("Are all stores above the average?", verdict)