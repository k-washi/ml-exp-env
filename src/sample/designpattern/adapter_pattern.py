from os.path import split, splitext

class DublinCoreAdapter:
    def __init__(self, filename) -> None:
        self._filename = filename
    
    @property
    def title(self):
        return splitext(split(self._filename)[-1])[0]
    
    @property
    def languages(self):
        return ("ja",)

    def __getitem__(self, item):
        return getattr(self, item, 'Unknown')
    

class DublinCoreInfo:
    def summary(self, dc_dict):
        print(f'タイトル: {dc_dict["title"]}')
        print(f'著者: {dc_dict["creator"]}')
        print(f'言語: {dc_dict["languages"]}')

if __name__ == "__main__":
    adapted = DublinCoreAdapter("work/example.txt")
    infos = DublinCoreInfo()
    infos.summary(adapted)
    """
    タイトル: example
    著者: Unknown
    言語: ('ja',)
    """