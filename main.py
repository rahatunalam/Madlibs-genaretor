story= open("story.txt",'r')
f=story.read()
story.close()
#print(f)

words = set()
start_of_word =-1

t_start = "<"
t_end = ">"

for i, char in enumerate(f):
    if char == t_start:
        start_of_word = i

    if char == t_end and start_of_word != -1:
        word = f[start_of_word:i+1]
        words.add(word)
        start_of_word =-1

print(words)
answers ={}
for word in words:
    answer = input("Enter a word for"+word+":")
    answers[word]=answer

for word in words:
    f=f.replace(word,answers[word])

print(f)