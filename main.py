def main():
    print(show_result(count_word(request_question())))

def show_result(count):
    return f"Interesting! you do show your thinking in only {count} words!"

def count_word(string):
    list = string.split()
    count = 0
    for x in list:
        count += 1
    return count

def request_question():
    string = input("Enter some thinking: ")
    return string;

if __name__ == '__main__':
    main()