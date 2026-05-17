# Project: Making Shopping Smart
# COSC 40503 - Artificial Intelligence


## Files
This project subdirectory contains a number of files you'll edit or run:\

-   `addition.py`: source file for question 1

-   `buyLotsOfFruit.py`: source file for question 2

-   `shop.py`: source file for question 3

-   `shopSmart.py`: source file for question 3

-   `town.py`: source file for question 4

-   `shopAroundTown.py`: source file for question 4

-   `autograder.py`: autograding script (see below)

and others you can ignore:

-   `test_cases`: directory contains the test cases for each question

-   `grading.py`: autograder code

-   `testClasses.py`: autograder code

-   `tutorialTestClasses.py`: test classes for this particular project

-   `projectParams.py`: project parameters

The command `python3 autograder.py` grades your solution to all three problems. If it is run before editing any files you get a page or two of output:

```text 
userid@linux:~/project-1$ python3 autograder.py 
Starting on 6-20 at 13:41:08

Question q1
===========

*** FAIL: test_cases/q1/addition1.test
***     add(a,b) must return the sum of a and b
***     student result: "0"
***     correct result: "2"
*** FAIL: test_cases/q1/addition2.test
***     add(a,b) must return the sum of a and b
***     student result: "0"
***     correct result: "5"
*** FAIL: test_cases/q1/addition3.test
***     add(a,b) must return the sum of a and b
***     student result: "0"
***     correct result: "7.9"
*** Tests failed.

### Question q1: 0/1 ###


Question q2
===========

*** FAIL: test_cases/q2/food_price1.test
***     buyLotsOfFruit must compute the correct cost of the order
***     student result: "0.0"
***     correct result: "12.25"
*** FAIL: test_cases/q2/food_price2.test
***     buyLotsOfFruit must compute the correct cost of the order
***     student result: "0.0"
***     correct result: "14.75"
*** FAIL: test_cases/q2/food_price3.test
***     buyLotsOfFruit must compute the correct cost of the order
***     student result: "0.0"
***     correct result: "6.4375"
*** Tests failed.

### Question q2: 0/1 ###


Question q3
===========

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
*** FAIL: test_cases/q3/select_shop1.test
***     shopSmart(order, shops) must select the cheapest shop
***     student result: "None"
***     correct result: ""
Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
*** FAIL: test_cases/q3/select_shop2.test
***     shopSmart(order, shops) must select the cheapest shop
***     student result: "None"
***     correct result: ""
Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
Welcome to shop3 fruit shop
*** FAIL: test_cases/q3/select_shop3.test
***     shopSmart(order, shops) must select the cheapest shop
***     student result: "None"
***     correct result: ""
*** Tests failed.

### Question q3: 0/1 ###


Question q4
===========

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
Welcome to shop3 fruit shop
*** FAIL: test_cases/q4/find_route1.test
***     shopAroundTown(orders, fruitTown, price) must select the best route
***     student result: "None"
***     correct result: "['shop1', 'shop2', 'shop3']"
Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
Welcome to shop3 fruit shop
*** FAIL: test_cases/q4/find_route2.test
***     shopAroundTown(orders, fruitTown, price) must select the best route
***     student result: "None"
***     correct result: "['shop1', 'shop3']"
Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
Welcome to shop3 fruit shop
*** FAIL: test_cases/q4/find_route3.test
***     shopAroundTown(orders, fruitTown, price) must select the best route
***     student result: "None"
***     correct result: "['shop2']"
*** Tests failed.

### Question q4: 0/1 ###


Finished at 13:41:08

Provisional grades
==================
Question q1: 0/1
Question q2: 0/1
Question q3: 0/1
Question q4: 0/1
------------------
Total: 0/4

Your grades are NOT yet registered.  To register your grades, make sure
to follow your instructor's guidelines to receive credit on your project.
```

For each of the three questions, this shows the results of that question's tests, the questions grade, and a final summary at the end. Because you haven't yet solved the questions, all the tests fail. As you solve each question you may find some tests pass while other fail. When all tests pass for a question, you get full marks. Looking at the results for question 1, you can see that it has failed three tests with the error message `"add(a,b) must return the sum of a and b"`. The answer your code gives is always 0, but the correct answer is different. We will fix that in the next tab.


# Questions

# Question 1: Addition

Open `addition.py` and look at the definition of add:

``` python
def add(a, b):
    "Return the sum of a and b"
    "*** YOUR CODE HERE ***"
    return 0
```

The tests called this with a and b set to different values, but the code always returned zero. Modify this definition to read:

``` python
def add(a, b):
    "Return the sum of a and b"
    print("Passed a={} and b={}, returning a+b={}".format(a,b,a+b))
    return a+b
```

Now rerun the autograder (omitting the results for questions 2 and 3):

