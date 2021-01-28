#import modules
from bs4 import BeautifulSoup 
from functions.daterange import dateRange

def makeMail(drum, loop):
    #get email template bs4
    template = open('email.html')
    soup = BeautifulSoup(template.read(), "html.parser")

    #find template
    article_template = soup.find('div', attrs={'class':'bg'})

    #before template and after template
    html_start = str(soup)[:str(soup).find(str(article_template))]
    html_end = str(soup)[str(soup).find(str(article_template))+len(str(article_template)):]
    html_start = html_start.replace('\n','')
    html_end = html_end.replace('\n','')
    
    #get date range
    date = dateRange()
    
    #output
    output = "\n" + html_start + """<div class="bg">""" + "<h1>Reddit Kits ("+ date + ")</h1>" + """<div class="list">\n""" + "<hr>\n<h2>DrumKits 🥁</h2>\n<ul>\n" + drum + "\n</ul>\n<hr>\n<h2>LoopKits 🔁</h2>\n<ul>\n" + loop + "\n</ul>\n</div>\n" + html_end
    return output
