## The Exercise
#### Focus: to practice the TDD, red green refactor flow.

#### The red green refactor steps:
* Write a unit test that fails.
* Update code to make tests pass.
* Clean up, refactor.

#### Hints:
Unlike in the string calculator exercise, the steps are not clearly set out for you here. Nonetheless, break your problem into the smallest, simplest steps and always keep in mind the focus of the red-green-refactor. One recommendation is to solve with a limited set of roman numeral characters initially and extend it from there.

## The Problem
“As a Roman Bookkeeper I want to add Roman numbers because doing it manually is too tedious.” 

Given the Roman numerals, (IVXLCDM which means one, five, ten, fifty, hundred, fivehundred and a thousand respectively), create two numbers and add them. As we are in Rome there is no such thing as an integer, we need to do this with the strings (so try to solve this without ever converting inputs to their int representation). An example would be “XIV” + “LX” = “LXXIV”

There are some rules to a Roman number:

Numerals can be concatenated to form a larger numeral (“XX” + “II” = “XXII”)
If a lesser numeral is put before a bigger it means subtraction of the lesser from the bigger (“IV” means four, “CM” means ninehundred)
If the numeral is I, X or C you can’t have more than three (“II” + “II” = “IV”)
If the numeral is V, L or D you can’t have more than one (“D” + “D” = “M”)

Sample inputs and outputs:
  add('I', 'II') =  'III'
  add('II', 'II') =  'IV'
  add('III', 'II') = 'V'
  add('IV', 'I') = 'V'
  add('V', 'I') = 'VI'
  add('I', 'V') =  'VI'
  add('V', 'V') =  'X'
  add('V', 'IV') = 'IX'
  add('VIII', 'I') =  'IX'
  add('IX', 'I') = 'X'
  add('X', 'I') = 'XI'
  add('I', 'X') = 'XI'
  add('X', 'V') = 'XV'
  add('V', 'X') = 'XV'
  add('X', 'X') = 'XX'

## References
 * http://codingdojo.org/kata/RomanCalculator/
