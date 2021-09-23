#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):

	for i in text:
		c = 0
		if i.isalnum():
			c+=1

		else: continue
	return c



def get_word_length_histogram(text):
#	split_text = text.split(" ")
#	split_word = split_text.split
#	a, b, c, d = 0, 0, 0, 0
#	if
	list = [0, 0, 0, 0, 0]
	c = get_num_letters(text)
	for i in text:
		if c == 1 :
			list[1] += 1
		if c == 2:
			list[2] += 1
		if c == 3 :
			list[3] += 1
		if c == 4 :
			list[4] += 1
		if c == 5 :
			list[5] += 1

	return list




def format_histogram(histogram):
	ROW_CHAR = "*"

	return ""

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"

	return ""


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
