class Node:
    def __init__(self,key,definition):
        self.key=key
        self.definition=definition
        self.right=None
        self.left=None
        self.height=1

class AVLTree:
    def __init__(self):
        self.root=None

    def height(self,node):
        if node is None:
            return 0
        return node.height
    
    def balanced(self,node):
        if node is None:
            return 0
        return self.height(node.left)-self.height(node.right)
        
    def right_rotation(self,root):
        new_root=root.left
        root.left=root.left.right
        new_root.right=root

        root.height=1+max(self.height(root.left),self.height(root.right))
        new_root.height=1+max(self.height(new_root.left),self.height(new_root.right))
        
        return new_root
    
    def left_rotation(self,root):
        new_root=root.right
        root.right=root.right.left
        root.left=root

        root.height=1+max(self.height(root.left),self.height(root.right))
        new_root.height=1+max(self.height(new_root.left),self.height(new_root.right))
        
        return new_root
        

    def insert(self,root,key,definition):
        if root is None:
            return Node(key,definition)
        
        if key<root.key:
            root.left=self.insert(root.left,key,definition)
        elif key>root.key:
            root.right=self.insert(root.right,key,definition)
        else:

            root.definition=definition
            return root
        
        root.height=1+max(self.height(root.left),self.height(root.right))
        

        balance=self.balanced(root)

        if balance>1 and key<root.key:
            return self.right_rotation(root)
        
        if balance>1 and key>root.key:
            root.left=self.left_rotation(root.left)
            return self.right_rotation(root)
        
        if balance<-1 and key<root.key:
            root.right=self.right_rotation(root.right)
            return self.left_rotation(root)
        
        if balance<-1 and key>root.key:
            return self.left_rotation(root)
        
        return root
    
    def search(self,root,key):
        if root is None:
            return None
        if key==root.key:
            return root.definition
        elif key<root.key:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)

def main():
    tree=AVLTree()
    while True:
        print("\n ---Dictionary---")
        print("1.Add word")
        print("2.Search word")
        print("3.Exit")

        choice=input("\nChoice.")
        if choice == '1':
            word=input("Enter the word.")
            meaning=input("Enter the meaning.")
            tree.root=tree.insert(tree.root,word,meaning)
            print(f"{word} has been added.")
        elif choice=='2':
            word=input("Search the word.")
            result=tree.search(tree.root,word)
            if result:
                print(f"{word}-{result}")
            else:
                print("The word was not found.")
        elif choice=='3':
            print("It came out...")
            break
        else:
            print("Please try again.")


if __name__=="__main__":
    main()