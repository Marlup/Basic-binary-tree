# Recursive Binary Tree Builder and Search

A Python class for building and searching recursive-binary trees.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Introduction

This Python class, `Tree`, provides a simple way to build binary trees and search for specific values within them. It allows you to construct a binary tree structure and perform value-based searches efficiently.

## Installation

1. Clone this repository to your local machine:

 ```bash
 git clone https://github.com/Marlup/Basic-binary-tree.git
 ```

You can then use the Tree class in your Python project by importing it.
## Usage
Building a Binary Tree
To build a binary tree, create an instance of the Tree class and use the build_tree method, passing a list of values to be inserted into the tree.

```python
  tree = Tree()
  values = [1, 2, 3, 4, 5, 6, 7]
  root = tree.build_tree(values)
```

Searching for a Value
You can search for a value within the binary tree using the search_one_value method.

```python
  result = tree.search_one_value(4)
  if result[0]:
      print(f"Value found at level {result[1]}")
  else:
      print("Value not found in the tree.")
```

## Example
Here's a basic example of how to use the Tree class to build a binary tree and search for a value:

```python
  from binary_tree import Tree

  # Build a binary tree
  values = [1, 2, 3, 4, 5, 6, 7]
  tree = Tree()
  root = tree.build_tree(values)
  
  # Search for a value
  result = tree.search_one_value(4)
  if result[0]:
      print(f"Value found at level {result[1]}")
  else:
      print("Value not found in the tree.")
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
