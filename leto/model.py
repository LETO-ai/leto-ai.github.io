from dataclasses import dataclass


class Entity:
    name: str
    type: str

    def __init__(self, name:str, type:str, **kwargs) -> None:
        self.name = name
        self.type = type
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self) -> str:
        return f"{self.name}:{self.type}"

    def __repr__(self):
        return str(self)

    def __eq__(self, o: object) -> bool:
        return str(self) == str(o)


class Relation:
    label: str
    entity_from: Entity
    entity_to: Entity

    def __init__(self, label:str, entity_from:Entity, entity_to:Entity, **kwargs) -> None:
        self.label = label
        self.entity_from = entity_from
        self.entity_to = entity_to
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self) -> str:
        return f"({self.entity_from}) -[{self.label}]-> ({self.entity_to})"

    def __repr__(self):
        return str(self)

    def __eq__(self, o: object) -> bool:
        return str(self) == str(o)
