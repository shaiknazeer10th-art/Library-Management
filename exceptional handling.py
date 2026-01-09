# divide by zero exception handling example
try:
  result = 10 / 2
  print(result)
except ZeroDivisionError:
   print("error: cannot divide by zero.")
except ValueError:
   print("error: invalid value provided.")
else:
   print("division successful.")
finally:
   print("execution completed.")
  