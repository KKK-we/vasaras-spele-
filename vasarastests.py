# Mans vasaras tests
# Autors: (Kristers Lapiņš)

questions = [
    {
        "jaut": "1. Ko es darīju daudz šovasar?",
        "atb": ["a) Atpūtos", "b) Strādāju", "c) Gulēju"],
        "pareiza": "b"
    },
    {
        "jaut": "2. Kur es devos izklaidēties?",
        "atb": ["a) Uz koncertiem", "b) Uz muzejiem", "c) Uz bibliotēku"],
        "pareiza": "a"
    },
    {
        "jaut": "3. Ko es darīju sporta nolūkā?",
        "atb": ["a) Skrēju maratonu", "b) Gāju uz treniņiem", "c) Spēlēju šahu"],
        "pareiza": "b"
    },
    {
        "jaut": "4. Kur es bieži pavadīju laiku ar draugiem?",
        "atb": ["a) Mājās pie datora", "b) Ārā", "c) Skolā"],
        "pareiza": "b"
    },
    {
        "jaut": "5. Ko es nopirku šovasar?",
        "atb": ["a) Velosipēdu", "b) Mašīnu", "c) Motociklu"],
        "pareiza": "b"
    },
    {
        "jaut": "6. Ar ko saistītas manas brīvā laika aktivitātes?",
        "atb": ["a) Darbu un draugiem", "b) Ziemassvētkiem", "c) Slēpošanu"],
        "pareiza": "a"
    },
    {
        "jaut": "7. Kāds bija manas vasaras lielākais pirkums?",
        "atb": ["a) Jauns dators", "b) Mašīna", "c) Telefons"],
        "pareiza": "b"
    },
    {
        "jaut": "8. Kāds bija viens no priecīgākajiem notikumiem?",
        "atb": ["a) Koncerti", "b) Eksāmeni", "c) Ziema"],
        "pareiza": "a"
    },
    {
        "jaut": "9. Kā es uzturēju sportisku formu?",
        "atb": ["a) Ejot uz treniņiem", "b) Ēdot saldējumu", "c) Gulšņājot"],
        "pareiza": "a"
    },
    {
        "jaut": "10. Kāda bija mana vasara kopumā?",
        "atb": ["a) Aktīva", "b) Garlaicīga", "c) Neatceros"],
        "pareiza": "a"
    }
]

punkti = 0

print("Sveiks! Atbildi uz jautājumiem par manu vasaru.\n")

for q in questions:
    print(q["jaut"])
    for a in q["atb"]:
        print(a)
    atbilde = input("Tava atbilde (a/b/c): ").lower()
    if atbilde == q["pareiza"]:
        print("Pareizi!\n")
        punkti += 1
    else:
        print("Nepareizi! Pareizā atbilde bija:", q["pareiza"], "\n")

print("Tests pabeigts!")
print("Tavi punkti:", punkti, "no", len(questions))
