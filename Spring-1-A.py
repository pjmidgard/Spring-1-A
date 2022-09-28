from time import time
cvf=0
import os
import binascii
self="'"

namez = input("for password for incrypt file p1 or p2 insert password from file ")
#@Author Jurijus pacalovas
class password_class:

    def password1(self):

                def strToBinary(s):
                    bin_conv = []
                 
                    for c in s:
                         
                        # convert each char to
                        # ASCII value
                        ascii_val = ord(c)
                         
                        # Convert ASCII value to binary
                        binary_val = bin(ascii_val)
                        bin_conv.append(binary_val[2:])
                     
                        return (' '.join(bin_conv))       
                
                self.name = "Author: Jurijus Pacalovas"

                print(self.name)

                if namez!="p1" and namez!="p2":
                    print("Your enter incorrect letter")
                
                if namez=="p1":


                    
                   
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

                                import getpass
                                
                                password=getpass.getpass()
                                

                                string = password

                                lower="abcdefghijklmopqrstuvwxyz"

                                upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

                                res=""

                                for i in range(0,len(string)):

                                    if(i%2==0):

                                        if(string[i] in lower):

                                            res+="1"*(lower.index(string[i])+1)

                                        else:

                                            res+="1"*(upper.index(string[i])+1)

                                    else:

                                        if(string[i] in lower):

                                            res+="0"*(lower.index(string[i])+1)

                                        else:

                                            res+="0"*(upper.index(string[i])+1)

                                password=res  
                                N=int(password,2)
                                N=format(N,'0240b')

                                password=N    

                                
                                
                                
                                    
                                    
                                size_data11=password+size_data3
             
                                                                                
                                n = int(size_data11, 2)
                                
                                qqwslenf=len(size_data11)
                                qqwslenf=(qqwslenf/8)*2
                                qqwslenf=str(qqwslenf)
                                qqwslenf="%0"+qqwslenf+"x"
                             
                                jl=binascii.unhexlify(qqwslenf % n)
                                
                                
                                    
                                size_after=len(jl)

                                size_after=len(jl)
                                
                                   
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

    def password2(self):

                 def strToBinary(s):
                        bin_conv = []
                     
                        for c in s:
                             
                            # convert each char to
                            # ASCII value
                            ascii_val = ord(c)
                             
                            # Convert ASCII value to binary
                            binary_val = bin(ascii_val)
                            bin_conv.append(binary_val[2:])
                             
                            return (' '.join(bin_conv))
                 if namez=="p2":
                    
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
                        
                        data = binary_file.read()

                        

                    
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
                                    
                                    import getpass

                                    password=getpass.getpass()
                                    
                                    password1=size_data3[:240]
                                    
                                    string = password

                                    lower="abcdefghijklmopqrstuvwxyz"

                                    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

                                    res=""

                                    for i in range(0,len(string)):

                                        if(i%2==0):

                                            if(string[i] in lower):

                                                res+="1"*(lower.index(string[i])+1)

                                            else:

                                                res+="1"*(upper.index(string[i])+1)

                                        else:

                                            if(string[i] in lower):

                                               res+="0"*(lower.index(string[i])+1)

                                            else:

                                               res+="0"*(upper.index(string[i])+1)

                                    password=res   
                                    
                                    
                                
                                    N=int(password,2)
                                    N=format(N,'0240b')

                                    password=N    
                                    
                                    if  password==password1:
                                        size_data3=size_data3[240:]
                                        
                                      
                                    n = int(size_data3, 2)
                                    
                                    
                                    qqwslenf=len(size_data3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                  
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
d=password_class()
    
xw=d.password1()
print(xw)

xw1=d.password2()
print(xw1)
