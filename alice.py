filename = ['book1.txt','book2.txt','book3.txt']
def count_words(filename):
    try:
        with open(filename) as f_object:
            contents=f_object.read();

    except FileNotFoundError:
        print("file name:"+filename)
        print("status:Unavailable" )
    else:
        words=contents.split()
        num_words=len(words)
        print("The file"+filename+"has about "+str(num_words)+" words.")
for book in filename:
    count_words(book)
