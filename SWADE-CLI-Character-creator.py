#Haven't added races or anything btw

#global predefined variables needed later
attributePoints=5 #points to spend on attributes
skillPoints=12 #how many points to spend on skills
hindrancePoints=0 #determines how much extra points for other catergories, dependant on how many hindrances chosen, max of 4.
edgePoints=1 #normally 0 but assumed to be a human will change later maybe

attributes= { #these are the attributes which allow derived traits, determine skills, and enable certain edges to be taken
  "Agility" : 4,
  "Smarts" : 4,
  "Spirit" : 4,
  "Strength" : 4,
  "Vigor" : 4
}

skills= { #these are the skills, core skills get a value of 4 and others have a value of 2
  "Academics" : 2,
  "Athletics" : 4,
  "Battle" : 2,
  "Boating" : 2,
  "Common Knowledge" : 4,
  "Driving" : 2,
  "Electronics" : 2,
  "Fighting" : 2,
  "Gambling" : 2,
  "Hacking" : 2,
  "Healing" : 2,
  "Intimidation" : 2,
  "Notice" : 4,
  "Occult" : 2,
  "Performance" : 2,
  "Persuasion" : 4,
  "Piloting" : 2,
  "Repair" : 2,
  "Research" : 2,
  "Riding" : 2,
  "Science" : 2,
  "Shooting" : 2,
  "Stealth" : 4,
  "Survival" : 2,
  "Taunt" : 2,
  "Thievery" : 2
}

#naming character
print("Welcome to your Character Creation!")
name=input("Please name your character: ") #sets the name, eventually should write this to a file

print("\nAttributes, Skills, Hindrances, Edges, or Inventory")
decision=input("Where would you like to start: ")

#here we want a switch function to determine the choice made at the start
match decision:
  case "Attributes": #attribute raises here
    while attributePoints>0: #loops until attributes are spent

      # Get user descision on what to increase
      print() # Just give us some visual separation for each iteration
      # Do a confusing looking print statement for current allocations LoL
      print(', '.join([f"{key}: d{attributes[key]}" for key in attributes]))
 	  # Show how many points are left to spend
      print(f"You have {attributePoints} point{'' if attributePoints == 1 else 's'} left to spend")
      userAttributeInc = input("Choose to increase: ")

      # Ensure that the selected increase is a valid selection
      if userAttributeInc in attributes and attributes[userAttributeInc] + 2 <= 12:
        attributes[userAttributeInc] += 2 #increases the desired stat
        attributePoints -= 1 #decreases the while loop variable
      else:
        print("Pick a different attribute!")

    # Print all the attributes stored in the dict
    print(f"{name}'s atttributes are:", sep="")
    for key in attributes:
      print(f'\t{key}: d{attributes[key]}')
      #so we need a d before the key.
    print("\nSkills, Hindrances, Edges, or Inventory")
    decision=input("Where to now?") #********************************************This will not work*************** Needs to be fixed. Allow the match to be used multiple times basically.
  case "Skills": #skill raises here
    while skillPoints>0 #loops till enough skill points are spent
      
    

