#Input Output Files
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

"""
All 4 components of the IAS machine has been implemented as classes
Each class contains all the sub components as class attribute variables
and all the diffrent steps that happenes inside these classes as methods
"""

#Components Begin
class Arithmetic_Logical_Unit:
    ac=None
    mq=None
    mbr=None
    def __init__(self):
        pass
    def memory_to_mbr(self,value):                              
        self.mbr=value                                          
        return(self.mbr)
    """
    Perofrms logical operations based on signal received from control circuits.
    """
    def Arithmetic_Logical_Circuits(self, signal,data):
        if signal==1:
            self.ac=data
            return
        elif signal==2:
            self.ac=format(int(self.ac,2)+int(data,2), "040b")
            return
        elif signal==3:
            self.ac=format(int(self.ac,2)-int(data,2), "040b")
            return
        elif signal==4:
            return(self.ac)
class Program_Control_Unit:
    ibr=None
    ir=None
    pc=format(int("0",2), "012b")
    mar=None
    
    def __init__(self):
        pass
    def pc_to_mar(self):
        self.mar=self.pc
        self.pc=format(int(self.pc,2)+1, "012b")
        return(self.mar)
    def mbr_to_ibr(self,mbr_rhs):
        self.ibr=mbr_rhs
        return(self.ibr)
    def mbr_to_mar(self,mbr_adress):
        self.mar=mbr_adress
        return(self.mar)
    def mbr_to_ir(self,mbr_optcode):
        self.ir=mbr_optcode
        return(self.ir)
    """
    Generates signals after analising the opt code
    """
    def Signal_From_Control_Circuit(self):
        if(self.ir=="00000001"):
            return(1)
        elif(self.ir=="00000101"):
            return(2)
        elif(self.ir=="00000110"):
            return(3)
        elif(self.ir=="00100001"):
            return(4)
    def ibr_to_mar(self):
        self.mar=(self.ibr)[8:20]
        return(self.mar)
    def ibr_to_ir(self):
        self.ir=(self.ibr)[0:8]
        return(self.ir)

class Input_Output:
    def __init__(self):
        pass
    def InputData(self):
        inpt=input("")
        if inpt!="STOP":
            i=int(inpt, 2)
            return(format(i, "040b"))
        else:
            return("STOP")
    def InputInstruction(self):
        inpt=input("")
        if inpt!="STOP":
            i=int(inpt, 2)
            return(format(i, "040b"))
        else:
            return("STOP")
    def Output(self, value):
        print(value)

class Memory:
    """
    Stored in this format 
    [[adress,data],[adress,data],[adress,data]................]
    """
    mem=[] 
    next_instruction_memory_location=0
    next_data_memory_location=99
    """
    initialises the adress of all locations with 12 bit adress
    """
    def __init__(self):
        x="0"
        for i in range(200):
            self.mem.append([str(x).zfill(12),None])
            x = format(int(x,2)+1, "012b")

    def fetch_from_memory(self,adress):
        for i in range(200):
            if adress==(self.mem[i])[0]:
                return (self.mem[i])[1]

    def store_to_instruction_memory(self,value, adress): 
        for i in range(200):
            if adress==(self.mem[i])[0]:
                (self.mem[i])[1]=value 
                self.next_instruction_memory_location=self.next_instruction_memory_location+1
                break
    def store_to_data_memory(self,value, adress): 
        for i in range(200):
            if adress==(self.mem[i])[0]:
                (self.mem[i])[1]=value
                self.next_data_memory_location=self.next_data_memory_location+1
                break
#Components end 

"""
The Below class is the our IAS Computer,
an instance of all the the component classes has been created in this class.
All the main processes (fetch, decode, excecute) has been created as methods in this class.
A special method is created to demonstrate the whole process.
"""

