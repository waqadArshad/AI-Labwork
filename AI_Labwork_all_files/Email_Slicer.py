#
#
email = input("Enter your email: ")
# email = "waqadArshad2@gmail.com"
email_username = email[0:email.find('@'):1]
email_domain = email[email.find('@')+1:(len(email)):1]
print("Username is: " + email_username)
print("domain is: " + email_domain)
