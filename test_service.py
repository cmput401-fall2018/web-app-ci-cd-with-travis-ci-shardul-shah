from mock import patch
from service import Service

#check if this is correct with TA/CH/LZ/G

@patch("service.Service.bad_random")
def test_bad_random(bad_random):

	newService = Service()

	bad_random.return_value = 3
	assert newService.bad_random() == 3

	bad_random.return_value = 0
	assert newService.bad_random() == 0

	bad_random.return_value = 10
	assert newService.bad_random() == 10


@patch("service.Service.bad_random")
def test_divide(bad_random):
	newService = Service()

	bad_random.return_value = 0
	assert newService.divide(1) == 0
	assert newService.divide(-1) == 0

	bad_random.return_value = -5
	assert newService.divide(5) == -1
	assert newService.divide(-5) == 1

	bad_random.return_value = 8
	assert newService.divide(-2) == -4
	assert newService.divide(2) == 4
	
	assert newService.divide(10) == 8/10
	assert newService.divide(-10) == -8/10

	try:
		divide(0)
	except ZeroDivisionError:
		assert True	


def test_abs_plus():
	newService = Service()

	assert newService.abs_plus(-10) == (abs(-10) + 1)
	assert newService.abs_plus(10) == (abs(10) + 1)
	assert newService.abs_plus(0) == (abs(0) + 1)
	assert newService.abs_plus(3.14) == (abs(3.14) + 1)

test_abs_plus()

@patch('service.Service.bad_random')
@patch('service.Service.divide')
def test_complicated_function(divide, bad_random):
	newService = Service()

	bad_random.return_value = 6
	divide.return_value = 3

	assert newService.complicated_function(2)[0] == 3
	assert newService.complicated_function(2)[1] == 6%2

	bad_random.return_value = 6
	divide.return_value = -3

	assert newService.complicated_function(-2)[0] == -3
	assert newService.complicated_function(-2)[1] == 6%-2

	divide.return_value = 0
	bad_random.return_value = 0

	assert newService.complicated_function(6)[0] == 0
	assert newService.complicated_function(6)[1] == 0

	divide.return_value = None
	bad_random.return_value = 4
	try: 
		newService.complicated_function(0)
	except ZeroDivisionError:
		assert True
		divide.return_value = 2
		assert newService.complicated_function(2)[0] == 2
		assert newService.complicated_function(2)[0] == 0





