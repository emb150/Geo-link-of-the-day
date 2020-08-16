import bs4 as bs
import urllib.request

#links to the main Earth Science portal and retrieves soup
sauce = urllib.request.urlopen('https://en.wikipedia.org/wiki/Portal:Earth_sciences').read() 
soup = bs.BeautifulSoup(sauce, 'html5')

main_portal_list = []
#'Subcategories' header on https://en.wikipedia.org/wiki/Portal:Earth_sciences
for i in soup.find(class_= 'CategoryTreeTag').find(class_="CategoryTreeSection").find_all('a'):
    main_portal_list.append('http://wikipedia.org' + i.get('href'))

def get_pages(url):
    #creates new list to retrieve 'Pages in category' links under each 'Subcategories'
    pages_list = []
    try:
        sauce = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(sauce, 'html5')
        
        #for each item in the soup it finds the 'a' tag
        for i in soup.find(id="mw-pages").find(class_="mw-content-ltr").find_all('a'):
            #appends 'http://wikipedia.org' to make a proper URL and appends the 'href' attribute values
            pages_list.append('http://wikipedia.org' + i.get('href'))
            
    #adds an error handling if the URL isn't valid
    except:
        print('Oops, that wasn\'t a valid URL')
        
    return pages_list
    
    all_page_urls = []
#loops over the main_portal_list and webscrapes each link under the header 'Pages in category'
#link then gets passed into the function get_pages
for i in main_portal_list:
    pages = get_pages(i)
    #appends the newly found page to the blank list
    for page in pages:
        all_page_urls.append(page)
        
#opens the list of URLs in a textfile line by line
with open("/users/emily/downloads/GeoURLsFinal.txt","a") as textfile:
    #textfile.writelines(all_page_urls[:3] + '\n')
     for i in all_page_urls:
        textfile.write(i + '\n')
        
