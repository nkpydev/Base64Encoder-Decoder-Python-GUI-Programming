from appJar import gui  # This is a GUI Library to create good UserInterfaces
import base64 # This is to use the Base64 Encoding/Decoding facility from this library



# This is a function defined to either Clear, Encode, Decode or Close the program.
def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Clear":
        app.clearTextArea("input")
        app.clearTextArea("output")
    elif btn == "Encode":
        try:    
            if app.getTextArea("input") == "":
                app.errorBox('EmtpyInput',"Oops! Nothing to Encode!!")
            else:
                ncode1 = bytes(app.getTextArea("input"),'utf-8')
                ncode2 = base64.encodebytes(ncode1)
                app.clearTextArea('output')
                app.setTextArea('output',ncode2)
        except Exception as e:
            app.errorBox('Base64EncodeError',e)
    elif btn == "Decode":
        try:
            if app.getTextArea("output") == "":
                app.errorBox('EmtpyInput',"Oops! Nothing to Decode!!")
            else:
                ncode1 = bytes(app.getTextArea("output"),'utf-8')
                ncode2 = base64.decodebytes(ncode1)
                app.clearTextArea('input')
                app.setTextArea('input',ncode2)
        except Exception as e:
            app.errorBox('Base64DecodeError',e)    

# Intialize/Define the app GUI, with name and size
app = gui("BASE64-Encoder/Decoder","500X500")
# Set SkyBlue Background color
app.setBg("SkyBlue")

# User Interface: We will try to create 3 vertical and 3 horizontal frames to create and locate specifically our Labels and user Input/Output Text Areas.

# This is the first vertical column
app.startFrame("FirstColumn",column=0)
app.addEmptyLabel("FirstVerticalSpacer",column=0)
app.stopFrame()

# This is second vertical column
app.startFrame("SecondColumn",column=1)

app.startFrame("IntialSpacer",row=0)
app.addEmptyLabel("Initial",row=0)
app.stopFrame()

app.startFrame("InputFrame",row=1)
app.addLabel("InputLabel","Encode:",row=1,column=0)
app.addTextArea("input",text=None,row=1,column=1)
app.stopFrame()

app.startFrame("OutputFrame",row=2)
app.addLabel("OutputLabel","Decode:",row=2,column=0)
app.addTextArea("output",text=None,row=2,column=1)
app.stopFrame()

app.startFrame("MidSpacer",row=3)
app.addEmptyLabel("Mid",row=3)
app.stopFrame()

app.startFrame("ButtonFrame",row=4)
app.addButtons(["Clear","Encode","Decode","Exit"],press,row=2,column=1,colspan=2)
app.stopFrame()

app.startFrame("FinalSpacer",row=5)
app.addEmptyLabel("Final",row=5)
app.stopFrame()

app.stopFrame()

# This is third vertical column
app.startFrame("ThirdColumn",column=2)
app.addEmptyLabel("ThirdVerticalSpacer",column=2)
app.stopFrame()


# Start the app
app.go()
