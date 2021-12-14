import time
import manganelo
import json
def scan(nurl, chaps):
    manga = manganelo.get_story_page(url = nurl)
    new_chaps = manga.chapter_list()

    # I don't like this, but whatever it works
    # If future me wonders what it is, basically new_chaps by default is a "manganelo.chapter" object
    for i, chap in enumerate(new_chaps):
        new_chaps[i] = chap.title
    

    if chaps == "":
        print("New Manga!!!")
        print("Adding %s to your library" %(manga.title))
        print("New Chapter: ", nurl)
        return new_chaps
    if new_chaps == chaps:
        return new_chaps
    print("New chapter: ", nurl)
    return new_chaps
    

def main():
    init_time = 0
    chapter_list = []
    while True:
        #TODO add different source scanning (so scan as it is becomes scan_nelo)
        #TODO add different manga scanning
       
        manga_list = open("mangalist.txt", "r")

        manga_list = (manga_list.read()).split()

        # Basically makes chapter_list the same length as manga_list, using the blank string as an indicator
        # that there is a newly added manga to the list
        if len(chapter_list) != len(manga_list):
            for i in range(len(manga_list) - len(chapter_list), len(manga_list) + 1):
                chapter_list.append('')

        for i, manga in enumerate(manga_list):
            chapter_list[i] = scan(manga, chapter_list[i])
            #TODO add JSON/Class support for scan

        time.sleep(15)    

main()
