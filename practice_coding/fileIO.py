from typing import TextIO
from practice_coding.data import file_practice
def proccess_file(f: TextIO) -> int:
    answer = 0
    # step 1) Processing each line
    for line in f.readlines():
        # step 2) Skipping any comments
        if line.startswith("#"):
            continue
        # step 3) Skipping any more comments
        new_line = line.split("#")[0].strip() # strip 을 써서 양옆의 빈 공간 없애주기

        # step 4) spliting lines with .    
        # Note -> the last element will be empty
        valid_numbers = new_line.split(".")
        for element in valid_numbers:
            # check if any element is empty
            if element:
                num = int(element.strip())
                if num > answer:
                    answer = num

    return answer

def biggest_number(input_text):
    with open(input_text, 'r', encoding = 'utf-8') as f:
        answer = proccess_file(f)
        print(answer)


if __name__ == "__main__":
    biggest_number('file_practice.txt')