#23 March 2021
#Cherilus Sam Bracley
# cherilussambracley@gmail.com
# tech5_09
#15:51


from tkinter import*

#This is the mad Libs Generator project with Tkinter 




window=Tk()
window.title("Mad Libs Generator")

Input_one = Entry()

#Text for the first input a kind of placeholder in the order to show to the user what to do and where
Text_one = "Insert your value" 
Input_one.insert(0, Text_one)
Input_one.pack()



#Text for the second input a kind of placeholder in the order to show to the user what to do and where
Text_two = "Insert your second value"



Input_two= Entry()
Input_two.insert(0, Text_two)
Input_two.pack()



#Text for the third input a kind of placeholder in the order to show to the user what to do and where
Text_three= "Insert your third value"
Input_three=Entry()
Input_three.insert(0, Text_three)
Input_three.pack()





def ACTION():
    Value_one= Input_one.get()
    Value_two=Input_two.get()
    Value_three= Input_three.get()

    global RESULT
    
    RESULT= str(Value_one) + " " +  str(Value_two) + " " + str(Value_three)


    MESSAGE= Label(window, text=RESULT)
    MESSAGE.pack()

    

#button text
Button_text= "Let's Go"
Button= Button(window, text= Button_text,  command=ACTION)
Button.pack()




window.mainloop()





