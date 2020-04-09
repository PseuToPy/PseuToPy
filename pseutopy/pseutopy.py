import ast

from textx import metamodel_from_file


# TODO: Input, Function Calls
# TODO: Then, the only missing aspect will be lists
# TODO: But we could create expressions that are methods and see how that goes

def main():
    program = """
    set a, b to 1 + 2 - True * a < b, 3
    set c to ()

    a = 1
    declare bix

    for i in range(0):
        for j in range(0, 10):
            for k in range(0, 10, 1):
                set a to None
                declare b, c, d
                print(1, "Hello", True)
                print(1 + True)
                print "Hello" + "world"
                print "Hello" followed by a followed by "my friend" + "Bob"
                if a == b:
                    set a to b
                end
            end
        end
    end

    if a is greater than b then
        if b is lower than c then:
            if d is lower than e then     :
                set f to the result of input integer ("Hi")
                set b to the result of input number("hello")
                set a to the result of input("hello")
                if e is equal to f:
                    a = 2
                    b = 3
                end
            end
        end
    end

    if True:
        a = 1
    else if True:
        b = 2
    elif True:
        c = 3
    else if True:
        d = 4
    else:
        e = 5
    end

    def fizz with arguments (a, b, c) as :
        a = None
        b = 1
        return (b, c)
    end

    """

    meta_model = metamodel_from_file('pseudocode.tx', debug=True)
    model = meta_model.model_from_str(program)
    for statement in model.statements:
        print(statement)


if __name__ == '__main__':
    main()
