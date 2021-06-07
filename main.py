import random
from pic import hang
from words import words
lives = 6
chosen_word = random.choice(words)
word_len = len(chosen_word)
display = []
end = False
for _ in range(word_len):
    display.append("_")
print(f"{' '.join(display)}")

while not end:
    letter = input("Guess a letter: ").lower()
    if letter in display:
        print("Already chosen.")
    else:
        c = 0
        for pos in range(word_len):
            if chosen_word[pos] == letter:
                display[pos] = letter
                if c == 0:
                    print(f"Correct, {letter} is in the word.")
                    c += 1
        print(f"{' '.join(display)}")
        if letter not in chosen_word:
            lives -= 1
            print(hang[lives])
            print(f"Wrong, down by one live , remains {lives} lives.")
            if lives == 0:
                print("You loss.")
                end = True
        if "_" not in display:
            end = True
            print("You won")
    print()
