#Starting Array
tools = ['Laptop', 'Monitor', 'Keyboard', 'Mouse']

# Goal print laptop out of our list
print(tools[0])

# Grab mouse from tool kit
print(tools[-1])

# Create a subarray of monitor and keyboard from the list
# Stop index is NOT inclusive
removed = tools[1:3]
print(removed)

# REplaced monitor with webcam, modifying with []
tools[1] = 'Webcam'
print(tools)

# Add a desk to our tools
tools.append('Desk')
print(tools)

# Lets add headphones at the 1st index
tools.insert(1, 'Headphones')
print(tools)

# Remove keyboard
tools.remove('Keyboard')
print(tools)

# figure out how many items are in my backpack/tool and save to a variable
numOfItems = len(tools)
print(f'Tool Length: {numOfItems}')

og_list = [1, 2, 3]

new_reference = og_list

new_reference.append(4)

print('Ref list:', new_reference)
print('Og list:', og_list)
print(og_list == new_reference)

# Deep Copys - for when you want to manipulate data without changing source
new_deep_copy = og_list.copy()

new_deep_copy.append(13)
print('Og list:', og_list)
print('Deep Copy:', new_deep_copy)

# Part 3 -------------------------------------
# Lists and Functions
recent_first =  [1989, 1991, 1997, 2000]
recent_last = [2022, 2018, 2016, 2011]

def reorder_years(recentFirst, recentLast):
    recentLast.reverse()

    recentFirst.extend(recent_last)

    return recentFirst

reorder_years(recent_first, recent_last)

print(recent_first)