class IAS:
    #IAS Components
    alu=Arithmetic_Logical_Unit()
    pcu=Program_Control_Unit()
    io=Input_Output()
    m=Memory()
    """
    Initialise all the memory locations that contains data(variables)
    """
    def initialise_data_memory(self):
        while True:
            input=self.io.InputData()
            if input!="STOP":
                self.m.store_to_data_memory(input,format(self.m.next_data_memory_location, "012b"))
            else:
                break
    """
    Initialise all the memory locations that contains instructions by taking user input
    """
    def initialise_instruction_memory(self):
        while True:
            input=self.io.InputInstruction()
            if input!="STOP":
                self.m.store_to_instruction_memory(input,format(self.m.next_instruction_memory_location, "012b"))
            else:
                break
    def fetch(self):
        current_mar=self.pcu.pc_to_mar()
        value=self.m.fetch_from_memory(current_mar)
        current_mbr=self.alu.memory_to_mbr(value)
    def decode_lhs(self):
        current_ibr=self.pcu.mbr_to_ibr(self.alu.mbr[20:40])
        current_ir=self.pcu.mbr_to_ir(self.alu.mbr[0:8])
        current_mar=self.pcu.mbr_to_mar(self.alu.mbr[8:20])
    def execute_lhs(self):
        signal=self.pcu.Signal_From_Control_Circuit()
        data=self.m.fetch_from_memory(self.pcu.mar)
        return_value=self.alu.Arithmetic_Logical_Circuits(signal,data)
        if return_value:
            self.m.store_to_data_memory(return_value,data)
            self.io.Output(return_value)
            return 1
        else:
            return 0
    def decode_rhs(self):
        if self.pcu.ibr==format(int("0",2), "020b"):
            pass
        else:
            current_ir=self.pcu.ibr_to_ir()
            current_mar=self.pcu.ibr_to_mar()
    def execute_rhs(self):
        if self.pcu.ibr!=format(int("0",2), "020b"):
            signal=self.pcu.Signal_From_Control_Circuit()
            data=self.m.fetch_from_memory(self.pcu.mar)
            return_value=self.alu.Arithmetic_Logical_Circuits(signal,data)
            if return_value:
                self.m.store_to_data_memory(return_value,data)
                self.io.Output(return_value)
                return 1
            else:
                return 0
    def IAS_Demonstation_statements(self,stringg):
        print("=====================================================")
        print(stringg," process is now complete")
        print("Here are the status of all IAS components")
        print("Memory:\n",self.m.mem)
        print("PC: ",self.pcu.pc)
        print("MAR: ",self.pcu.mar)
        print("IBR: ",self.pcu.ibr)
        print("IR: ",self.pcu.ir)
        print("MBR: ",self.alu.mbr)
        print("AC: ",self.alu.ac)
        print("MQ: ",self.alu.mq)
        print("=====================================================")


"""
In the main function, I have made a instance of IAS class, and then excecuted all the process one by one. 
It can be run on 2 modes, With demo and without demo.
"""

#Main
Myias=IAS()
choice=input("")
if(choice=="n"):
    Myias.initialise_data_memory()
    Myias.initialise_instruction_memory()
    while(Myias.m.fetch_from_memory(Myias.pcu.pc)!=None):
        Myias.fetch()
        Myias.decode_lhs()
        Myias.execute_lhs()
        Myias.decode_rhs()
        Myias.execute_rhs()
else:
    print("<<<<<<Welcome To The IAS Architecture Demonstration>>>>>>")
    Myias.initialise_data_memory()
    Myias.initialise_instruction_memory()
    while(Myias.m.fetch_from_memory(Myias.pcu.pc)!=None):
        Myias.IAS_Demonstation_statements("No")
        Myias.fetch()
        Myias.IAS_Demonstation_statements("Fetch")
        Myias.decode_lhs()
        Myias.IAS_Demonstation_statements("Decode LHS")
        check=Myias.execute_lhs()
        if check==1:
            print("^^^^Alert,Output Received^^^^")
            print("")
        Myias.IAS_Demonstation_statements("Execute LHS")
        Myias.decode_rhs()
        Myias.IAS_Demonstation_statements("Decode RHS")
        check=Myias.execute_rhs()
        if check==1:
            print("^^^^Alert,Output Received^^^^")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        Myias.IAS_Demonstation_statements("Execute RHS")