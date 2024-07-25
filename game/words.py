words = open("game/words.txt").readlines()

def is_a_word(s):
    try:
        words.index(s + "\n")
        return True
    except ValueError:
        return False
