# SnoFlake Compiler Project

This project contains a simple compiler and integrated development environment (IDE) for the SnoFlake programming language. SnoFlake is a custom language with a syntax that is translated into C++ for execution.

## Project Files

* **`snoflake_compiler.py`**: This file contains the complete SnoFlake IDE, including:
    * The SnoFlake transpiler logic (tokenization and translation).
    * A `Tkinter`-based graphical user interface with a text editor for writing SnoFlake code and a console for displaying output and errors.
    * Functionality to run the SnoFlake code by transpiling it to C++, compiling the C++ code using `g++`, and then executing the resulting binary.
* **`transpiler.py`**: This file contains only the core transpiler logic for the SnoFlake language. It includes:
    * A dictionary `KEYWORDS` that maps SnoFlake keywords to their C++ equivalents.
    * A `tokenize` function that breaks down SnoFlake code into individual tokens.
    * A `transpile` function that takes a list of tokens and translates them into C++ code.

## SnoFlake Language Basics

The SnoFlake language includes the following keywords and features:

* **`truefalse`**: Translates to `bool` in C++.
* **`integer`**: Translates to `int` in C++.
* **`character`**: Translates to `char` in C++.
* **`nonchanging`**: Translates to `const` in C++.
* **`stoploop`**: Translates to `break` in C++.
* **`option`**: Translates to `case` in C++.
* **`none`**: Used for functions that do not return a value (translates to `void`, except for the `main` function which is translated to `int` as required by C++).
* **`say`**: Used for outputting to the console, similar to `std::cout` in C++. You can use `endl` within a `say` statement for a newline.

## How to Run

To run the SnoFlake IDE:

1.  Make sure you have Python installed on your system.
2.  Save the `snoflake_compiler.py` file.
3.  Open a terminal or command prompt and navigate to the directory where you saved the file.
4.  Run the command: `python snoflake_compiler.py`

This will open the SnoFlake IDE window. You can then write SnoFlake code in the editor, click the "▶ Run" button to execute it, and see the output in the console below. The "🧹 Clear Console" button will clear the output area.

To use the standalone transpiler (`transpiler.py`):

1.  Save the `transpiler.py` file.
2.  You can import the `transpile` function into another Python script and use it to translate SnoFlake code.

    ```python
    from transpiler import tokenize, transpile

    snoflake_code = "integer main() { say \"Hello, SnoFlake!\" endl; return 0; }"
    tokens = tokenize(snoflake_code)
    cpp_code = transpile(tokens)
    print(cpp_code)
    ```

    **Note:** The standalone `transpiler.py` does not handle the extraction of the `main` function or the inclusion of necessary C++ headers. The `snoflake_compiler.py` provides a more complete translation process for runnable code.

## Example SnoFlake Code

```snoflake
integer main() {
  say "Hello from SnoFlake!" endl;
  integer count = 0;
  nonchanging integer limit = 5;

  while (count < limit) {
    say "Count is: " count endl;
    count = count + 1;
    if (count == 3) {
      say "Reached three!" endl;
    }
  }

  return 0;
}
