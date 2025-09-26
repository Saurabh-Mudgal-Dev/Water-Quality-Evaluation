class Area:
    #Creating a class Area to emphasize abstraction and ease data filling
    def __init__(self,name, turbid, contam, ph_dev):

        '''Parameters used are turbidity (cloudiness),
        contamination index, pH deviation (abs(7-pH)*5 for scale)'''

        self.turbid=turbid
        self.contam=contam
        self.ph_dev=ph_dev
        self.name=name
        self.record=[turbid,contam,ph_dev]

no_A=mod_A=ext_A=0
def check_imp(x,y,z):
    global no_A,mod_A,ext_A
    imp=0.5*x+0.5*y+5*z
    if imp>=0 and imp<45:
        print('No assistance needed')
        no_A+=1
    elif imp>=45 and imp<90:
        print('Moderate attention needed')
        mod_A+=1
    elif imp>=90:
        print('Extreme attention needed')  
        ext_A+=1  

import pickle as pkl                # we assume a pre existing binary file which has simple lists and unspecified parameters
File=open('Information.dat','rb')
while True:
    try:
        entry=pkl.load(File)
        A1=Area(*entry)
        print(A1.name+':', end=' ')
        check_imp(A1.turbid,A1.contam,A1.ph_dev)
    except EOFError:
        break
File.close()
print(f"No assistance required:{no_A},Moderate assistance required:{mod_A},Extreme assistance required:{ext_A}")