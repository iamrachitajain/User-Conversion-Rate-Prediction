# encoding: utf-8
# ******************************************************
# Author       : iamrachitajain
# Email        : raj73@pitt.edu
# Filename     : task1_.py
# Description  : Write structured json for key_metrics. 
# ******************************************************

import re
import time
import json

def read_json_file(file_path):
	"""
	"""
	json_file = open(file_path, 'r')
	data = json.load(json_file)
	return data

def traverse_json_data(json_data):
	"""
	"""
	final_list = list()
	for country in json_data['report']['data']:
		for city in country['breakdown']:
			for product in city['breakdown']:
				meaningful_dict = dict()
				meaningful_dict["country"] = country['name']
				meaningful_dict["city"] = city['name']
				meaningful_dict["product_name"] = product['name']
				meaningful_dict["page_views"] = product["counts"][0]
				meaningful_dict["visits"] = product["counts"][1]
				final_list.append(meaningful_dict)

	return final_list

def create_json(list_of_dict, file_path):
	"""

	"""
	with open(file_path, 'w') as fout:
		json.dump(list_of_dict , fout)

def main(ip_file_path, out_file_path):
	start = time.time()
	json_data = read_json_file(ip_file_path)
	list_of_dict = traverse_json_data(json_data)
	sample_file = create_json(list_of_dict, out_file_path)
	end = time.time()
	return (end - start)

if __name__=='__main__':
	print(main('../data/products.json', '../data/sample.json'))
