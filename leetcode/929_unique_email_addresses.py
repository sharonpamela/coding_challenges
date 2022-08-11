# Given an array of strings emails where we send one 
# email to each emails[i], return the number of different 
# addresses that actually receive mails.

# Input: emails = ["test.email+alex@leetcode.com",
# "test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and 
# "testemail@lee.tcode.com" actually receive mails.

def check_unique_emails(email_list):
    res = set()
    for e in email_list:
        email, domain = e.split("@")
        local = []
        for char in email:
            if char == "+":
                break
            if char == ".":
                continue 
            local.append(char)
        new_local = "".join(local)
        res.add(new_local+"@"+domain)
        print(res)
    return len(res)

email_list = ["test.email+alex@leetcode.com",
"test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
email_list = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
print(check_unique_emails(email_list))      