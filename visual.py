def print_tex(l:list, boxlength, file):
    '''
    Input: a list of lists l containing integers (a.k.a a youngtableau), an integer "boxlength" and a string 'filename'
    Output: A file containing LaTeX data for a diagram of the young tableau with specified entries and boxlength
    '''
    a = boxlength
    size = a * (max(len(l), len(max(l, key=lambda x: len(x)))) + 2)
    if 1 < a < 3:
        fsize = 25
    elif a <= 1:
        fsize = 10
    elif a >= 3:
        fsize = 50

    header = r'''﻿\documentclass{article}

\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage{geometry}
\geometry{papersize={''' + str(size) + 'cm,' + str(size) + 'cm},total={' + str(size-a) + 'cm,' + str(size-a) + r'''cm}}

\begin{document}\begin{figure}
   \tikzset{
      tick/.style = {black, very thick}
    }

\begin{tikzpicture}
'''

    footer = r'''\end{tikzpicture}
\end{figure}
\end{document}
'''

    main = ''

    for i in range(len(l)):
        y = i * a
        for j in range(len(l[i])):
            x = j * a
            main += r'''\draw [ultra thick] (''' + str(x) + ',' + str(y) + ') rectangle (' + str(x + a) + ',' + \
                    str(y + a) + ');\n'
            main += r'''\node at ($(''' + str(x) + ',' + str(y) + ')+(' + str(a/2) + ',' \
                    + str(a/2) + r''')$) {\fontsize{''' + str(fsize) + '}{8}$' + str(l[i][j]) + '$};\n'

    content = header + main + footer

    with open(file, mode='w', encoding='utf-8') as f:
        f.write(content)


#print_tex([[5, 6], [4, 4, 6, 6], [2, 3, 5, 5], [1, 2, 2, 3, 3, 5]], 15, 'new_file.tex')
#v = '5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5'
