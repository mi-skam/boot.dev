
def count_words(str):
  return len(str.split())

def count_chars(str):
  count = {}
  for c in str.lower():
    count[c] = 1 if c not in count else count[c]+1
  return count

def toList(dict):
  list = []
  for key, value in dict.items():
    list.append({"name": key, "num": value})
  return list

def sort_on(dict):
  return dict["num"]

def print_report(words, chars):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{words} words found in the document")
  for c in chars:
    if c['name'].isalpha():
      print(f"The '{c['name']}' character was found {c['num']} times")
  print("--- End report ---")

with open('frankenstein.txt') as f:
  content = f.read()
  words_count = count_words(content)
  chars_count = toList(count_chars(content))
  chars_count.sort(reverse=True, key=sort_on)
  print_report(words_count, chars_count)

