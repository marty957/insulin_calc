import re
with open("preproinsulin.txt", "r") as file:
 
 lines= file.readlines()
  
 del lines[0]
 del lines[2]
 str1=''.join(lines)
 str_without_number = re.sub(r"[0-9\s]","",str1)
 
 
 with open("preproinsulin-seq-clean.txt","w") as file2:
  
  file2.write(str_without_number)
  


with open("preproinsulin-seq-clean.txt", "r") as checkFile1:
 
  stringToCheck = checkFile1.read()

if len(stringToCheck) >= 110:

 first_seq=stringToCheck[0:23]
 secend_seq=stringToCheck[24:53]
 third_seq=stringToCheck[54:88]
 fourth_seq=stringToCheck[89:110]
 print("Preproinsulin is long enough")
else:
  
 print("Preproinsulin is incoret")
 
with open("Isinsulin-seq-clean.txt","w") as seq1:
 seq1.write(first_seq)
 
 if len(first_seq) == 23:
  print("Isinsulin is good")
 else:
  print("Something went wrong")
  
with open("binsulin-seq-clean.txt","w") as seq2:
 seq2.write(secend_seq)
 
 if len(secend_seq) == 29:
  print("binsulin is good")
 else:
  print("Something went wrong")
  
with open("cinsulin-seq-clean.txt", "w") as seq3:
 seq3.write(third_seq)
 
 if len(third_seq) == 34:
  print("cinsulin is good")
 else:
  print("Something went wrong")
  
with open("ainsulin-seq-clean.txt","w") as seq4:
 seq4.write(fourth_seq)
 
 if len(fourth_seq) == 21:
  print("ainsulinis good")
 else:
  print("Something went wrong")