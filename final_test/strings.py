# 5.	Задача консенсуса DNA ридов
# При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
# Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка,
# в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях.
# Т.е. для строк
# ATTA
# ACTA
# AGCA
# ACAA
# консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т, в четвертой – снова А).
# Для входного списка из N строк одинаковой длины построить консенсус-строку.

def consensus_string(strings: list) -> str:
    # result string
    string_ = [" " for _ in range(len(strings[0]))]
    # put letters into a special temp list
    letter_list = []
    for i in range(len(strings[0])):
        i_letters = []
        for str_ in strings:
            i_letters.append(str_[i])
        letter_list.append(i_letters)
    # print(letter_list)
    j = 0
    # count frequency
    for letters in letter_list:
        freq = 0
        for l in letters:
            # count number of each letters
            num = letters.count(l)
            if num > freq:
                freq = num
                string_[j] = l
                # check if all letters are the same
                if num == len(letters):
                    break
        j += 1 # next

    return "".join(string_)


if __name__ == '__main__':

    str_lst = [
        'ATTA',
        'ACTA',
        'AGCA',
        'ACAA',
    ]

    print("Array:", str_lst)
    print("Consensus_string:", consensus_string(str_lst))

    str_lst = [
        'ATTA',
        'ATTA',
        'ATTA',
        'ATTA',
        'ATTA',
        'ATTA',
        'ATTA'
    ]
    print("Array:", str_lst)
    print("Consensus_string:", consensus_string(str_lst))

    str_lst = [
        'ACTA',
        'ATTA'
    ]
    print("Array:", str_lst)
    print("Consensus_string:", consensus_string(str_lst))
