import random
lettres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','#','$','%','&','(',')','*','+']

print("Bienvenue dans le generateur de mot de passe !")
n_lettres = int(input("Entrer la taille de votre mot de passe !"))

password_list = []

for i in range(1,n_lettres+1):
    char = random.choice(lettres)
    password_list.append(char)

random.shuffle(password_list)

password = ""
for char in password_list:
    password = password + char

print (password)