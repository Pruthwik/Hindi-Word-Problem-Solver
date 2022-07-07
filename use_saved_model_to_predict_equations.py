"""Use saved model to predict the equations for Hindi word problems."""
import os
from convert_data_into_subwords import convert_text_into_subwords
from sys import argv
from re import search


number_pattern = '\d*[,\/\.]?\d+'
basic_operators = ['+', '-', '*', '/']


def read_text_from_file(file_path):
	"""Read text from a file."""
	with open(file_path, 'r', encoding='utf-8') as file_read:
		return file_read.read().strip()


def write_text_to_file(text, file_path):
	"""Write text to file."""
	with open(file_path, 'w', encoding='utf-8') as file_write:
		file_write.write(text)


def convert_into_subwords_write_to_file_and_run_model(input_text, model_path):
	"""Convert text into subwords, write into a file and run the model."""
	text_in_subwords, dict_special_actual_nums = convert_text_into_subwords(input_text)
	write_text_to_file(text_in_subwords, 'temp-subwords.txt')
	os.system('onmt_translate -model ' + model_path + ' -src temp-subwords.txt -output temp-equation.txt')
	return dict_special_actual_nums


def replace_special_tokens_in_equation(equation_components, dict_special_actual_nums):
	"""Replace special number tokens with actual numbers in equation."""
	return [dict_special_actual_nums[component] if component in dict_special_actual_nums else component for component in equation_components]


def check_solvability(equation_components):
	"""Check whether an equation is solvable."""
	for component in equation_components[2:]:
		if component in basic_operators:
			continue
		elif search(number_pattern, component):
			continue
		else:
			return False
	return True


def solve_infix_expression(expr):
	"""Solve the infix expression."""
	operators, operands = list(), list()
	final_value = 0
	for char in expr:
		if char in basic_operators:
			operators.append(char)
		elif len(operands) == 2 and operators:
			operand_2 = operands.pop()
			operand_1 = operands.pop()
			operator = operators.pop()
			final_value = str(eval(operand_1 + operator + operand_2))
			operands.append(final_value)
			operands.append(char)
		else:
			operands.append(char)
	if len(operands) == 2 and operators:
		operand_2 = operands.pop()
		operand_1 = operands.pop()
		operator = operators.pop()
		final_value = str(eval(operand_1 + operator + operand_2))
		operands.append(final_value)
	if len(operands) == 1 and not operators:
		final_value = operands.pop()
		return final_value
	else:
		return 0


def main():
	"""Pass arguments and call functions here."""
	text = argv[1]
	model_path = argv[2]
	dict_special_actual_nums = convert_into_subwords_write_to_file_and_run_model(text, model_path)
	print('Question is:', text)
	equation = read_text_from_file('temp-equation.txt')
	equation = equation.replace('▁', '')
	equation_components = equation.split()
	actual_equation_components = replace_special_tokens_in_equation(equation_components, dict_special_actual_nums)
	print('Equation is:', ' '.join(actual_equation_components))
	solvable_flag = check_solvability(actual_equation_components[2:])
	if not solvable_flag:
		print('Can not solve this equation')
	else:
		solution = solve_infix_expression(actual_equation_components[2:])
		print('Solution is:', 'x = ' + str(solution))


if __name__ == '__main__':
	main()
