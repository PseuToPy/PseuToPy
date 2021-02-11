# Grammar description

- Author: Patrick Wang
- Version: 0.1
- Date: February 10th, 2021

## Introduction

### Objectives of this document

The objective of this document is to describe the rules implemented in the Python 3.9.1 full grammar
specification. We hope that this document will help new developers navigate rapidly between all the rules and
their names as they are detailed in the grammar specification.

A copy of the Python 3.9.1 full grammar specification is available in this project, in
`src/pseutopy/grammars/full_grammar.txt`. Note that by simply going on
https://docs.python.org/3/reference/grammar.html, you will simply end up on the grammar specification of the
latest stable release. Hence the need to actually keep a version of it somewhere.


**Disclaimer**: The grammar that we wish to implement _probably_ will not work for a REPL-type of use-case. As
a consequence, we will consider REPL-type instructions to be out of the scope of this project.

### Syntax and symbols used in the Python 3.9.1 full grammar specification

A comprehensive list is given [here](https://www.python.org/dev/peps/pep-0617/#grammar-expressions). The table
below is just a summary of what is written in this link (for the lazy ones).

| Symbol      | Description                                                    |
|-------------|----------------------------------------------------------------|
| e1 e2       | Matches e1, then matches e2.                                   |
| e1 \| e2    | Matches e1 or r2.                                              |
| ( e )       | Matches e.                                                     |
| [ e ] or e? | Optionally matches e.                                          |
| e*          | Matches zero or more occurrences of e.                         |
| e+          | Matches one or more occurrences of e.                          |
| s.e+        | Matches one or more occurrences of e separated by s.           |
| &e          | Succeeds if e can be parsed, without consuming any input.      |
| !e          | Fails if e can be parsed, without consuming any input.         |
| ~           | Commits to the current alternative, even if it fails to parse. |

Note:

- `s.e+` is identical to `(e (s e)*)`.
- `[ e ]` and `e?` are both used in the grammar, but have the same meaning.
- We are given the following example to illustrate `~`: `rule_name: '(' ~ some_rule ')' | some_alt`. This rule
  means that if a left parenthesis is parsed, then `some_alt` will not be considered even if `some_rule` or
  `)` fail to be parsed. **I actually don't know if there is a similar mechanism in textX**, but what I know
  is that this symbol does not exist in textX.

## Expressions and statements

In Python (and in other programming languages), there is a distinction between _expressions_ and _statements_.
The following paragraphs will be used to describe briefly expressions and statements based on the Python
documentation.

A more detailed description of each rule in the Python grammar specification will be made in dedicated sections.

### Expressions

See [this link](https://docs.python.org/3/reference/expressions.html) for reference.

In Python, an expression simply represents a value (which can itself be the results of several operations).

The documentation uses a bottom-up approach to describe expressions. It starts with `atoms` which are the most
basic elements of expressions. Atoms represents identifiers (e.g., names), literals (e.g., strings and
numbers), and also any value that is enclosed in parentheses, brackets, and curly braces (so basically,
tuples, lists, sets, and dictionaries).

With these atoms, the document then describes:

- How tuples, lists, sets, and dictionaries can be formed (either by giving values or by _comprehension_).
- How we can retrieve some parts of a tuple, list, set, or dictionary (e.g., typically by using slices or a
  subscription).
- Then Sections 6.5 to 6.15 presents all the different types of operations that one can do on expressions
  (with a very well-defined ordering priority).
- How Python orders the evaluation of an expression.
- The operator precedence in Python (from least binding to most binding). If you take a look at the grammar
  specification, you will see that this operator precedence is also visible in the grammar specification as
  the least binding rule makes reference to the next least binding rule and so on.

### Statements

See [this link](https://docs.python.org/3/reference/simple_stmts.html) and [that
one](https://docs.python.org/3/reference/compound_stmts.html) for reference.

In Python, statements are basically any instruction that takes up a line (or several lines). As one can see
with the two links above, there are simple statements (i.e., single-line statements) and compound statements
(i.e., multi-line statements).

Statements usually rely on expressions. This means that it is important to have defined the PseuToPy grammar
for expressions before being able to work on statements. **However**, and as mentioned earlier, PseuToPy
currently does not work with REPL-type instructions. This also means that, as of the time of writing we cannot
directly test expressions with `pytest`.

#### Simple statements

Simple statements are instructions that take a single line. Usually, these consist in:

- Calling a function;
- Assigning values to targets;
- Defining a new value to a target with the augmented assignment operators (e.g., `+=`);
- Several statements that rely on Python keywords (e.g., `pass`, `continue`, `break`, `return`, `del`,
  `import`, etc.);


#### Compound statements

Compound statements comprise control structures (`if`, `for`, and `while`), function and class definitions,
and other instructions such as the `try` or `with` statements. The key point here is that compound statements
have a `suite` which consists in a list of statements that are all indented.

## Expressions

### Atoms

The Python 3.9.1 full grammar specification is given below:

```
atom:
    | NAME
    | 'True' 
    | 'False' 
    | 'None' 
    | '__peg_parser__' 
    | strings
    | NUMBER
    | (tuple | group | genexp)
    | (list | listcomp)
    | (dict | set | dictcomp | setcomp)
    | '...' 
```

This means that the `atom` rule will look for valid matches in the following order:

1. An identifier, which needs to be defined so that it does not collide with the language safe words;
2. `True` and `False`, which are also represented in textX by the built-in type `BOOL`;
3. `None`;
4. `__peg_parser__`


## Statements
