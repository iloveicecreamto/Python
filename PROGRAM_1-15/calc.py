# calc.py --> for calculator.py


def addition(a,b):
  return a + b


def subtraction(a,b):
  return a - b


def multiplication(a,b):
  return a * b


def division(a,b):
  try:
    return a / b
  except ZeroDivisionError as e:
    print("!!!! Error: ",e )


