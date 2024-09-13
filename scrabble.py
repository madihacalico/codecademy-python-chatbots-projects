# project 9

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
# print(letter_to_points)

# function that takes in a word and returns how many points that word is worth
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter)

  return point_total

brownie_points = score_word("BROWNIE")
print(f"brownie_points: {brownie_points}")

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
print(player_to_words)

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)

# bonus

# function that adds word to the list of words a player has played
def play_word(player, word):
  word = word.upper()
  print(f"{player} plays the word {word}.")
  player_words_list = player_to_words[player]
  player_words_list.append(word)
  print(player_to_words)
  update_point_totals(player, word)

# function that updates players' total points
def update_point_totals(player, word):
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  print(player_to_points)

play_word("player1", "LOVELY")
play_word("Lexi Con", "GUILTY")
play_word("wordNerd", "unsatiable")
