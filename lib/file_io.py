def write_file(file_name, file_content):
    print(f"Writing to file: {file_name}")
    with open(f'{file_name}.txt' , mode='w', encoding='utf-8') as file1:
        file1.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as file1:
        file1.write(append_content)


def read_file(file_name):
    with open(file_name, mode ='r',encoding = 'utf-8') as file1:
        content = file1.read()
    return content
