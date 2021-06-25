# encoding: utf-8
# ******************************************************
# Author       : iamrachitajain
# Email        : raj73@pitt.edu
# Filename     : task1_.py
# Description  : Write structured json for key_metrics. 
# ******************************************************

import re
import json
import time
import datetime

def read_json_file(file_path):
	"""
	"""
	json_file = open(file_path, 'r')
	data = json.load(json_file)
	return data

def date_string_to_datetime(dtstr):
	"""
	Converts date string to python datetime object
	Arguments:
		dtstr: str
	Returns:
		datetime object

	"""
	dtstr = re.sub('[^A-Za-z0-9]+', '', dtstr)
	datetime_object = datetime.datetime.strptime(dtstr, '%a%d%b%Y')
	datetime_object = datetime_object.strftime('(%Y,%m,%d)')
	return datetime_object

def create_meaningful_dict(json_data):
	"""
	"""
	final_list = list()
	for item in json_data['report']['data']:
		meaningful_dict = dict()
		meaningful_dict["date"] = date_string_to_datetime(item['name'])
		meaningful_dict["page_views"] = item['counts'][0]
		meaningful_dict["visits"] = item['counts'][1]
		meaningful_dict["unique_visitors"] = item['counts'][2]
		meaningful_dict["bounce_rate"] = item['counts'][3]
		final_list.append(meaningful_dict)
	return final_list

def create_json(list_of_dict, file_path):
	"""

	"""
	with open(file_path, 'w') as fout:
		json.dump(list_of_dict , fout)

def main(ip_file_path, out_file_path):
	start = time.time()
	data = read_json_file(ip_file_path)
	meaningful_dict = create_meaningful_dict(data)
	sample_file = create_json(meaningful_dict, out_file_path)
	end = time.time()
	return (end - start)

if __name__=='__main__':
	print(main('../data/key_metrics.json', '../data/sample.json'))