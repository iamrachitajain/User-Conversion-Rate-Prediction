import data
from src.utility import task1_
from src.utility import task2_

if __name__ == '__main__':
	
	task1_time = task1_.main('data/key_metrics.json', 'data/sample_key_metrics.json')
	print("Task 1 completed in {} secs".format(task1_time))
	print("Created the required json file sample_key_metrics.json in data folder.")


	task2_time = task2_.main('data/products.json', 'data/sample_products.json')
	print("Task 2 completed in {} secs".format(task2_time))
	print("Created the required json file sample_products.json in data folder.")