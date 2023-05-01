# Layout:
# 1) Exercise
#       a) Item
#       b) Item
# 2) Exercise
#       a) Item

# Run with:
# python3 compile.py practica1.tex
#
# For font installation check:
# https://tex.stackexchange.com/questions/88423/manual-font-installation

import os
import sys

input_filename = sys.argv[1]
compilation_style = sys.argv[2]

if compilation_style == 'docente':
    os.system("pdflatex -synctex=1 -interaction=nonstopmode %s" %input_filename)
    exit()


output_filename = input_filename.replace('.tex','_ready.tex')
answers_dict = {} 
output_string = ''

input_lines = open(input_filename).readlines()

exercise_id = 0
for line in input_lines:
    arr = line.split()

    if len(arr) == 0:
        continue

    elif arr[0] == '\\exercise':
        exercise_id += 1
        item_id = 0
        answers_dict[exercise_id] = {}
        output_string += line

    elif arr[0] in ['\\item', '\\Item']:
        item_id += 1
        answers_dict[exercise_id][item_id] = ''
        output_string += line

    elif arr[0] == '\\answer':
        answers_dict[exercise_id][item_id] = line

    elif arr[0] == '\\end{document}':
        continue

    else:
        output_string += line

output_string += '\\vspace{20pt} \n \\textbf{Respuestas}'
output_string += '\\begin{enumerate}'
for exercise in answers_dict.keys():
    output_string += '\\exercise'
    if ''.join([answer for answer in answers_dict[exercise].values()]) == '': #no answers in all items
        output_string += '---'
    else:
        output_string += '\\begin{enumerate} [label=(\\alph*)]'
        for answer in answers_dict[exercise].values():
            if answer == '':
                output_string += '\\item ---'
            else:
                output_string += answer.replace('\\answer', '\\item')
        output_string += '\\end{enumerate}'

output_string += '\\end{enumerate}'
output_string += '\\end{document}'


print(answers_dict)
file_output = open(output_filename,'w')
file_output.write(output_string)
file_output.close()

os.system("pdflatex -synctex=1 -interaction=nonstopmode %s" %output_filename)
#os.system("pdflatex -synctex=1 %s" %output_filename)