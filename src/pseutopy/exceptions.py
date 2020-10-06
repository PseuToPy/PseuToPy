import os
import re


class ExceptionHandler:
    """
        -- GLOBAL --
        This class' goal is to bring details on the error made from the user.
        It should be able to recognize typo made from the user, missing arguments, wrong syntaxes, etc...

        -- OPERATION --
        This class must be called in pseutopy.py while trying to build the str. If the build fails, it should
        create an ExceptionHandler object which will analyze the root of the error.
        Calling this class requires 3 arguments:
            - the request called
            - the Textx.SyntaxError
            - the PseuToPy.meta_model

        -- INIT --
        1. Format the request to get rid of excessive white spaces. A request can be converted even if there are 2
        consecutive white spaces for example.
        2. self.statements parameter stores the keyword for each statements using __getstatements(meta_mode) which return
        a dict with the key as the statement type and the value as an array of keywords.
        3. self.tokenized_request stores each word composing the request in a matrix by using
        __tokenize_request(formated_request) private method.
        4. self.exception stores the SyntaxError produced from Textx. There are some valuable information to get.
        Need to analyze deeper.
        5. self.failed_part stores the 2 indexes of the word surrounding the located error from the Textx exception.

        -- WIP --
        analyze_error() function should return the identified error and the expected output within a message. Right now,
        It only "detect" one case which is when the request has 2 consecutive Variables. However, the identifying part
        need to be improved and more cases should be added.
    """
    def __init__(self, request, SE, meta_model):
        formated_request = " ".join(request.split())
        self.statements = self.__getstatements(meta_model)
        self.tokenized_request = self.__tokenize_request(formated_request)
        self.exception = SE
        self.failed_part = self.locate_failed_part()

    def __getstatements(self, meta_model):
        """
        Retrieves the statements keyword defined from the grammar.
        Need to adapt with language later

        :return: dict of {Statement_class: keywords}
        """
        with open(os.path.dirname(__file__) + "/pseudocode.tx", 'r') as f:
            grammar = ""
            for test in f.readlines():
                # \n is accounted for 2 characters with textx, only counted as 1 with Python 3.8
                # Replacing \n by 2 characters solve the count issues
                # Look for cleaner solution later
                grammar += test.replace("\n", "  ")
        statements = {}
        for stmt in ["ExprStmt", "InputStmt", "FuncCallStmt", "DeclareStmt", "PrintStmt", "DelStmt", "IfStmt" \
                , "WhileStmt", "ForStmt", "FuncDef", "ReturnStmt"]:
            x = meta_model.__dict__.get("user_classes").get(stmt)._tx_position
            y = meta_model.__dict__.get("user_classes").get(stmt)._tx_position_end
            declaration = grammar[x:y]
            statements[stmt] = []
            record = False
            keyword = ""
            for c in declaration:
                if (c == "\'"):
                    record = not record
                    if keyword != "" and keyword not in statements[stmt]:
                        statements[stmt] += [keyword]
                        keyword = ""
                if record and c != "\'":
                    keyword += c
        return statements

    def __identify_token(self, token):
        m = re.search("\w+", token)
        if m:
            word = m.group(0)
        else:
            word = token
        for k, v in self.statements.items():
            if word in v:
                return k
        return "Variable"

    def __tokenize_request(self, request):
        """
        Tokenize the inputted request

        :param request: inputted request
        :return: list of words contained by the request
        """
        tokenized_request = []
        line = []
        splitted_request = request.split(" ")
        for token in splitted_request:
            if "\n" in token:
                tokenized_request += [line]
                line = [token[1:]]
            else:
                line += [_WordInRequest(token, self.__identify_token(token))]
        tokenized_request += [line]
        return tokenized_request

    def locate_failed_part(self):
        """
        Find the word which made the error

        :return: the word and previous word besides the error
        """
        count = 0
        error_line = self.tokenized_request[int(self.exception.line - 1)]
        for i in range(0, len(error_line)):
            count += len(error_line[i].word) + 1
            # print("Count etape " + str(i) + ": " + str(count))
            if count >= int(self.exception.col):
                if i == 0:
                    return i, i
                else:
                    return i - 1, i

    def analyze_error(self):
        """
            WIP
        :return:
        """
        first_word_error = self.tokenized_request[0][self.failed_part[0]]
        last_word_error = self.tokenized_request[0][self.failed_part[1]]
        print(first_word_error, last_word_error)
        if self.failed_part == (0, 0):
            # The error is obviously the only word on the line, see what to do in this case later
            pass
        else:
            if first_word_error.type == last_word_error.type == "Variable":
                return "Syntax error: Missing argument between \'" + first_word_error.word \
                    + "\' and \'" + last_word_error.word + "\'."


class _WordInRequest:
    """
        Private Class to rebuild the request by identifying the type of each word
        Discuss to see if really necessary ? (Other method is <pairObject(type, position)>)
    """

    def __init__(self, word, word_type):
        self.word = word
        self.type = word_type
