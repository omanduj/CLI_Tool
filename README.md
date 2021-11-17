 Challenge 1
 =======

 How to Run
 -----------

 In order to properly run this project you must first install Poetry, a tool used for dependency management and
 packaging in Python. A link to the installation documents can be found here:
 >https://python-poetry.org/docs/

 Following installation run the command "poetry install" (within the CLI_Combos directory), this will install
 all the project's dependencies.

 In order to run the application you must simply migrate to the correct parent directory (CLI_Combos), then
 execute the following command replacing XXXX with the desired input:
 >python ./challenge_1.py XXXX

  This will cause the program to run, returning all possible combination of values given the specified
  restrictions.

  In order to run tests, migrate to the correct parent directory (CLI_Combos), then execute the following
  command:
 >pytest

 This will execute predefined tests which are located in the CLI_Combos.py file

 Design Decisions
 -----------

 The design decisions taken were used to increase scalability, reliability and maintainability of the program.

 In regards to scalability, if the user has a desire to find the possible combinations of more than 4
 numbers, they would simple be required to add a line to specify accessing a 5th input value in the get_pins
 function (editing the length 4 if statement as well). If the problem statement were to switch from adjacent
 values to other values, simply modifying the dictionary with values that reflect this new schema would
 suffice. The code also lends itself to be easily added to, creating new functions in logic.py to create more
 complicated outputs.

 Reliability was designed via the testing with a range of parameters. The usage of checking if the input is
 length of 4 is used to have program fail gracefully. I used a set in order to verify that all elements
 outputted by my algorithm were equal to what I expected. I then sorted these values, resulting in a list to
 properly display the values in increasing order on the command line. Poetry was also used in order to track
 what versions of software are required to this program function correctly.

 Maintainability was emphasized via the simple coding logic and doc strings. The usage of the dictionary allows
 for very quick look up times to identify the required numbers to complete the calculation. In the get_pins
 function, converting the input of strings to an integer at every required location within the
 itertools.product increases readability. Including the required dependencies allows to identifying outdated
 technology and replace it.

