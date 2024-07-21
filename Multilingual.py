Num_Set = "1 2 3 4 5 6 7 8 9"
i = 1
LangSpeakTotal = set()
LangTypes_Set = []
PeopleNum = int(input("How many people are there? (1-9): "))
for num in Num_Set.split(" ", PeopleNum - 1):
    LangSpeak = int(input(f"Person {i}, how many languages can you speak? "))
    LangSpeakTotal.add(LangSpeak)
    for _ in range(LangSpeak):
        LangType = input("Which language(s) can you speak? ")
        LangTypes_Set.append(LangType)
    i += 1
LangType_Count = {lang: LangTypes_Set.count(lang) for lang in set(LangTypes_Set)}
Languages_Everyone_Speaks = [lang for lang, count in LangType_Count.items() if count == PeopleNum]
LangSpeakTotal = len(Languages_Everyone_Speaks)
print(f"Number of Languages Everyone Speaks: {LangSpeakTotal}")
print("Languages spoken by everyone: ", Languages_Everyone_Speaks)
TotalLanguages_Set = set(LangTypes_Set)
print(f"Total Language(s) Spoken in The Group: {len(TotalLanguages_Set)}")
print(f"Language(s) Spoken: {TotalLanguages_Set}")
