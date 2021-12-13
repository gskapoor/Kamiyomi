import time
import manganelo
def scan(nurl, chaps):
    manga = manganelo.get_story_page(url = nurl)
    new_chaps = manga.chapter_list()
    if chaps == "":
        print("New Manga!!!")
        print("Adding %s to your library" %(manga.title))
        print("New Chapter: ", nurl)
        return new_chaps
    if new_chaps == chaps:
        return
    print("New chapter: ", nurl);
    return new_chaps
    

def main():
    init_time = 30
    while True:
        #TODO add different source scanning (so scan as it is becomes scan_nelo)
        #TODO add different manga scanning
       
        manga_list = open("mangalist.txt", "r")
        try:
            chapter_list = open("mangalist.txt","r")
        except:
            chapter_list = open("mangalist.txt", "w")
            chapter_list.close()
            chapter_list = open("mangalist.txt", "r")
        chapter_holder = chapter_list.readlines()

        #TODO fix the scanning or else I'll cry ;( (very sad)

        for i, manga in enumerate(manga_list):
            manga = manga.strip()
            chapter_holder[i] = scan(manga, chapter_holder[i])


        time.sleep(15)    

main()
