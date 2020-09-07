import words, visual, ytmath


class word:
    def __init__(self, string):
        self.string = string
        self.list = list(map(int, string.split()))

    def K1(self, index):
        return word(ytmath.listtostring(ytmath.K1(self.list,index)))


    def K1_inv(self, index):
        return word(ytmath.listtostring(ytmath.K1_inv(self.list, index)))

    def K2(self, index):
        return word(ytmath.listtostring(ytmath.K2(self.list,index)))

    def K2_inv(self, index):
        return word(ytmath.listtostring(ytmath.K2_inv(self.list,index)))

    def YT(self):
        e = youngtableau(word(""))
        for x in self.list:
            e.row_insert(x)
        return e

class youngtableau:
    def __init__(self,word):
        self.w = word
        self.tab = words.parse_word(word.string)

    def visual(self, boxlength, file):
        '''
        :param boxlength: length of the box
        :param file: name of the file to be saved at (write ".tex" in the end of the name)
        This function creates the file .tex with the visualization of the young tableau and saves it in the project folder
        '''
        visual.print_tex(self.tab, boxlength, file)

    def row_insert(self, x):
        '''
        This function inserts x in our young tableau and changes the word accordingly
        '''
        newtab = ytmath.row_insert(self.tab[::-1], x, 0)
        newtab = newtab[::-1]
        newstring = ""
        for row in newtab:
            newstring += ytmath.listtostring(row) + " "
        self.w = word(newstring[:-1])
        self.tab = newtab


    def word(self):
        return self.w


def create_from(row, file):
    '''
    :param row: row of the word in the file
    :param file: name of the file where words are saved (write ".txt" in the end of the name)
    :return: returns element of class youngtableau
    This function creates the element of class youngtableau from the word w(T), which is saved in the "file" in the row number "row"
    '''
    tab = words.parse(row, file)
    string = ''
    for row in tab:
        string += ytmath.listtostring(row) + " "
    string = string[:-1]
    return youngtableau(word(string))


def multiply(S, T):
    '''
    :param S: element of class youngtableau
    :param T: element of class youngtableau
    :return: S*T as defined
    '''
    return ytmath.multiply_tab(S, T)


def mult_classes(w1,w2):
    return word(w1.string + " " + w2.string)


def are_equiv(w1,w2):
    return w1.YT().tab == w2.YT().tab





'''
TESTING INSTANCES

a = "5 6 4 4 6 6 2 3 5 5 1 2 2 3 3 5"
b = "4 6 1 2 3"
c = ytmath.multiply_tab(youngtableau(word(a)),youngtableau(word(b)))
print(ytmath.multiply_tab(youngtableau(word(a)),youngtableau(word(b))).tab)
print(c.w.string)
print(mult_classes(word(a),word(b)).string)
print(are_equiv(c.w, mult_classes(word(a),(word(b)))))

A = youngtableau(word(a))
B = youngtableau(word(b))
tab1 = A.tab
tab2 = B.tab
'''
