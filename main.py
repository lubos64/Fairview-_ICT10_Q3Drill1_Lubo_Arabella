from pyscript import display, document

def av_ee(e):
   num1 = float(document.getElementById("grade1").value)
   num2 = float(document.getElementById("grade2").value)
   result = (num1 + num2) / 2

   display(result, target = "averagee", append = False)

   if result >= 75:  #to show the results
        display("Yes!", target = "passed", append = False)

   else:
             display("No...", target = "passed", append = False)
#to put a diffrent result