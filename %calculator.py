width = input("ENTER WIDTH > ")
height = input("ENTER HEIGHT > ")

precentage = input("ENTER PRECENTAGE > ")

print("THE WIDTH OF YOUR PHOTO IS : " + str(float(width) / 100 * float(precentage) + float(width)))
print("THE HEIGHT OF YOUR PHOTO IS :" + str(float(height) / 100 * float(precentage) + float(height)))

input("close? > ")