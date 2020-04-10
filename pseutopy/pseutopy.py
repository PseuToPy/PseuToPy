import ast

from textx import metamodel_from_file


# TODO: Function Calls
# TODO: Then, the only missing aspect will be lists
# TODO: But we could create expressions that are methods and see how that goes

def main():
    program = """
    set a, b to 1 + 2 - True * a < b, 3
    set c to ()

    input("Hello")

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

    def fizz(a):
        return None
    end
    def fizz():
        return 1
    end
    def fizz with no parameter to do:
        print("Hello")
    end
    define function fizz with a as parameter to do:
        return a
    end
    define function fizzbuzz with a, b as parameters:
        return b
    end
    define function fizzbuzz with (a,b,c) as parameters to do  :
        return 1
    end

    call function fizzbuzz
    call function fizzbuzz with a as parameter
    call function fizzbuzz with (a, b) as parameters
    set a to (a, b, c)
    set a to the result of call function fizzbuzz with a, b as parameters
    """

    meta_model = metamodel_from_file('pseudocode.tx', debug=False)
    model = meta_model.model_from_str(program)
    for statement in model.statements:
        print(statement)


if __name__ == '__main__':
    main()
