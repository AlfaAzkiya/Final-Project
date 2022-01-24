from appJar import gui


def Encrypt (filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    
    file = open(filename, "wb")
    file.write(data)
    file.close()


def Decrypt (filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    
    file = open(filename, "wb")
    file.write(data)
    file.close

    
        
def press(button):
    
    if button == "Encrypt":
        filename = app.getEntry("Input_File")
        key = (int(app.getEntry("Insert_Key")))
        Encrypt(filename, key)

    elif button == "Decrypt":
        filename = app.getEntry("Input_File")
        key = (int(app.getEntry("Insert_Key")))
        Decrypt(filename, key)
        
    else:
        app.stop()



# Create the GUI Window
app = gui("Encrypt & Decrypt", useTtk=True)
app.setTtkTheme("default")
app.setSize(500, 200)

# Add the interactive components
app.addLabel("Choose Source PDF File")
app.addFileEntry("Input_File")

app.addLabel("Insert Key")
app.addEntry("Insert_Key")


# link the buttons to the function called press
app.addButtons(["Encrypt", "Decrypt", "Quit"], press)

# start the GUI
app.go()
