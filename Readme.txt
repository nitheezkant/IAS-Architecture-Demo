$$IAS Architecture Implimentation 
>>>The Program has been implemented in an object-oriented manner.

>>>Explanation about the classes has been mentioned in the comments 
above each set of classes.

>>>Each major process (fetch, decode, execute) has been shown as a 
method in the IAS class and all small sub-process is shown as a method 
in the corresponding component class. Methods have been named in such a way that 
no explanation would be required to understand what is being done(eg: the "pc_to_mar" 
method sends the value of PC to MAR). 

>>>A special feature is included that outputs status of each
component after every process.

>>>In the memory, Instructions are stored from address '000000000000' to 
'000001100010' and data(variables) are stored from '000001100011' to '000011000111'.

>>>The first data that you send in is stored in '000001100011', then 
subsequent data is progressively stored towards '000011000111'. Remember this 
while entering the address in the 40-bit instruction.


$$The input format in input.txt

>>>Line 1 contains 'y' or 'n'. y outputs the entire demo. 
'n' outputs 40-bit data each time a data is stored in memory from ALU.

>>>It is then followed by data(variable values). You may wish 
to give it in 40-bit format, else if u give it in other bit binary formats(eg: "011"), 
then it is auto-converted to 40 bits in the Input_Output module by adding the leading zeros. 
Variable input ends with a "STOP".

>>>It is followed by 40-bit instructions. OPT codes corresponding to LOAD, 
ADD, SUB, and STORE are accepted. Give the appropriate address. 
Instructions input ends with a "STOP". 


$$Samples:
The following samples have been executed and attached with 
both input and output files(with and without demo).
1)>>>9-5=4
2)>>>49+51=100
3)>>>4+6-7+9-3+1-10=0
ps:
>>>In main folder (where both readme and main python code is stored), an empty 
input and output text files have been given where you can test your own custom 
test cases
>>>Visual Studio Code is recommended for viewing txt output files as it does 
not wrap the long memory line providing a decent expirence.