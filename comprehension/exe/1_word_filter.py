# some_text = input().split()
# even_words_len = ([x for x in some_text if len(x) % 2 == 0])
# print(*even_words_len, sep='\n')


print(*[x for x in input().split() if len(x) % 2 == 0], sep='\n')
