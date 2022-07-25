# 'Github rest api' kullanilarak yapilmis bir programdir.
# user hakkinda bilgiler alan ve repo olusturacak olan bir 
# python kodudur.

import requests, os, time, json

class Github:
    # Her nesne orneklemede, bu url olusturulacaktir.
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token   = "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"
    
    # Verilen baglantidaki kullanicinin bilgilerini ceken metod.
    def getUser(self, username):
        response = requests.get(self.api_url + "/users/" + username)
        return response.json()
    
    # Depolari ceken metod.
    def getRepositories(self, username):
        response = requests.get(self.api_url + "/users/" + username + "/repos")
        return response.json()
    
    def createRepository(self, name):
        response = requests.post(self.api_url + "/user/repos?access_token=" + self.token, json={
            "name"        : name,
            "description" : "This is my first repository",
            "homepage"    : "https://github.com",
            "private"     : False,
            "has_issues"  : True,
            "has_projects": True,
            "has_wiki"    : True
        })
        return response.json()

github = Github()

menu = """
1- Find User
2- Get Repository
3- Create Repository
4- Exit

Secim: """

while True:
    _ = os.system("cls")
    secim = input(menu)

    _ = os.system("cls")

    if secim == "4":
        _ = os.system("cls")
        print("Program kapatiliyor...")
        time.sleep(1)
        break
    else:
        if secim == "1":           
            usrName = input("User name: ")
            result  = github.getUser(usrName)
            text    = f"""
            ***********************************************************
            Name        :  {result['name']}
            Github      :  {result['html_url']}
            Public_repos:  {result['public_repos']}
            Location    :  {result['location']}
            Bio         :  {result['bio']}
            Following   :  {result['following']}
            Followers   :  {result['followers']}
            Created_at  :  {result['created_at']}
            ***********************************************************
            """
            _ = os.system("cls")
            print(text)
            _ = input("\nDevam Etmek Icin Enter tusuna basiniz...")            
        elif secim == "2":
            usrName = input("User Name: ")
            result = github.getRepositories(usrName)

            
            # ilgili kisinin, depolarini tek tek ekrana yazdirir.
            _ = os.system("cls")
            if (result):
                print(f"Depo Sahibi: {result[0]['owner']['login']}".center(50,"*"))
                for repo in result:
                    print(repo['name'])            
                print("*****" * 10)
            else:
                print("Herhangi bir oge yoktur !!")
            
            _ = input("\nDevam Etmek Icin Enter tusuna basiniz...")   
        elif secim == "3":
            print("Uzerinde Calisiliyor...")
            _ = input("\nDevam Etmek Icin Enter tusuna basiniz...")  
            # name = input("Repository name: ")
            # result = github.createRepository(name)
            # print(result)
        else:
            print("Yanlis bir secim !!")