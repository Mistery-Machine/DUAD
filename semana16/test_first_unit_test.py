from bubble_sort_test import bubble_sort

def test_bubble_sort_small_list(): 
  #arrange
  input_list=[3,1,2]
  expected_output=[1,2,3]

  #act
  bubble_sort(input_list)

  #assert
  assert input_list == expected_output

def test_bubble_sort_long_list(): 

  #arrange
  second_list=list(range(100,0,-1))
  desired_output=sorted(second_list)

  #act
  bubble_sort(second_list)

  #assert
  assert second_list==desired_output

def test_bubble_sort_empty_list(): 
  #arrange 
  empty_list=[]
  output_expected=[]

  #act
  bubble_sort(empty_list)

  #assert
  assert empty_list==output_expected

def test_bubble_sort_non_list(): 
  #arrange
  invalid_input=["string", 123, None, 3.14, {1:"a"}]
  for i in invalid_input:
    try:
      bubble_sort(i)
      assert False, f"Expected error on the input: {i}"
    except TypeError: 
      pass



