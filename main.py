import os


def get_data(folder_name):
    global file1_data, emails, file2_data, instagram
    title_counter = 0
    submitter_counter = 0
    email_counter = 0
    credit = {}
    names = []

    folder_name = folder_name.lower()
    if 'повтор' in folder_name or 'вне' in folder_name:
        append_file3 = False
    else:
        append_file3 = True

    with open('credits.txt', 'r', encoding='utf-8') as file:
        info = file.readlines()

        for i in range(len(info)):
            if 'Title: ' in info[i] and title_counter == 0:
                title = info[i].replace('Title: ', '').strip()
                title_counter = 1
            if 'Submitter: ' in info[i] and submitter_counter == 0:
                submitter = info[i].replace('Submitter: ', '').strip()
                submitter_counter = 1
            if 'Email: ' in info[i] and email_counter == 0:
                email = info[i].replace('Email: ', '').strip()
                email_counter = 1
            if 'Submission URL: ' in info[i]:
                start = i + 1
                break

        line = info[start]
        while line == '\n':
            start += 1
            line = info[start]

        credit_key = ''
        credit_value = ''
        while line != '\n':
            line = info[start]
            if line[0] != ' ':
                credit_key = line.strip()
                ind = credit_key.find(': ')
                name = credit_key[ind + 1:].strip()
                if name not in names:
                    names.append(name)
            if 'IG: ' in line:
                credit_value = '@' + line.replace('IG: ', '').strip()
                if (append_file3 is True) and (credit_value not in instagram):
                    instagram.append(credit_value + '\n')
            if info[start + 1][0] != ' ' or info[start + 1] == '\n':
                credit[credit_key] = credit_value
                credit_key = ''
                credit_value = ''

            start += 1

        sorted_credit = sorted(credit, key=lambda value: submitter not in value)
        file2_data.append(title + '\n')
        for person in sorted_credit:
            res = person + ' ' + credit[person] + '\n'
            file2_data.append(res)
        file2_data.append('\n\n')

        if append_file3:
            title_names.append(title + ': ' + ', '.join(names[:-1]) + '\n')

        if append_file3:
            emails.append(email + '\n')
        title_submitter = submitter + ':\n' + title + '\n\n\n'
        file1_data.append(title_submitter)


emails = []
instagram = []
title_names = []
file1_data = []
file2_data = []
file_error = False


os.chdir('folders')
dirs = os.listdir()


for c in dirs:
    try:
        os.chdir(c)
    except:
        pass
    else:
        try:
            get_data(c)
        except:
            cred = os.listdir()
            if not 'credits.txt' in cred:
                print(f'!!!Возникла ошибка!!!\n'
                      f'В папке "{c}" не обнаружен файл "credits.txt".\n'
                      f'Проверьте название файла и повторите попытку.')
            else:
                print(f"!!!Возникла ошибка в ходе считывания файла!!!")
            file_error = True
            os.chdir('..')
            break

        os.chdir('..')


if not file_error:
    with open('file1.txt', 'w', encoding='utf-8') as file:
        file.writelines(file1_data)

    with open('file2.txt', 'w', encoding='utf-8') as file:
        file.writelines(file2_data)

    with open('file3.txt', 'w', encoding='utf-8') as file:
        file.writelines(title_names)
        file.write('\n\n')
        file.writelines(emails)
        file.write('\n\n')
        file.writelines(instagram)

    print("Программа успешно отработала")
