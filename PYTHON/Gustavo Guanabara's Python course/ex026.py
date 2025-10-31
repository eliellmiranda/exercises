# Write a program that reads a sentence from the keyboard and shows:
# - how many times the letter 'a' appears
# - the position where it appears the first time
# - the position where it appears the last time

phrase = str(input('Enter a sentence: ')).lower().strip()

print('The letter "A" appears {} time(s).'.format(phrase.count('a')))
print('The first "A" appears at position {}.'.format(phrase.find('a') + 1))
print('The last "A" appears at position {}.'.format(phrase.rfind('a') + 1))
