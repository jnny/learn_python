# a broken work in progress:

import bs4, requests

def getOaklandEvictionSched(pdfURL):
    res = requests.get(pdfURL)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
#    elems = soup.select('html body.overflow-x-hidden div.page-holder main section.bg-white.relative.z-0 div.container div a.btn')
#    return elems[0].text    

    for link in soup.find_all(class_="btn"):
        print(link.get('href'))

sched = getOaklandEvictionSched('https://www.oaklandca.gov/documents/homeless-encampment-clean-up-schedule')

print('The schedule is here: ' + sched)
