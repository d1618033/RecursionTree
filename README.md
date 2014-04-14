Recursion Tree Decorators
========================

Usage
-----

      @recursion_tree(save_to_file=True)

saves the recursion tree to a file

      @recursion_tree

displays the recursion tree using xdot

Requirements
------------

Xdot, dot, graphviz

Example
-------


      @recursion_tree(save_to_file=True)
      def ackermann(m, n):
          if m == 0:
              return n + 1
          elif m > 0:
              if n == 0:
                  return ackermann(m - 1, 1)
              else:
                  return ackermann(m - 1, ackermann(m, n - 1))
