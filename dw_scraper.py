from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


#Creating the web scraper function
def doodle_info():
    main_url = "https://doodle-world.fandom.com/wiki/Doodlepedia"

    main_request = Request(
        main_url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    main_page = urlopen(main_request).read().decode("UTF-8")

    m_soup = BeautifulSoup(main_page, "html.parser")

    #Declaring the variable which we'll loop through to get info on all doodles
    doodle_list = m_soup.find_all("table")[0].find_all("tbody")[0].find_all("tr")

    
    g_speed = 0
    fastest = "a"


    g_attack = 0
    p_strongest = "a"
    for doodle in doodle_list[1:]:
        name = doodle.find_all("td")[2].find_all("a")[0].getText()
        type1 = doodle.find_all("td")[3].find_all("a")[0]['title'].split()[0]
        try:
            type2 = doodle.find_all("td")[3].find_all("a")[1]['title'].split()[0]
        except:
            type2 = ""
        ref = doodle.find_all("td")[2].find_all("a")[0]['href']
        doodle_url = f"https://doodle-world.fandom.com{ref}"

        doodle_request = Request(
            doodle_url,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        doodle_page = urlopen(doodle_request).read().decode("UTF-8")

        d_soup = BeautifulSoup(doodle_page, "html.parser")

        awakened = False
        alt_form = False
        stat_change = True
        table_idx = 4
        
        if name == "Vigimantè" or name == "Sobbuoy":
            table_idx -= 1
        
        hp = d_soup.find_all("table", {"class": "article-table"})[table_idx].find_all("td")[3].find_all("b")[0].getText()
        attack = d_soup.find_all("table", {"class": "article-table"})[table_idx].find_all("td")[7].find_all("b")[0].getText()
        defense = d_soup.find_all("table", {"class": "article-table"})[table_idx].find_all("td")[11].find_all("b")[0].getText()
        m_attack = d_soup.find_all("table", {"class": "article-table"})[table_idx].find_all("td")[15].find_all("b")[0].getText()
        m_defense = d_soup.find_all("table", {"class": "article-table"})[table_idx].find_all("td")[19].find_all("b")[0].getText()
        speed = d_soup.find_all("table", {"class": "article-table"})[table_idx].find_all("td")[23].find_all("b")[0].getText()
        total = d_soup.find_all("table", {"class": "article-table"})[table_idx].find_all("td")[27].find_all("b")[0].getText()

        try:
            typeOfForm = d_soup.find_all("aside")[0].find_all("section")[1].find_all("table")[0].find_all("tr")[0].find_all("th")[1].getText().split()[0]

            if typeOfForm == "Awakened":
                awakened = True
            elif typeOfForm == "Alt":
                alt_form = True
            
            type1_a = d_soup.find_all("aside")[0].find_all("section")[1].find_all("table")[0].find_all("tr")[1].find_all("td")[1].find_all("a")[0]["title"]
            type2_a = d_soup.find_all("aside")[0].find_all("section")[1].find_all("table")[0].find_all("tr")[1].find_all("td")[1].find_all("a")[2]["title"]
            try:
                hp_a = d_soup.find_all("table", {"class": "article-table"})[table_idx+1].find_all("td")[3].find_all("b")[0].getText()
                attack_a = d_soup.find_all("table", {"class": "article-table"})[table_idx+1].find_all("td")[7].find_all("b")[0].getText()
                defense_a = d_soup.find_all("table", {"class": "article-table"})[table_idx+1].find_all("td")[11].find_all("b")[0].getText()
                m_attack_a = d_soup.find_all("table", {"class": "article-table"})[table_idx+1].find_all("td")[15].find_all("b")[0].getText()
                m_defense_a = d_soup.find_all("table", {"class": "article-table"})[table_idx+1].find_all("td")[19].find_all("b")[0].getText()
                speed_a = d_soup.find_all("table", {"class": "article-table"})[table_idx+1].find_all("td")[23].find_all("b")[0].getText()
                total_a = d_soup.find_all("table", {"class": "article-table"})[table_idx+1].find_all("td")[27].find_all("b")[0].getText()
            except:
                stat_change = False
        except:
            print("")
        if int(speed) > g_speed:
            g_speed = int(speed)
            fastest = fastest.replace(fastest, name)
        if int(attack) > g_attack:
            g_attack = int(attack)
            p_strongest = p_strongest.replace(p_strongest, name)
        if(type2 == ""):
            print(f"{name}: {type1} [{hp},{attack},{defense},{m_attack},{m_defense},{speed}]\nTotal: {total}\n")
        else:
            print(f"{name}: {type1}, {type2} [{hp},{attack},{defense},{m_attack},{m_defense},{speed}]\nTotal: {total}\n")
        if(awakened):
            print(f"A-{name}: {type1_a}, {type2_a} [{hp_a},{attack_a},{defense_a},{m_attack_a},{m_defense_a},{speed_a}]\nTotal: {total_a}\n")
        if(alt_form):
            if(stat_change):
                print(f"Alt form of {name}: {type1_a}, {type2_a} [{hp_a},{attack_a},{defense_a},{m_attack_a},{m_defense_a},{speed_a}]\nTotal: {total_a}\n")
            else:
                print(f"Alt form of {name}: {type1_a}, {type2_a}")
        
    print(f"The fastest doodle in this range is {fastest} with {g_speed} speed\nThe strongest doodle (physically) in this range is {p_strongest} with {g_attack} attack")

doodle_info()
connection.close()
