def answer(n):
    n = int(n)
    steps = 0

    while n > 1:
        # if n is even, divide by 2 using bit manipulation
        if n & 1 == 0:
            n >>= 1
        else:
            # Use bit manipulation to create as many 0 from LSB as possible
            n = (n - 1) if (n == 3 or n % 4 == 1) else (n + 1)

        steps += 1
    return steps

# _-_-_-_-_-_-_-_-_-_-_-_-TEST--CASES-_-_-_-_-_-_-_-_-_-_-_-_


a = 124480579411363943422977485485450829978158403576349485507396127987323092328068524587695005561434534623452345436346456353425362283769712245781118297614280332424240701048410620648401132628401374562794562558123463462235342526466804149296501029546541499918765438784295157088047123009825235235168758962399

print("*********")
print(answer(4))
print("*********")
print(answer(15))
print("*********")
print(answer(768))
print("^^^^^^^^^^^^^^")
print(answer(1235))
print("**********")
print(answer(65535))
print("=============")
print(answer(947712))
print("*********")
print(answer(17542149120))
print("*********")
print(answer(15755622182313818849280))
print("*********")
print(answer(a))


print(len(str(a)))
