t = input('Enter the text: ')
p = input('Enter the pattern: ')

# TODO 1: Calculate the bad match Table
bad_match_table = {}
for i in range(len(p)):
    if i == len(p)-1:
        bad_match_table[p[i]] = len(p)
    else:
        bad_match_table[p[i]] = len(p)-i-1

bad_match_table['*'] = len(p)
print('BAD MATCH TABLE VALUES:')
for key, value in bad_match_table.items():
    print(key, '=', value)

print('Doing Search\n--------------------')
# TODO 2: Do search
pos = len(p)-1
p_pos = len(p)-1
val = 0
matched = 0
while pos < len(t):
    print('T: ', t)
    print('P: ', '_'*val+p)

    # TODO 3: move the matching pos if matched
    if p[p_pos] == t[pos]:
        print(f'Matched : {p[p_pos]} and {t[pos]}')
        matched += 1
        pos -= 1
        p_pos -= 1
        if p_pos == -1:
            print('complete MATCH at position: ', pos+matched)
            break

    # TODO 4: if unmatched, search the bad match table and move n positions
    elif t[pos+matched] in bad_match_table:
        print(f'Mismatched : {p[p_pos]} and {t[pos]}')
        val += bad_match_table[t[pos+matched]]
        print(f'Moving {bad_match_table[t[pos+matched]]} positions')
        pos += (bad_match_table[t[pos+matched]]+matched)
        matched = 0
        p_pos = len(p)-1

    # TODO 5: if unmatched and letter not present in p, move len(p) positions
    else:
        print(f'Mismatched : {p[p_pos]} and {t[pos]}')
        matched = 0
        print(f'Moving {len(p)} positions, since {t[pos]} not present in {p}')
        val += len(p)
        pos += len(p)
        p_pos = len(p)-1
    print('-------------')

if pos >= len(t):
    print(f'{p} not found in {t}')

