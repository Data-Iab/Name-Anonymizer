class Entity:
    def __init__(self, entity, start, length):
        """Stored entity, its starting index and length"""
        self.start = start
        self.length = length
        self.entity = entity

    def to_dict(self):
        """Returns entity as a dictionary -> dict"""
        end = self.start + self.length
        return {'entity': self.entity, 'start': self.start, 'end': end}
