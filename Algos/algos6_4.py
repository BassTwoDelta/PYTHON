# def Acronyms(phraseInput):

# phrase = "there's no free lunch - gotta pay yer way"
# phrase2 = "Live from New York, it's Saturday Night!"

# phrase_split = phrase.split()
# phrase2_split = phrase2.split()

# acronym = ""
# acronym2 = ""

# for i in phrase_split:
# #     acronym = acronym + i[0].upper()

# # for i in phrase2_split: 
# #     acronym2 = acronym2 +i[0].upper()

def Acronyms(phraseInput): 
    acronym = ""
    phrase_split = phraseInput.split()

    for i in phrase_split:
        acronym = acronym + i[0].upper()

    print(acronym)

Acronyms("there's no free lunch - gotta pay yer way")
Acronyms("Live from New York - It's Saturday Night")


