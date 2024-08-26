# project 4
# input
weight = 41.5
print(f"Weight of package is {weight}lbs.")

# check rate for ground shipping
if(weight <= 2):
  rate_ground = weight * 1.50
elif(weight <= 6):
  rate_ground = weight * 3.00
elif(weight <= 10):
  rate_ground = weight * 4.00
else:
  rate_ground = weight * 4.75

# ground shipping cost
flat_charge_ground = 20.00
cost_ground = rate_ground + flat_charge_ground
# ground shipping premium cost
cost_ground_prem = 125.0
# drone shipping cost
rate_drone = rate_ground * 3
cost_drone = rate_drone

# output to user
print(f"Cost of Ground Shipping: ${cost_ground}")
print(f"Cost of Ground Shipping Premium: ${cost_ground_prem}")
print(f"Cost of Drone Shipping: ${cost_drone}")

# extra - check cheapest shipping method
cheapest = min(cost_ground, cost_ground_prem, cost_drone)
if (cheapest == cost_ground):
  cheapest_method = "Ground Shipping"
elif (cheapest == cost_ground_prem):
  cheapest_method = "Ground Shipping Premium"
else:
  cheapest_method = "Drone Shipping"

print(f"The cheapest method of shipping is {cheapest_method}")
