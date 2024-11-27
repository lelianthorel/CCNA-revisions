import requests
from bs4 import BeautifulSoup
import json

def find_question(ul):
    try:
        question = ul.find_previous_sibling('p').find('strong').text
    except:
        question = "Question non trouvé"

    return question

def find_index_answer(lis, ul):
    try:
        index_answer = [lis.index(ul.find('li', class_="correct_answer"))]
    except:
        print("Erreur lors de la détection de la réponse.")
        index_answer = None

    return  index_answer

URL = "https://ccnareponses.com/modules-14-16-concepts-de-routage-et-examen-de-configuration-reponses/"#input("Indiquez le lien  :")
page= requests.get(URL)
json_data = []

soup = BeautifulSoup(page.content, "html.parser")
content = soup.find('div', class_="thecontent")

uls = content.find_all("ul")
for ul in uls:
    lis = ul.find_all("li")
    choices = [li.text for li in lis]

    json_data.append({
        "question": find_question(ul),
        "choices": choices,
        "answers": find_index_answer(lis, ul)
    })

# Enregistrer le résultat dans un fichier JSON
with open('json/CCNA2/ccna14-16.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=3)
    
#test commit.