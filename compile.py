import os
import sys
import re


def process_docente(input_lines, input_filename):
    output_filename = input_filename.replace('.tex', '_docente.tex')

    with open(output_filename, 'w') as file:
        for line in input_lines:
            line = re.sub(r'\\begin\{enumcols\}\[\d+\]', r'\\begin{enumcols}', line)
            if '\\answer' in line:
                line = line.replace('\\answer', '\\textcolor{darkblue}{ \\answer ') + "}"
            file.write(line)

    compile_tex(output_filename)
    remove_temp_files(output_filename)
    return output_filename


def compile_tex(filename):
    os.system(f"TEXINPUTS=../: pdflatex -synctex=1 -interaction=nonstopmode {filename}")


def remove_temp_files(base_filename):
    os.remove(base_filename)
    base_name = os.path.splitext(base_filename)[0]
    for ext in [".aux", ".out", ".synctex.gz", ".log"]:
        temp_file = f"{base_name}{ext}"
        if os.path.exists(temp_file):
            os.remove(temp_file)


def process_student(input_lines, input_filename, suffix="_ready"):
    output_filename = input_filename.replace('.tex', f'{suffix}.tex')
    output_string = ""
    answers_dict = {}
    exercise_id, item_id = 0, 0

    for line in input_lines:
        arr = line.split()
        if not arr:
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
        elif arr[0] != '\\end{document}':
            output_string += line

    output_string += process_answers(answers_dict)
    with open(output_filename, 'w') as file:
        file.write(output_string)

    compile_tex(output_filename)
    remove_temp_files(output_filename)
    return output_filename


def process_answers(answers_dict):
    ans_str = '\\vspace{20pt} \n \\textbf{Respuestas}\\begin{enumerate}'
    for exercise in answers_dict:
        ans_str += '\\exercise'
        items = answers_dict[exercise].values()
        if not any(items):
            ans_str += '---'
        else:
            ans_str += '\\begin{enumerate} [label=(\\alph*)]'
            for answer in items:
                ans_str += '\\item ---' if not answer else answer.replace('\\answer', '\\item')
            ans_str += '\\end{enumerate}'
    ans_str += '\\end{enumerate}\\end{document}'
    return ans_str


def modify_for_celular_mode(lines):
    modified_lines = []
    for line in lines:
        # Replace the document class
        line = line.replace('\\documentclass{template_practica}',
                            '\\documentclass{template_celular_practica}')

        modified_lines.append(line)
    return modified_lines


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 compile.py <filename.tex> <style>")
        sys.exit(1)

    input_filename = sys.argv[1]
    compilation_style = sys.argv[2]

    with open(input_filename, 'r') as file:
        input_lines = file.readlines()

    # Check for the 'celular' compilation style
    output_suffix = "_ready"
    if compilation_style == 'celular':
        input_lines = modify_for_celular_mode(input_lines)
        output_suffix = "_celular"
        compilation_style = 'estudiante'

    if compilation_style == 'docente':
        process_docente(input_lines, input_filename)
    else:
        process_student(input_lines, input_filename, output_suffix)
