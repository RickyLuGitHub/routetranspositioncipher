def get_str_ls(s, r, c):
    s = s.upper()
    s1 = ''
    for a in s:
        if a.isalnum():
            s1 += a
    s = s1
    if len(s) != r * c:
        s += 'X' * (r*c - len(s))
    return [list(s[i*c:(i+1)*c]) for i in range(r)]

def encrypt(s, c, r, clockwise=True):
    from math import ceil

    grid = get_str_ls(s, r, c)
    res_s = ''

    if clockwise:
        for i in range(ceil(r / 2)):
            try:
                for ls in grid:
                    res_s += ls.pop()

                for a in grid[-1][::-1]:
                    res_s += a
                grid.pop()

                for ls in grid[::-1]:
                    res_s += ls.pop(0)

                for a in grid[0]:
                    res_s += a
                grid.pop(0)
            except Exception:
                pass

            # pprint(grid)

    else:
        for i in range(ceil(r / 2)):
            try:
                for a in grid[0][::-1]:
                    res_s += a
                grid.pop(0)

                for ls in grid:
                    res_s += ls.pop(0)

                for a in grid[-1]:
                    res_s += a
                grid.pop()

                for ls in grid[::-1]:
                    res_s += ls.pop()
            except Exception:
                pass

    return res_s


# "WE ARE DISCOVERED. FLEE AT ONCE" (9, 3) clockwise
s1 = encrypt('WE ARE DISCOVERED. FLEE AT ONCE', 9, 3, True)
s1a = 'CEXXECNOTAEOWEAREDISLFDEREV'
print(s1 == s1a)

# "why is this professor so boring omg" (6, 5) counter-clockwise
s3 = encrypt('why is this professor so boring omg', 6, 5, False)
s3a = 'TSIYHWHFSNGOMGXIRORPSIEOBOROSS'
print(s3 == s3a)

# "Solving challenges on r/dailyprogrammer is so much fun!!" (8, 6) counter-clockwise
s4 = encrypt('Solving challenges on r/dailyprogrammer is so much fun!!', 8, 6, False)
s4a = 'CGNIVLOSHSYMUCHFUNXXMMLEGNELLAOPERISSOAIADRNROGR'
print(s4 == s4a)

# "For lunch let's have peanut-butter and bologna sandwiches" (4, 12) clockwise
s5 = encrypt('For lunch let\'s have peanut-butter and bologna sandwiches', 4, 12, True)
s5a = 'LHSENURBGAISEHCNNOATUPHLUFORCTVABEDOSWDALNTTEAEN'
print(s5 == s5a)

# "I've even witnessed a grown man satisfy a camel" (9,5) clockwise
s6 = encrypt('I\'ve even witnessed a grown man satisfy a camel', 9, 5, True)
s6a = 'IGAMXXXXXXXLETRTIVEEVENWASACAYFSIONESSEDNAMNW'
print(s6 == s6a)

# "Why does it say paper jam when there is no paper jam?" (3, 14) counter-clockwise
s7 = encrypt('Why does it say paper jam when there is no paper jam?', 3, 14, False)
s7a = 'YHWDSSPEAHTRSPEAMXJPOIENWJPYTEOIAARMEHENAR'
print(s7 == s7a)
