#################################################################################################
#                      Ad & Soyad: Lüey Elhac Ali 
#                      oğrenci numarasi : b201200554
#                      Ödev adı : block zincri
#################################################################################################
import hashlib
class LueyCoinBlock:
 def __init__(self,previous_block_hash ,transaciton_list):
         self.previous_block_hash=previous_block_hash
         self.transaciton_list=transaciton_list
      
         self.block_data="______________".join(transaciton_list) + "______________" + previous_block_hash
         self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()
    
a1 = "luey sends 7 LC to his teacher"
a2 = "luey sends 3.7 LC to his brother"
a3 = "luey's teacher sends 15.2 LC to his son"
a4 = "luey sends 100 LC to his university"

<<<<<<< HEAD
initial_block = LueyCoinBlock("Initial string", [a1, a2])#1.blok oluşturduk
=======
initial_block = LueyCoinBlock("Initial string", [a1, a2])
>>>>>>> parent of 70c9e22 (Update porje.py)
 
print(initial_block.block_data)
print(initial_block.block_hash)

second_block = LueyCoinBlock("Initial string", [a3, a4])
 
print(second_block.block_data )
print(second_block.block_hash)