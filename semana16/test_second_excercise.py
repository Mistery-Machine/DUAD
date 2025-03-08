from function_test import suma_numeros
from function_test import busqueda_letras
from function_test import primera_funcion

def test_function_sum_numbers_list():
  #arrange
  number_input=[1,2,3,4,5]
  desire_ouput=15

  #act
  result= suma_numeros(number_input)

  #assert
  assert  result== desire_ouput

def test_function_sum_numbers_empty_list():
  #second arrange
  number_input = []
  desire_ouput = 0

  #act
  result = suma_numeros(number_input)

  #assert
  assert result == desire_ouput

def test_function_sum_numbers_negative_numbers_list():
  #third arrange 
  number_input = [-1,-2,-3,-4,-5]
  desire_ouput = -15

  #act
  result = suma_numeros(number_input)

  #assert
  assert result == desire_ouput

def test_function_upper_lower_letter():

  #arrange
  text="Hola soy Daniel"
  desired_upper=2
  desired_lower=11

  #act
  upper_count, lower_count = busqueda_letras(text)


  #assert
  assert upper_count==desired_upper
  assert lower_count==desired_lower

def test_function_all_lower_letter():
  # segundo arrange
  text="hola soy daniel"
  desired_upper=0
  desired_lower=13
  
  #act
  upper_count, lower_count = busqueda_letras(text)


  #assert
  assert upper_count==desired_upper
  assert lower_count==desired_lower

def test_function_all_capital_letter():
  #tercer arrange 
  text="HOLA SOY DANIEL"
  desired_upper=13
  desired_lower=0
  
  #act
  upper_count, lower_count = busqueda_letras(text)

  #assert
  assert upper_count==desired_upper
  assert lower_count==desired_lower

def test_function_print_string_backward():
  #arrange
  text="Hello world"
  desired_text="dlrow olleH"

  #act
  result= primera_funcion(text)

  #assert
  assert result==desired_text

def test_function_print_empty_string():
  #segundo arrange
  text=""
  desired_text=""

  #act
  result = primera_funcion(text)

  #assert
  assert result == desired_text

def test_function_print_one_letter():
  #tercer arrange
  text="A"
  desired_text="A"

    #act
  result = primera_funcion(text)

  #assert
  assert result == desired_text





