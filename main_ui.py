import actions



print("What do you want to do?")

for seq, action in enumerate(actions.PalActions):
    print(f"{seq+1}. {action.name} : {action.desc}")

input("Please select")
