# Unittests and Integration Tests

||
| ---------- |
|![f088970b450e82c881ea](https://github.com/the1Riddle/alx-interview/assets/125451537/adb52b4e-1f1a-4a88-8a2a-eaee7a6ce2a4)|
Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with :

```
  $ python -m unittest path/to/test_file.py
```



