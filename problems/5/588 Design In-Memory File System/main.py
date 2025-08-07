class Node:

    def __init__(self, name: str, isFile: bool = False):
        self.name = name
        self.isFile = isFile
        self.children = {}
        self.content = ''

class FileSystem:

    def __init__(self):
        self.root = Node('/')
    
    def ls(self, path: str) -> list[str]:
        if path == '/':
            return ['/' + item for item in self.root.children.keys()]
        node = self.root
        for name in path.split('/'):
            if not name:
                continue
            node = node.children[name]
        return [path + '/' + item for item in node.children.keys()] 
        
    def mkdir(self, path: str) -> None:
        node = self.root
        for name in path.split('/'):
            if not name:
                continue
            if name not in node.children:
                node.children[name] = Node(name)
            node = node.children[name]
    
    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        for name in filePath.split('/')[1:]:
            if name not in node.children:
                node.children[name] = Node(name)
            node = node.children[name]
        node.isFile = True
        node.content += content
    
    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        for name in filePath.split('/')[1:]:
            if name not in node.children:
                node.children[name] = Node(name)
            node = node.children[name]
        return node.content
    
fs = FileSystem()
print(fs.ls('/'))
print(fs.mkdir("/a/b/c"))
print(fs.addContentToFile('/a/b/c/d', 'hello'))
print(fs.ls('/'))
print(fs.readContentFromFile('/a/b/c/d'))
    