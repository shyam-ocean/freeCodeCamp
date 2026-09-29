"""creating a function that takes a list of math problems written as strings
(like "32 + 698") and arranges them the way we write them on paper."""

def arithmetic_arranger(problems, show_answers=False):

    # Rule 1 for more than 5 problems allowed
    if len(problems) > 5:
        return 'Error: Too many problems.'

    #four empty lists, one for each output row
    line_1= []    # top no
    line_2=[]   #   operator+ bottom no
    line_dash=[]   
    result_line =[]     #results

    for problem in problems:
        # split "a+b" into ["a","+" ,"b"]
        first_num, operator, second_num = problem.split()

        # rule 2 for operators
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        #rule 3 -must contain only digits
        if not first_num.isdigit() or not second_num.isdigit():
            return 'Error: Numbers must only contain digits.'

        # rule 4 for length of numbers(at most 4 digits)
        if len(first_num) >4 or len(second_num) >4:
            return 'Error: Numbers cannot be more than four digits.'

        # column width= longest number + 2(operator and space)
        width = max(len(first_num), len(second_num)) + 2

        #align each line to the column width
        line_1.append(first_num.rjust(width))
        line_2.append(operator + second_num.rjust(width -1))
        line_dash.append('-'* width)

        # calculation if show_answers is True
        if show_answers:
            if operator == '+':
                output=int(first_num) +int(second_num)
            else:
                output= int(first_num)-int(second_num)
            result_line.append(str(output).rjust(width))

    # join problems side by side with 4 spaces between them
    lines= ['    '.join(line_1),
             '    '.join(line_2),
             '    '.join(line_dash)]

    if show_answers:
        lines.append('    '.join(result_line))

    # Put each row on its line
    return '\n'.join(lines)

# example
if __name__ == '__main__':
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))