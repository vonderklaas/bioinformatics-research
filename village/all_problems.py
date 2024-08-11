# problem 1
# import this

# problem 2
# a = 827
# b = 899
# result = a**2 + b**2
# print(result)

# problem 3
# str = 'ksE5TNnDH4Ts7DZ1QxxhXmRBVVloCCpK52b3GghmipZ6gcfPoCPratincolad4oxVkW1Yh4EjoZpoi7lPWbXQpeoBeTASC0SesqP7P1tZHyRleiuQbYGLEJ8uP082tto0hTaPO1UkESAwAtyOOqbftsz5MJQia6ySLjSiguanaaBjyLa6XmmNia5Dg791PpmJ.'
# word_one_start_pos = 50
# word_one_end_pos = 59

# word_two_start_pos = 164
# word_two_end_pos = 169

# print(f'{str[word_one_start_pos:word_one_end_pos + 1]} {str[word_two_start_pos:word_two_end_pos + 1]}')

# problem 4

# a = 4369
# b = 8716
# sum = 0;

# for x in range(a, b):
#     # print(x)
#     if x % 2 != 0:
#         sum += x

# print('sum', sum)

# problem 5
# output_file = []

# with open('./input.txt', 'r') as file:
#     # print(len(file.readlines()))
#     output_file = [line for pos, line in enumerate(file.readlines()) if pos % 2 != 0]

# print(output_file)

# with open('./input.txt', 'w') as file:
#     file.write(''.join([line for line in output_file]))

# problem 6

str = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'

word_count_dict = {}

for word in str.split(' '):
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1;

for key, value in word_count_dict.items():
    print(key, value)