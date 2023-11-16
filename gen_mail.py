import os
import re
def add_dot_to_name(name, domain):
    emails = []
    for i in range(1, len(name)):
        new_name = name[:i] + '.' + name[i:]
        email = new_name + '@' + domain
        emails.append(email)
    with open('add_dot_to_name.txt', 'w') as f:
        f.write('\n'.join(emails))
    return emails
def change_domain(name, domain, domain_list):
    emails = []
    for new_domain in domain_list:
        email = name + '@' + new_domain
        emails.append(email)
    with open('change_domain.txt', 'w') as f:
        f.write('\n'.join(emails))
    return emails
def add_website_to_name(name, domain, website_list):
    emails = []
    for website in website_list:
        email = name + '+' + website + '@' + domain
        emails.append(email)
    with open('add_website_to_name.txt', 'w') as f:
        f.write('\n'.join(emails))
    return emails
def add_dot_and_change_domain(name, domain, domain_list):
    emails = []
    for new_domain in domain_list:
        for i in range(1, len(name)):
            new_name = name[:i] + '.' + name[i:]
            email = new_name + '@' + new_domain
            emails.append(email)
    with open('add_dot_and_change_domain.txt', 'w') as f:
        f.write('\n'.join(emails))
    return emails
def add_dot_and_add_website(name, domain, website_list):
    emails = []
    for website in website_list:
        for i in range(1, len(name)):
            new_name = name[:i] + '.' + name[i:]
            email = new_name + '+' + website + '@' + domain
            emails.append(email)
    with open('add_dot_and_add_website.txt', 'w') as f:
        f.write('\n'.join(emails))
    return emails
def change_domain_and_add_website(name, domain, domain_list, website_list):
    emails = []
    for new_domain in domain_list:
        for website in website_list:
            email = name + '@' + new_domain
            email = email.replace(domain, website + '.' + domain)
            emails.append(email)
    with open('change_domain_and_add_website.txt', 'w') as f:
        f.write('\n'.join(emails))
    return emails
def add_dot_and_change_domain_and_add_website(name, domain, domain_list, website_list):
    emails = []
    for new_domain in domain_list:
        for website in website_list:
            for i in range(1, len(name)):
                new_name = name[:i] + '.' + name[i:]
                email = new_name + '+' + website + '@' + new_domain
                emails.append(email)
    with open('add_dot_and_change_domain_and_add_website.txt', 'w') as f:
        f.write('\n'.join(emails))
    return emails
def choose_option(name, domain, domain_list, website_list):
    while True:
        print("Chọn phương pháp thay đổi email:")
        print("1. Thêm dấu chấm vào tên email")
        print("2. Thay đổi tên miền")
        print("3. Thêm tên website vào tên email")
        print("4. Thêm dấu chấm vào tên email và thay đổi tên miền")
        print("5. Thêm dấu chấm vào tên email và thêm tên website")
        print("6. Thêm dấu chấm vào tên email, thay đổi tên miền và thêm tên website")
        print("7. Thay đổi tên miền và thêm tên website")
        choice = input("Nhập lựa chọn của bạn (1-7): ")
        if choice == '1':
            emails = add_dot_to_name(name, domain)
            break
        elif choice == '2':
            emails = change_domain(name, domain, domain_list)
            break
        elif choice == '3':
            emails = add_website_to_name(name, domain, website_list)
            break
        elif choice == '4':
            emails = add_dot_and_change_domain(name, domain, domain_list)
            break
        elif choice == '5':
            emails = add_dot_and_add_website(name, domain, website_list)
            break
        elif choice == '6':
            emails = add_dot_and_change_domain_and_add_website(name, domain, domain_list, website_list)
            break
        elif choice == '7':
            emails = change_domain_and_add_website(name, domain, domain_list, website_list)
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue
    print(f"{len(emails)} emails đã được tạo và lưu vào các file tương ứng.")
    return emails
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
def main():
    original_email = input("Nhập email gốc: ")
    if not is_valid_email(original_email):
        print("Email không hợp lệ. Vui lòng nhập lại email.")
        main()
    name, domain = original_email.split('@')
    domain_list = ['googlemail.com']
    website_list = ['facebook', 'twitter', 'instagram', 'linkedin', 'github', 'pinterest', 'tiktok', 'youtube', 'shoppee', 'lazada', 'zalo']
    while True:
        emails = choose_option(name, domain, domain_list, website_list)
        choice = input("Bạn có muốn tiếp tục thay đổi email vừa nhập không? (y/n): ")
        if choice.lower() == 'y':
            original_email = emails
        elif choice.lower() == 'n':
            change_email()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue
def change_email():
    while True:
        choice = input("Bạn có muốn thay đổi email không? (y/n): ")
        if choice.lower() == 'y':
            main()
        elif choice.lower() == 'n':
            exit()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            continue
main()