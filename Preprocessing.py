from string import punctuation
import codecs

punctuation = set(punctuation)
punctuation.discard('[')
punctuation.discard("]")
punctuation.discard(':')
punctuation.discard('*')
punctuation.discard(',')
punctuation.discard('.')
punctuation.discard(r'%')
punctuation.discard(';')
punctuation.add('"')


def preproces(file_path):
    f = codecs.open(file_path, 'r', 'utf-8')
    raw_data = f.read()
    mid_processed_data = raw_data.split('\n')
    result = ''
    for line in mid_processed_data:
        try:
            line = line[6:]
            i = 0
            while line[i] != '[':
                i = i + 1
            j = i
            while line[j] != ':':
                j = j + 1
            line = (line[:i] + line[j:].lower())
            result = result + line + '\n'
        except IndexError:
            continue

        f.close()
    return result


if __name__ == '__main__':
    data = preproces(r"C:\Users\Bartoszek\Desktop\TaernTradeHistory\21.01.17.txt")
    f = codecs.open(r"C:\Users\Bartoszek\Desktop\TaernTradeHistory\procesed21.01.17.txt", "w", 'utf-8')
    f.write(data)
    f.close()
