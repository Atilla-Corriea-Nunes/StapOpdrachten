#InternetVerbindingSelectie
connectionType = input("Welke verbinding wilt U gebruiken [4G, 5G, Wifi open]: ")

if connectionType == "4G":
    print(f"U bent verbonden via {connectionType}.")
elif connectionType == "5G":
    print(f"U bent verbonden via {connectionType}.")
elif connectionType == "Wifi open":
    warn = input("U heeft de voor de Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.")
    if warn == "ja":
        print(f"U bent verbonden via {connectionType}.")
    else:
        print("U bent niet verbonden!")
else:
    print("Onbekende invoer, er wordt geen verbinding tot stand gebracht.")
