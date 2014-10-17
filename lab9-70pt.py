############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer
print "enter in temprature in celcius" 
cel=int(raw_input())
cel=cel*9
cel=cel/5
cel=cel+32
print "The celcius temp in Fahrenhiet equals "+str(cel)