``` text
userid@linix:~/tutorial$ python3 autograder.py -q q1
Starting on 1-21 at 23:52:05

Question q1
===========
Passed a=1 and b=1, returning a+b=2
*** PASS: test_cases/q1/addition1.test
***     add(a,b) returns the sum of a and b
Passed a=2 and b=3, returning a+b=5
*** PASS: test_cases/q1/addition2.test
***     add(a,b) returns the sum of a and b
Passed a=10 and b=-2.1, returning a+b=7.9
*** PASS: test_cases/q1/addition3.test
***     add(a,b) returns the sum of a and b

### Question q1: 1/1 ###

Finished at 23:41:01

Provisional grades
==================
Question q1: 1/1
Question q2: 0/1
Question q3: 0/1
Question q4: 0/1
------------------
Total: 1/4
```

You now pass all tests, getting full marks for question 1. Notice the new lines `"Passed a=..."` which appear before `"*** PASS: ...`. These are produced by the print statement in `add`. You can use print statements like that to output information useful for debugging. You can also run the autograder with the option `–mute` to temporarily hide such lines, as follows:

``` text
userid@linux:~/tutorial$ python3 autograder.py -q q1 --mute 
Starting on 1-22 at 14:15:33

Question q1
===========
*** PASS: test_cases/q1/addition1.test
***     add(a,b) returns the sum of a and b
*** PASS: test_cases/q1/addition2.test
***     add(a,b) returns the sum of a and b
*** PASS: test_cases/q1/addition3.test
***     add(a,b) returns the sum of a and b

### Question q1: 1/1 ###
```


## Question 2: buyLotsOfFruit function

Add a `buyLotsOfFruit(orderList)` function to `buyLotsOfFruit.py` which takes a list of `(fruit,pound)` tuples and returns the cost of your list. If there is some `fruit` in the list which doesn't appear in `fruitPrices` it should print an error message and return `None`. Please do not change the `fruitPrices` variable.

Run `python3 autograder.py` until question 2 passes all tests and you get full marks. Each test will confirm that `buyLotsOfFruit(orderList)` returns the correct answer given various possible inputs. For example, `test_cases/q2/food_price1.test` tests whether:

``` text
Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
```


## Question 3: shopSmart function

Fill in the function `shopSmart(orders,shops)` in `shopSmart.py`, which takes an `orderList` (like the kind passed in to `FruitShop.getPriceOfOrder`) and a list of `FruitShop` and returns the `FruitShop` where your order costs the least amount in total. Don't change the file name or variable names, please. Note that provided to you is the `shop.py` implementation as a "support" file, so you don't need to submit yours.

Run `python3 autograder.py` until question 3 passes all tests and you get full marks. Each test will confirm that `shopSmart(orders,shops)` returns the correct answer given various possible inputs. For example, with the following variable definitions:

``` python
orders1 = [('apples',1.0), ('oranges',3.0)]
orders2 = [('apples',3.0)]       
dir1 = {'apples': 2.0, 'oranges':1.0}
shop1 =  shop.FruitShop('shop1',dir1)
dir2 = {'apples': 1.0, 'oranges': 5.0}
shop2 = shop.FruitShop('shop2',dir2)
shops = [shop1, shop2]
```

`test_cases/q3/select_shop1.test` tests whether:
`shopSmart.shopSmart(orders1, shops) == shop1` and

`test_cases/q3/select_shop2.test` tests whether:
`shopSmart.shopSmart(orders2, shops) == shop2`

## Question 4: shopAroundTown
The `shopAroundTown(orderList, fruitTown, gasCost)` function takes as input a list of `(fruit, numPounds)` pairs as in question 3, a town object, and a number representing the cost of gas per mile traveled, and determines the best route to take to fill the fruit order. A town object contains a list of shops and the distances between each pair of shops and from each shop to 'home' in miles. See the documentation in the file `town.py` for a more detailed description of the representation of a town object. A valid route must start and end at home, so function returns a list of shops such that the sum of the total gas cost accrued from starting at home, going to each shop in the list in order, and returning to home, plus the total cost of buying the necessary fruit at the stores on the list, is minimized.

This question has a few more working parts than the previous three. Fortunately, provided is an implementation of the solution! Unfortunately, it doesn't work.

The approach is simple: start with our list of all shops in town. Get all subsets of this list of shops, and filter the list of subsets to only contain subsets of shops that are carrying all the fruit we are trying to purchase. Then make a list of all permutations of all of these subsets (i.e. all possible routes through all possible valid choices of stores) and return the one which allows us to fill our order for the lowest cost. It's not the most clever algorithm (it checks O($n! \times 2^n$) routes where $n$ is the number of shops), but it gets the job done.

Using your newly acquired debugging skills, find the bugs in `shopAroundTown.py`. You should not have to make any major changes (specifically, there are four small changes, none of which require you to add or remove any lines). Bugs may be in the functions `shopAroundTown, getAllSubsets, and getAllPermutations`.

Try to find the bugs on your own; it's good practice for the later projects. If you get stuck though, highlight here for a hint: Put breakpoints at lines 44, 58, 71, and 75.

Do not change the file name or function names, please. Note that provided the `town.py` implementation as a \"support\" file, so you do not need to submit yours.

Run `python3 autograder.py` until question 4 passes all tests and you get full marks. Each test will confirm that `shopAroundTown(orderList, fruitTown, gasCost)` returns the correct answer given various possible inputs.

