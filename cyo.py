print ("Hello! You are a fish who needs help going home.")
first = input("Should you go left or right?")
if first == "left":
    print("You decide to go left and you meet a yellow fish. You ask the fish for help. The fish offers to help if you answer its riddle.")
    for tries in range(0,2):
        second = input("What walks on four legs in the morning, two legs at noon and three legs in the evening?")
        if second == "man":
            print("The fish says: 'Well done! Here are your directions' You make it home safely. Yay!")
            break
        elif (second != "man") and (tries < 1 ):
            print("Here's a hint: it is three letters.")
        else:
            print("The fish says: 'Wrong! I won't help you!' You decide to move on on your own. Then you encounter a crab who offers to lead you the way.")
            fourth = input("Do you follow the crab?")
            if fourth == "yes":
                print("You follow the crab and are led to a shark. The shark eats you and your journey ends. GAME OVER.")
                break
            else:
                print("You decide to go your own way and find your way home safely. Yay!")
                break
if first == "right":
    print("You decide to go right and you meet a red fish. You ask the fish for help. The fish offers to help if you answer its riddle.")
    for tries in range (0,2):
        third = input("What has a head, a tail, is brown, and has no legs? (oneword)")
        if third == "penny" :
            print("The fish says: 'Well done! Here are your directions.' You make it home safely. Yay!")
            break
        elif (third != "penny") and (tries < 1):
            print("Here's a hint:¢")
        else:
            print("The fish says: 'Wrong! I won't help you! You decide to go your own way. You encounter a shark. The shark eats you. GAME OVER")
        # if third == "penny" :
        #     print("The fish says: 'Well done! Here are your directions.' You make it home safely. Yay!")
        #     break
        # else:
        #     print("The fish says: 'Wrong! I won't help you! You decide to go your own way. You encounter a shark. The shark eats you. GAME OVER")




# Update this text to match your story.
# start = '''
# You wake up one morning and find that you aren't in your bed; you aren't even in your room.
'''
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''
"""
print(start)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if user_input == "left":
    print("You decide to go left and...") # Update to match your story.

    # Continue code to finish story.

elif user_input == "right":
    print("You choose to go right and ...") # Update to match your story.

    # Continue code to finish story.
"""
