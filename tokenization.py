def subword_tokenizer(word):
    subwords = []
    for i in range(len(word)):
        subwords.append(word[:i+1])
    return subwords
print(subword_tokenizer("hello"))