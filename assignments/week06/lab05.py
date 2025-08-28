""" เขียน function ชื่อ count_vowels_consonants ที่มีคุณสมบัติดังนี้:

รับ parameter text เป็น string
นับสระ (a, e, i, o, u) และพยัญชนะ (ไม่นับช่องว่างและตัวเลข)
return dictionary ที่มี vowels และ consonants counts
ไม่สนใจตัวใหญ่ตัวเล็ก (case insensitive) """

def count_vowels_consonants(text):
   text=text.replace(" ","")
   text=text.lower()
   number=text.count('1')+text.count('2')+text.count('3')+text.count('4')+text.count('5')+text.count('6')+text.count('7')+text.count('8')+text.count('9')+text.count('0')
   vowels=text.count('a')+text.count('e')+text.count('i')+text.count('o')+text.count('u')
   consonants=(len(text)-vowels)-number
   return{
      "Vowels":vowels,
      "Consonants":consonants
   }