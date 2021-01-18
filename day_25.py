
#key_1 = 5764801
#key_2 = 17807724
key_1 = 15628416
key_2 = 11161639


def loop(val, subject_number):
    val *= subject_number
    val = val % 20201227
    return val


def find_loop_size(key):
    loop_size = 0
    val = 1
    while not val == key:
        val = loop(val, 7)
        loop_size += 1
    return loop_size


def part_one():
    loop_size = find_loop_size(key_1)
    subject_number = key_2
    encrypt_key = 1
    for i in range(loop_size):
        encrypt_key = loop(encrypt_key, subject_number)
    print(encrypt_key)


part_one()

