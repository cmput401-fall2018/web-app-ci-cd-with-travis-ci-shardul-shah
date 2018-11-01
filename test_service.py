from mock import patch
from service import Service

#check if this is correct with TA/CH/LZ/G

@patch("service.Service.divide", return_value = 2)
def test_divide(divide):

	newService = Service()
	assert newService.divide(1) == 

test_bad_random()

