# Author: Nicole Giron nqg5259@psu.edu
# GitHub ID: nicolegiron
def is_anagram(s1, s2):
  if sorted("".join(char for char in s1 if char.isalnum()).lower()) == sorted("".join(char for char in s2 if char.isalnum()).lower()):
    return True
  else:
    return False

def run():
  s1 = input("Enter a string: ")
  s2 = input("Enter a string: ")
  if is_anagram(s1, s2):
    print("anagram")
  else:
    print("not anagram")


if __name__ == "__main__":
  run()