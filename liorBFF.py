letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1,
          3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letters_to_points = {k: v for k, v in zip(letters, points)}
letters_to_points[" "] = 0
# print(letters_to_points)


def score_word(word):
    point_total = 0
    for x in word:
        for y in letters_to_points:
            if(x == y):
                point_total = point_total + letters_to_points[y]
    return point_total


brownie_points = score_word("BROWNIE")
print(brownie_points)
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": [
    "ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_words = {key: [word.upper() for word in words] for key, words in player_to_words.items()}
player_To_points = {}


def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
    for word in words:
        player_points = score_word(word)
    player_To_points[player] = player_points


for player, words in player_to_words.items():
    update_point_totals()
print(player_To_points)


def play_word(player, word):
    player_to_words[player] = word

print("Put a stupid input over here")
i = input()
print(i)
j = input()