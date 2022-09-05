'''
Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization 
algorithm should work. You just need to ensure that a binary tree 
can be serialized to a string and this string can be deserialized 
to the original tree structure.
'''
class Codec:

    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        self.i = 0
        node_strs = data.split(",")

        def dfs():
            if node_strs[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(node_strs[i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


        