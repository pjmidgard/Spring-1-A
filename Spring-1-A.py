from time import time
cvf=0
import os
import binascii
self="'"

namez = input("for compress c or extract e? ")
#@Author Jurijus pacalovas
class compression:

    def cryptograpy_compression(self):

                
                
                self.name = "Author: Jurijus Pacalovas"

                print(self.name)

                if namez!="c" and namez!="e":
                    print("Your enter incorrect letter")
                
                if namez=="c":


                    
                   
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                   
                    long_block=100
                        
                    namea=""
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)

                    long=len(name)
                   
                    Times_compression=1
                    
                    name_cut=len(".bin")
                    
                    nameas=name+".bin"
                    name_bofore=len(nameas)
                    F=0
                    
                    
                    	 
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        #import paq
                        #data=paq.compress(data)
                
                        size_after2=len(data)
                        #print(size_after2)  
                        
                        if len(data)==0 or len(data)>2**40:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                         

                  
                        s=str(data)
                        
                        
                        lenf1=len(data)
                          
                    
                            
  
                            
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)

                                
                                    
                                
                                size_data3=size_data2
                               
                                long_file=len(size_data3)
                              
                                size_data10=size_data3
                               
                                times_of_times=0

                                cvf1=1
  
                                if cvf1==1:
                                    times_compression=0  
                                  
                                    long2=len(size_data3)
                                
                                    size_data10=size_data3
                                    
                                    
                                    long2=len(size_data3)
                                    
                                    #Logit 
                                    blocks=8#9 numbers 29 bits
                                    Number_Save=""            
                                    block=0  
                                    long=len(size_data3)
                                    times_count=0

                                    while times_count!=1:
                                        long=len(size_data3)
                                        #print(long)
                                
                                        while block<long:
                                            ILIN=size_data3[block:block+blocks]
                                            
                                            Number=int(ILIN,2)

                                            Str_Ilin_Number_Save=str(Number) 
                                            long5=len(Str_Ilin_Number_Save)
                                            str1=str(long5)
                                        
                                            c=0
                                            if Number>99:
                                                str1=""
                                                Str_Ilin_Number_Save=ILIN
                                                N=Str_Ilin_Number_Save
                                                #print(N)#1 0 or 1 1
                                            elif Number<100 and Number>29:
                                                str1=""
                                                N=str1+Str_Ilin_Number_Save
                                                N=int(N)
                                                N=format(N,'08b')#0
                                                
             
                                                if N[0:4]=="0000":
                                                      print("File can't compress")
                                                      N=str1+Str_Ilin_Number_Save
                                                      N=int(N)
                                                      N1=format(N,'07b')#0
                                                      
                                                      if N1[0:3]=="000":
                                                            print("File can't compress")
                                                            raise SystemExit
                                                   
                                                    
                                                    #print(N)
                                                else:
                                                    N=str1+Str_Ilin_Number_Save
                                                    N=int(N)
                                                    N=format(N,'08b')#0
                                                    if N[0:2]=="00":
                                                        N=str1+Str_Ilin_Number_Save
                                                        N=int(N)
                                                        N=format(N,'08b')#0

                                                        
                                                        
                                                #print(len(N))
                                                #print(N)#000
                                            elif Number<30:
                                                str1="0"
                                                N=Str_Ilin_Number_Save
                                                N=int(N)
                                                N=format(N,'08b')#00
                                                if N[0:4]=="0000":
                                                    str1="0"
                                                    N=Str_Ilin_Number_Save
                                                    N=int(N)
                                                    N=format(N,'07b')#00

                      #if N[0:4]=="0000":
                                                        #print(N)
                                                
                                            
                                            
                                            #print(N)
                                            Number_Save=Number_Save+N
                                            
                                            block=block+blocks
                                        size_data12=Number_Save
                                        size_data11=size_data12
                                        size_data3=size_data12
                                        times_count=times_count+1
                                        #print(times_count)
                                    #print(size_data12)
                                    
                                    b=bin(long2)[2:]
                                    #print(b)
                                    long8=len(b)
                                    #print(long8)
                                    b1=format(long8,'08b')
                                    b2=format(times_count,'040b')
                                    #print(len(size_data11))
                                    
                                    
                                    size_data11="1"+size_data11
                            
                                    lenf=len(size_data11)
                                        
                                    add_bits118=""
                                    count_bits=8-lenf%8
                                    z=0
                                    
                                    if count_bits!=8:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                                    
                                                                    
                                    size_data11=add_bits118+size_data11
                                    
                                    
                                    size_data11=size_data11
             
                                                                                
                                    n = int(size_data11, 2)
                                
                                    qqwslenf=len(size_data11)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                
                                    #import paq
                                    #jl= paq.compress(jl)
                                    
                                    size_after=len(jl)

                                    size_after=len(jl)
                                    #print(size_after)
                                   
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:

                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

    def cryptograpy_unpack(self):                      
                 if namez=="e":
                    
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    Portal=2
                    namea=""
                    namem=""
                    namema="?"
                    Deep=0
                 
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    nac=len(nameas)
                    
                  
                    
                    long=len(nameas)

                    
                    
                    
                    
                    Deep_long=240
                    Deep_long_All=Deep_long*16
                    block_size_long=16
                    Times_compression=1
                    	
                    
                    
                    nac=len(nameas)
                   
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        
                        data3 = binary_file.read()

                        data=data3

                    
                        #import paq
                        #data= paq.decompress(data)
                    

                        
                        
                        

                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                     	

                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)  
                                x4=1
                                if x4==1:

                                    

                                    size_data3=size_data2

                                    if size_data3[0:9]=="000000001":
                                        size_data3=size_data3[9:]
                                    elif size_data3[0:8]=="00000001":
                                        size_data3=size_data3[8:]
                                    elif size_data3[0:7]=="0000001":
                                        size_data3=size_data3[7:]
                                    elif size_data3[0:6]=="000001":
                                        size_data3=size_data3[6:]
                                    elif size_data3[0:5]=="00001":
                                        size_data3=size_data3[5:]
                                    elif size_data3[0:4]=="0001":
                                        size_data3=size_data3[4:]
                                    elif size_data3[0:3]=="001":
                                        size_data3=size_data3[3:]
                                    elif size_data3[0:2]=="01":
                                        size_data3=size_data3[2:]
                                    elif size_data3[0:1]=="1":
                                        size_data3=size_data3[1:]


                                    
                                    size_data10=size_data3
                                    
                                    
                                    long2=len(size_data3)
                                    
                                    #Logit 
                                    blocks=7#9 numbers 29 bits
                                    Number_Save=""            
                                    block=0  
                                    long=len(size_data3)
                                    times_count=0

                                    while times_count!=1:
                                        long=len(size_data3)
                                        #print(long)
                                
                                        while block<long:
                                            ILIN=size_data3[block:block+blocks]
                                            
                                            Number=int(ILIN,2)

                                            Str_Ilin_Number_Save=str(Number) 
                                            long5=len(Str_Ilin_Number_Save)
                                            str1=str(long5)
                                        
                                            
                                            N=Str_Ilin_Number_Save

                                            N=int(N)
                                            N=format(N,'07b')#00
                                            if N[0:3]=="000" and Number<30:
                                                N=Str_Ilin_Number_Save
                                                
                                                N=int(N)
                                                N=format(N,'08b')#00
                                                print(Number)
                                            else:
                                                ILIN=size_data3[block:block+8]
                                            
                                                Number=int(ILIN,2)

                                                Str_Ilin_Number_Save=str(Number) 
                                                long5=len(Str_Ilin_Number_Save)
                                                str1=str(long5)
                                            
                                            
                                                N=Str_Ilin_Number_Save
                                                N=int(N)
                                                N=format(N,'08b')#00
                                                      
                                            #if N[0:4]=="0000":
                                                        #print(N)
                                                
                                            
                                            
                                            #print(N)
                                            Number_Save=Number_Save+N
                                            
                                            block=block+blocks
                                        size_data12=Number_Save
                                        size_data11=size_data12
                                        times_count=times_count+1                                    
                                    size_data3=size_data11
                                    #print(len(size_data3))	
                                        
                                      
                                    n = int(size_data3, 2)
                                    
                                    
                                    qqwslenf=len(size_data3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    
                                    
                                    
                                    data2=jl

                               
                                    sssssw=len(jl) 
                                  
                                   

                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                                    
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:
                                        	
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)  
                  
self=""                                
d=compression()
    
xw=d.cryptograpy_compression()
print(xw)

xw1=d.cryptograpy_unpack()
print(xw1)
