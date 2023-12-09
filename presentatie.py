from helper import som

def presenteer(mijn_dict, totaal):
  
    for item, bedrag in mijn_dict.items():
        print(f'{item} : {bedrag} euro')

    print("==========================")
    print(f'totaal : {totaal} euro')

mijn_dict = {"vis": 10, "vlees": 25, "overig": 15}

print (presenteer(mijn_dict, som(mijn_dict)))
