import os
import re


class ExceptionHandler:
    def __init__(self, request, SE, meta_model):
        self.statements = self.__getstatements(meta_model)
        self.tokenized_request = self.__tokenize_request(request)
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
                # \n is accounted for 2 characters with textx, only counted as 1 with Python
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
        firstworderror = self.tokenized_request[0][self.failed_part[0]]
        lastworderror = self.tokenized_request[0][self.failed_part[1]]
        print(firstworderror, lastworderror)
        if self.failed_part == (0, 0):
            # The error is obviously the only word on the line, see what to do in this case later
            pass
        else:
            if firstworderror.type == lastworderror.type == "Variable":
                return "Syntax error: Missing argument between \'" + firstworderror.word \
                    + "\' and \'" + lastworderror.word + "\'."


class _WordInRequest:
    """
        Private Class to rebuild the request by identifying the type of each word
        Discuss to see if really necessary ? (Other method is <pairObject(type, position)>)
    """

    def __init__(self, word, word_type):
        self.word = word
        self.type = word_type
