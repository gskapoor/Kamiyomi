import datetime
import manganelo

def scan(url, chaps = False):
    manga = manganelo.MangaInfo(url, threaded=False)
    new_chaps = manga.results.chapters
    if chaps == False:
        print("New Manga!!!")
        print("Adding ", manga.results.title, " to your library")
        print("New Chapter: ", url)
        return new_chaps
    if new_chaps == chaps:
        return
    print("New chapter: ", url);
    return new_chaps
    

def main():
    while True:
        scan("https://readmanganato.com/manga-ng952689")
            

main()
