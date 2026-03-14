from collections import defaultdict
class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content
    def append(self, new_content):
        self.content += new_content

class DirNode:
    def __init__(self, name):
        self.name = name
        self.sub_dirs = {}
        self.files = {}

    def has_dir(self, name):
        return name in self.sub_dirs

    def has_file(self, name):
        return name in self.files


class FileSystem:

    def __init__(self):
        self.root_node = DirNode("")

    def ls(self, path: str) -> List[str]:
        paths = path.split("/")[1:]
        node = self.root_node
        for p in paths:
            if p in node.files:
                return [p]
            if p in node.sub_dirs:
                node = node.sub_dirs[p]
        res = []
        for file in node.files.values():
            res.append(file.name)
        for sub_dir in node.sub_dirs.values():
            res.append(sub_dir.name)
        return sorted(res)

    def mkdir(self, path: str) -> None:
        paths = path.split("/")[1:]
        node = self.root_node
        for p in paths:
            if p not in node.sub_dirs:
                node.sub_dirs[p] = DirNode(p)
            node = node.sub_dirs[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        paths = filePath.split("/")[1:]
        node = self.root_node
        for i in range(len(paths)-1):
            p = paths[i]
            if p not in node.sub_dirs:
                node.sub_dirs[p] = DirNode(p)
            node = node.sub_dirs[p]
        file_name = paths[-1]
        if file_name not in node.files:
            node.files[file_name] = File(file_name, "")
        node.files[file_name].append(content)

    def readContentFromFile(self, filePath: str) -> str:
        paths = filePath.split("/")[1:]
        node = self.root_node
        for i in range(len(paths) - 1):
            p = paths[i]
            if p not in node.sub_dirs:
                node.sub_dirs[p] = DirNode(p)
            node = node.sub_dirs[p]
        file_name = paths[-1]
        return node.files[file_name].content