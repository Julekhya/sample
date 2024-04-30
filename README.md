# sample

Unit converter project works from the steps user interface,input handling,conversion logic,calculation to finally ouput

User Interface: The project starts with a user interface where the user can input the value they want to convert and select the units they are converting from and to. This interface can be implemented as a command-line interface or any other depending on the application.

Input Handling: Once the user enters the value and selects the units, the program parses this input and validates it to ensure it's in the correct format.

Conversion Logic: The program then performs the actual conversion using conversion factors. These factors are predetermined constants that relate one unit of measurement to another.

Calculation: The program multiplies the input value by the appropriate conversion factor to obtain the converted value.

Output: Finally, the program displays the converted value to the user.

Optional Features: Advanced unit converter projects might include additional features such as support for a wide range of units, the ability to add custom units, handling of different data types (e.g.,volume, temperature) and support for complex conversions involving multiple steps.
                              
                              Code Expalnation
                              
First we need to creat a class with the quantity of which you need to convert units.

We need to call a function to feed intial ,final values of amount of quantity we give as a input using self.input.

Now create another function to convert temperature to different units like kelvin,celsius,fahrenheit.

Create another class with volume.

We will have to the same process as that of used in the case of temperature.

Finally we need to use if else conditions to analyse user inputs and call the functiooon according to user input. 
