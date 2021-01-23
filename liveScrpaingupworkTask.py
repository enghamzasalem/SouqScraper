import requests
from bs4 import BeautifulSoup
for i in range(1,600):
  r = requests.post('https://www.escpalumni.org/annuaire/ajax/loadresult', data = {'page':i,'sort':'alpha_asc','change_filters':'0','request_id':'2069946bc99e2aa99a7189599375aaa2','annuaire_mode':'standard','annuaire_action':"",'annuaire_action_arg':"",'annuaire_appli':'','annuaire_as_no':''})
  #print(r.content)
  soup = BeautifulSoup(r.content,'html.parser')
  for link in soup.findAll('a'):
    if 'profil' in link.get('href'):
      print (link.get('href'))
