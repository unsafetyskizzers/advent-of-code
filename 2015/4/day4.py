import hashlib
file = open("input.txt", "r")

answer_hash = hashlib.md5()
hash_inc = -1
input_code = file.read()
file.close()

print(input_code)

while answer_hash.hexdigest()[:5] != "00000":
    hash_inc += 1
    answer_hash = hashlib.md5((input_code + str(hash_inc)).encode("utf-8"))
if answer_hash.hexdigest()[:5] == "00000":
    print("ANSWER FOUND for 5 zeroes:", hash_inc)
else:
    print("No answer found for 5 zeroes")

#start over for part 2
answer_hash = hashlib.md5()
hash_inc = -1

while answer_hash.hexdigest()[:6] != "000000":
    hash_inc += 1
    answer_hash = hashlib.md5((input_code + str(hash_inc)).encode("utf-8"))
if answer_hash.hexdigest()[:6] == "000000":
    print("ANSWER FOUND for 6 zeroes:", hash_inc)
else:
    print("No answer found for 6 zeroes")
