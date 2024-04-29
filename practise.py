import streamlit as st

st.title("This is my sample discovery - This is what st.title behaves like.")
st.header("This is Header - This is what st.header behaves like.")
st.subheader("This is subheader - This is what suheader behaves like.")
st.text("Hello This is Bhulu! I am a good person constantly thriving to learn - This is how st.text behaves like.!")
st.markdown("###### This is a markdown")
st.markdown("Hey! Bhulu this side.....")
st.markdown("** This is How Text is made bold using  \*\* **")
st.markdown("__ This is how we can make it bold using \_\_ __")
st.markdown("_ This is how we make it italic using \_ _")
st.markdown("* This is how we make it italic using \* *")
st.markdown("# This is how header h1 is made using\"\#\" -> It is placed at starting of the string")
st.markdown("## This is how header h2 is made using \"\#\#\" -> It is placed at starting of the string.")
st.markdown("### This is how header h3 is made using \"\#\#\#\" -> It is placed at starting of the string.")
st.markdown("#### This is how header h4 is made using \"\#\#\#\#\" -> It is placed at starting of the string.")
st.markdown("##### This is how header h5 is made using \"\#\#\#\#\#\" -> It is placed at starting of the string.")
st.markdown("###### This is how header h6 is made using \"\#\#\#\#\#\#\" -> It is placed at starting of the string.")
st.markdown("[Hey! This is my sisters website take a look !!!!! - Inline Link](https://meghanaatmakuri.pythonanywhere.com/?next=/home)")
st.markdown('''
             [openurl]:https://meghanaatmakuri.pythonanywhere.com/?next=/home 
             Hey go check out this [click here][openurl] -> This is reference link.
   ''')
st.markdown("![A beautiful me](https://th.bing.com/th/id/OIP.SWt73TF8w5OjKp7NV7IvIQHaEK?w=314&h=180&c=7&r=0&o=5&pid=1.7)")
st.markdown('''
         [img]:https://th.bing.com/th/id/OIP.SWt73TF8w5OjKp7NV7IvIQHaEK?w=314&h=180&c=7&r=0&o=5&pid=1.7
         ![This is a Beautiful Scene][img]
            ''')
st.markdown('''
            Unordered list - 1
            - Travel
              - Bus
              - Train
              - Car
            ''')
st.markdown('''
           Unordered list - 2
           * Groceries
             * Milk
             * Egg
             * Chocolate         

'''
)
st.markdown(
    '''
    Ordered List
    1. Skills
       1. Java
       2. Python
       3. C++
'''
)
st.markdown("`Hi` - Inline Code.")
st.markdown('''
      ```python
def add(x,y):
    print(x+y)
add(1,2)
            ''')
import streamlit as st

st.markdown("""
```python
def greet():
    print("Hello, world!")
- Code Blocks
""")
st.markdown(
    '''
| S.NO | Name | 
|------|------|
|  1   |Bhuvana|
|  2   |Atmakuri|
'''
)
st.markdown("***")
st.success("Hurray !!!! I Got An Intenship")
st.warning("Beware of Dogs !!")
st.info("I got a new lesson today 😋")
st.error("Hehe There is no error now!")
def testing():
    a=10
    b=0
    try:
        a//b
    except ZeroDivisionError as zer:
        st.exception(zer)
testing()
st.text(range(10))
st.write(range(0,10))

from PIL import Image
imag = Image.open("fall.jpeg")
# st.image(imag,width=100,height=100) # Does not accept a height argument.
imag=imag.resize((500,600))
st.image(imag,caption="Hey This is my achievement") #Caption adds a small description to the image.

st.markdown('''
          ```python
            st.image(imag,width=200) - can only set width and not height directly.           
'''
            )
val=st.checkbox("Check the box if you are female.",False)#Default value is stored as True or False.
if val:
    st.write("oh u are a female !!")

#Radio Buttons
selection=st.radio("Choose Your Gender",["choose","Female","Male","others"],0)
st.write(selection)
#By using dictionaries.
options = {"Option 1": 1, "Option 2": 2, "Option 3": 3}
selected_option = st.radio("Select an option", list(options.keys()))
selected_value = options[selected_option]
st.write("You selected:", selected_value)

#By using selectbox to select an option from dropdown.
selected_op=st.selectbox("Select Your Department:",["Choose","COMPUTER SCIENCE","ECE","EEE","Mechanical"],index=0)
st.write("you selected:",selected_op)

#Multiselect
hobbies = st.multiselect("Hobbies: ",['Dancing', 'Reading', 'Sports'])
st.write("You selected", len(hobbies), 'hobbies',"They are:",hobbies)

#Button
value=st.button("Click me for no reason!")
if(value):
    st.write("You Truely Have No work 😁")
#Text Input
name=st.text_input("Enter your name:","Type Here ....")
height = st.number_input('Meters')
but=st.button("Submit")
if(but):
    st.success(name.title())#title() function is used to make 1st letter of each word caps.


# slider
 
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)
 
# print the level
# format() is used to print value 
# of a variable at a specific position
st.text('Selected: {}'.format(level))

#Mini Project
# import the streamlit library
import streamlit as st

# give a title to our app
st.title('Welcome to BMI Calculator')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
				('cms', 'meters', 'feet'))

# compare status value
if(status == 'cms'):
	# take height input in centimeters
	height = st.number_input('Centimeters')

	try:
		bmi = weight / ((height/100)**2)
	except:
		st.text("Enter some value of height")

elif(status == 'meters'):
	# take height input in meters
	height = st.number_input('Meters')

	try:
		bmi = weight / (height ** 2)
	except:
		st.text("Enter some value of height")

else:
	# take height input in feet
	height = st.number_input('Feet')

	# 1 meter = 3.28
	try:
		bmi = weight / (((height/3.28))**2)
	except:
		st.text("Enter some value of height")

# check if the button is pressed or not
if(st.button('Calculate BMI')):

	# print the BMI INDEX
	st.text("Your BMI Index is {}.".format(bmi))

	# give the interpretation of BMI index
	if(bmi < 16):
		st.error("You are Extremely Underweight")
	elif(bmi >= 16 and bmi < 18.5):
		st.warning("You are Underweight")
	elif(bmi >= 18.5 and bmi < 25):
		st.success("Healthy")
	elif(bmi >= 25 and bmi < 30):
		st.warning("Overweight")
	elif(bmi >= 30):
		st.error("Extremely Overweight")
