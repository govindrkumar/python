#!/usr/bin/env python
# coding: utf-8

# In[6]:


#create a small adventure game where the player navigates through different rooms in a house. Each room can have different items, and the player can choose to pick up items, drop them, or look around.


# In[8]:


import time


# In[13]:


#main menu for starting game.
def display_menu():
    print("1. Play Game")
    time.sleep(1)
    print("2. Exit")


# In[20]:


#final villager congratulations
def village_celeb():
    print("All Villagers: Thanks for saving us Lord!")
    time.sleep(2)
    print("Happy Ending!")
    time.sleep(2)
    exit()


# In[19]:


#final killing of demon.
def final_kill_of_demon():
    print("The battle intensifies, both sides showing signs of fatigue. The hero, with one final push, gathers all strength for a powerful strike.")
    time.sleep(3)
    print("Hero: This is for every life you’ve taken! I will end your reign of terror!")
    time.sleep(1)
    print("No! This cannot be! I am eternal!", "\n[Attempts to shield itself but fails]")
    time.sleep(2)
    print("Demon Dies with a howling sound and blast!")
    print("Congratulations You Win!")
    village_celeb()



# In[16]:


#This block is connected with def place_story module and this is about war.
def fight_scene():
    print("Battle Field is Prepared!")
    tools = ["Sword","Bow&Arrow","Rock","Needle","Knife","God Power: 1 left"]
    time.sleep(2)
    print("Choose Option: ")
    print("1. Check Arsenal\n2. Storm toward Demon")
    t_final=input("Your Choice: ")
    if (t_final==1): #weapon checking ho rha hai fight se pahle
        print(tools)
    elif (t_final==2): #final battle ho rha hai
        print("Hero: Every time I stand back up, I’m stronger! You’ll never break my spirit!")
        time.sleep(2)
        print("Demon: Your spirit is weak! Watch as I crush your hopes!")
        print("Demon: You’re just a stepping stone in my path to chaos!")
        final_kill_of_demon()


# In[10]:


def place_story():
    if (a==1):
        print(f"thanks for coming our Hero {name}!")
        time.sleep(3)
        print("Save us from demon")
    elif (a==3):
        print("Enters Demon's Lair!")
        time.sleep(1)
        print("Demon appears!")
        print("Demon:- Who are you?")
        time.sleep(2)
        dialogue_1_output=input("You: ")
        print("Demon:- Foolish mortal! You think you can defeat me? I’ve devoured the souls of the bravest warriors!")
        time.sleep(1)
        print("Demon:- Hahahaaaaa!")
        dialogue_2_output=input("You: ")
        fight_scene()
    else:
        exit()


# In[4]:


#choosing input
def option_1():
    print("Welcome to The Quest of the Demon Slayer!")
    time.sleep(2)
    print("Characters:")
    print("1. Hero(You)\n2. The Demon\n3. Villagers\n\n")
    time.sleep(3)
    print("Story Starts! ")
    name = input("First tell your name: ")
    name_s = f"Welcome {name}"
    print(name_s)
    print("Places are:\n1. The Village Square\n2. The Forest of Shadows\n3. The Demon's Lair")
    place_story()


# In[12]:


def option_2():
    exit() #exit the program


# In[ ]:


def main():
    while True:
        display_menu()  # displays menu
        a = int(input("Choose option: "))  # move this inside the while loop
        if a == 1:
            option_1()
        elif a == 2:
            option_2()
        elif a == 3:
            print("Exiting...")
            break  # Exit the Gloop
        else:
            print("Invalid option, please try again.")


# In[ ]:


main()

