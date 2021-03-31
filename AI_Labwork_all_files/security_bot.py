# Security bot.
guest2=['Aslam','Kaleem','Saleem khan','Carol','Micheal',
        'Chris johnson','John','Ferry','Ali','Falak sher','Akram kaleem',
        'Malik aslam','Aleem kaleem','Waqad','Faizyab']

guest=['aslam', 'Ali']
print("Hello I am Travis!")
str="The classroom is very very clean."
# guest.pop()
# guest.remove('aslam'.capitalize())
# guest.insert(3,'alm cheem'.upper())
# print(guest[0].split('a'))
# print(str.replace('very','vary'))
word = input("Please enter a word to find: ")
if(str.__contains__(word)):
    print(str[str.index(word):str.index(word)+len(word):1])
else:
    print("Not find")



# print(type(guest))
#
# while True:
#     # Asking user for his name and stripping all spaces and capitalizing it.
#     name = input("Please enter your name: ").strip().capitalize()
#     # check if the guest is invited or not
#     if name in guest:
#         print("Hello, Mr. {}! Welcome to the party.".format(name.title()))
#         while removeConsent!='y' or removeConsent!='n':
#             print("Hello, Mr. {}! Welcome to the party.".format(name.title()))
#             if removeConsent=='y':
#                 guest.remove(name)
#                 print("Mr. {}. You may leave now.".format(name))
#                 print(guest)
#             elif removeConsent=='n':
#                 print("Hello, Mr. {}! Welcome to the party.".format(name.title()))
#             else:
#                 print("Please enter a valid choice.")
#                 removeConsent = input("Would you like to be removed from the list (y/n)? ")
#         # guest2.remove(name)
#         # print(guest2)
#     else:
#         print("Sorry, You are not invited!")
#         addConsent = input("Would ou like me add you to the list (y/n)? ")
#         if addConsent=='y':
#             guest.append(name)
#             print("Hello, Mr. {}! Welcome to the party.".format(name.title()))
#             print(guest)
#         elif addConsent=='n':
#             print("Ok, Mr. {}".format(name.title()))
#         else:
#             print("Please enter a valid choice.")
