import os


class ExceptionHandler:
    def __init__(self, request, textx_exception, meta_model):
        self.tokenized_request = self.__tokenize_request(request)
        self.failed_part = self.__locate_failed_part(textx_exception)
        self.statements = self.__getstatements(meta_model)

    def __locate_failed_part(self, textx_exception):
        """
        Find the word which made the error

        :return: the word and previous word besides the error
        """
        count = 0
        error_line = self.tokenized_request[int(textx_exception.line-1)]
        for i in range(0, len(error_line)):
            count += len(error_line[i]) + 1
            # print("Count etape " + str(i) + ": " + str(count))
            if count >= int(textx_exception.col):
                return i-1, i

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
                line += [token]
        tokenized_request += [line]
        return tokenized_request

    def __getstatements(self, meta_model):
        """
        Retrieves the statements keyword defined from the grammar.
        Need to adapt with language later

        :return: dict of {Statement_class: keywords}
        """
        with open(os.path.dirname(__file__) + "/pseudocode.tx", 'r') as f:
            grammar = ""
            for line in f.readlines():
                grammar += line
            record = False
            statements = {}
            for stmt in ["ExprStmt", "InputStmt", "FuncCallStmt", "DeclareStmt", "PrintStmt", "DelStmt", "IfStmt", "WhileStmt", "ForStmt", "FuncDef", "ReturnStmt"]:
                x = meta_model.__dict__.get('user_classes').get(stmt)._tx_position
                y = meta_model.__dict__.get('user_classes').get(stmt)._tx_position_end
                declaration = grammar[x:y]
                statements[stmt] = []
                keyword = ""
                for c in declaration:
                    if c == '\'':
                        record = not record
                        # Filter
                        if keyword not in ["", ",", "(", "followed by", ")", "number", "integer", "with"]:
                            statements[stmt] += [keyword]
                        keyword = ""
                    if record and c != '\'':
                        keyword += c
            return statements

    def analyze_error(self):
        """
            WIP
        :return:
        """
        print(self.tokenized_request)
        print(self.failed_part)
        if (self.tokenized_request[self.failed_part[0]] or self.tokenized_request[self.failed_part[1]] in self.statements.values()):
            pass