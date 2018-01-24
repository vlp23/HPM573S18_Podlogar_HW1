yours = ['yale', 'MIT', 'Berkley']
mine= ['rutgers', 'UCLA', 'Maryland']


ours1= yours + mine
print (ours1)

ours2= []
ours2.append(mine)
ours2.append(yours)
print (ours2)

yours[1]= 'Cornell'
print (yours)

print (ours1)
print(ours2)

# In ours1, adding the two lists together creates a variable containing all of the elements of the two lists. In ours2,
# the elements of the lists are still independent of eachother. 

# When changing the content of yours, ours2 changes but ours 1 remains the same. This is because ours1 is a new
#variable that we had created with the original lists. Ours2 remains the same because it still contains the independent
#elements of each list. 
