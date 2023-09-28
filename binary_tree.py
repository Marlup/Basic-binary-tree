class Tree():
    def __init__(self):
        self.tree = None

    def build_tree(self, values):
        self.nodes = 0
        self.levels = 0
        self.tree = self._build_tree(None, values)
        return self.tree
    def _build_tree(self, node, values, level=0):
        if node is None:
            node = Node(values.pop(0))
            self.nodes += 1
            print('Root:', self.levels, '==> build root;', 'Value: ', node.value)
        if self.nodes >= (2**self.levels):
            print(f'{self.nodes} nodes in level {self.levels}')
            self.levels += 1
            self.nodes = 0
        if len(values) != 0:
            value = values.pop(0)
            node.left = Node(value)
            self.nodes += 1
            print('Level:', self.levels, '==> build left;', 'Value: ', node.left.value)
            self._build_tree(node.left, values, self.levels)
        if len(values) > 0:
            value = values.pop(0)
            node.right = Node(value)
            self.nodes += 1
            print('Level:', self.levels, '==> build right;', 'Value: ', node.right.value)
            self._build_tree(node.right, values, self.levels)
        return node

    def search_one_value(self, value):

        def _search_one_value(
            value, 
           _node, 
           _iteration=0, 
           _stop_search=False, 
           result=None, 
           on_verbose=False):
            """
              Output. Node and level location if exists,
            """
            if on_verbose:
                print(f'Node value {_node.value} in iteration {_iteration}')

            if result is not None:
                if result[2]:
                    print('stop')
                    return ('return stop')
                    return result
            if on_verbose:
                print(f'\n--Continue search--\n')
            # Main node
            if value == _node.value:
                _stop_search = True
                result = (_node, _iteration, _iteration, _stop_search)
                if on_verbose:
                    print('Value found')
                return result

            # Left node
            if _node.left is not None:
                result = _search_one_value(value, _node.left, _iteration + 1, _stop_search=_stop_search, result=result)
                if result is not None:
                    return result
            # Right node
            if _node.right is not None:
                result = _search_one_value(value, _node.right, _iteration + 1, _stop_search=_stop_search, result=result)
                if result is not None:
                    return result
                if on_verbose:
                    print('return last')
                return result

        result = _search_one_value(value=value, _node=self.tree)
        return result[:3] if result is not None else (None, -1, -1)

class Node():
    def __init__(self, value, left=None, right=None):
        """
        value [float]       :  amount or value applied to the node.
        left  [Node object] : left node
        right [Node object] : right node
        """
        self.value = value
        self.left = left
        self.right = right