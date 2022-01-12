# Author JRI 1/6/22

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"],
["Aiden", "Ian", "Colin" "Tim", "Cam"],
["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

for x in rows:
    for name in x:
        if name == "James":
            name += "'"
        else:
            name += "'s" 
        print(name)
