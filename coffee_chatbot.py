# project 5
# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  temp = get_temp()
  cup_type = get_cup_type()
  print(f"Alright, that's a {size} {temp} {drink_type} in a {cup_type}!")

  name = input("Can I get your name please?")
  print(f"Thanks, {name}! Your drink will be ready shortly.")

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  
  if res == 'a':
    return "small"
  elif res == 'b':
    return "medium"
  elif res == 'c':
    return "large"
  else:
    print_message()
    return get_size()

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
  res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  
  if res == 'a':
    return "brewed coffee"
  elif res == 'b':
    return "mocha"
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  
  if res == 'a':
    return "latte"
  elif res == 'b':
    return "non-fat latte"
  elif res == 'c':
    return "soy latte"
  else:
    print_message()
    return order_latte()

def get_temp():
  res = input('And would that be hot or iced? \n[a] Hot \n[b] Iced \n> ')

  if res == 'a':
    return "hot"
  elif res == 'b':
    return "iced"
  else:
    print_message()
    return get_temp()

def get_cup_type():
  res = input('Would you like to get a plastic cup for your drink or do you want to use your own reusable cup? \n[a] Plastic cup \n[b] Reusable cup \n> ')

  if res == 'a':
    return "plastic cup"
  elif res == 'b':
    return "reusable cup"
  else:
    print_message()
    return get_cup_type()
    
# Call coffee_bot()!
coffee_bot()
