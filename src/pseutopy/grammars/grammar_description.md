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

| Symbol | Description                                                                      |
|--------|----------------------------------------------------------------------------------|
| '...'  | Matches the string within the quotes.                                            |
| \|     | Defines a ordered sequence of choices.                                           |
| ?      | Defines an optional rule that will not fail if not respected.                    |
| +      | Defines a rule that can be present one or several times.                         |
| *      | Defines a rules that can be present zero or several times.                       |
| [   ]  | According to Wikipedia, this defines an optional rule.                           |
| .      | It seems that it is used in conjunction of two rules, one of them being optional |
| ~      | Defines a sequence where, if a ~ b, a must be true in order to evaluate b.       |
| !      | Negative lookahead that succeeds if what comes after the symbol is not matched.  |
| &      | Positive lookahead that succeeds if what comes after the symbol is matched.      |

This table might not be completely accurate. For example, why do we use both `[]` and `?` if they both mean
that a rule is optional? Surely, there is an explanation to that.

## Statements and Expressions

In Python (and in other programming languages), there is a distinction between _statements_ and _expressions_.
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

