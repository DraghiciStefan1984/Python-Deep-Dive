import pytest
from app.models.inventory import Resource, CPU


############ for Resource
@pytest.fixture
def resource_values():
    return {'name': 'Parrrot', 
            'manufacturer': 'Pirates', 
            'total': 100, 
            'allocated': 50}
    
@pytest.fixture
def resource(resource_values):
    return Resource(**resource_values)

def test_create_resource(resource_values, resource):
    for attr_name in resource_values:
        assert getattr(resource, attr_name)==resource_values.get(attr_name)
        
def test_create_invalid_allocated_type():
    with pytest.raises(TypeError):
        Resource('name', 'menu', 10, 12.5)
        
def test_create_invalid_total_value():
    with pytest.raises(TypeError):
        Resource('name', 'menu', -10, 0)
        
@pytest.mark.parametrize('total, allocated', [(10, -5), (10, 20)])
def test_create_invalid_allocated_value(total, allocated):
    with pytest.raises(TypeError):
        Resource('name', 'menu', total, allocated)
        

############# for CPU      
@pytest.fixture
def cpu_values():
    return {'name': 'Intel i9', 
            'manufacturer': 'Intel', 
            'total': 10, 
            'allocated': 4,
            'cores':8,
            'socket': 'Socket',
            'power_watts':250}
    
@pytest.fixture
def cpu(cpu_values):
    return CPU(**cpu_values)

def test_create_cpu(cpu_values, cpu):
    for attr_name in cpu_values:
        assert getattr(cpu, attr_name)==cpu_values.get(attr_name)
        
@pytest.mark.parametrize('cores', 'exception', [(10.5, TypeError), (-1, ValueError), (0, ValueError)]):
def test_invalid_cores(cores, exception, cpu_values):
    cpu_values['cores']=cores
    with pytest.raises(exception):
        CPU(**cpu_values)