from abc import abstractmethod

class Band:
    ''' class which creates band instances'''
    instances = []
    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

    def play_solos(cls):
        return [member.play_solo() for member in cls.members]

    @classmethod
    def to_list(cls):
        return cls.instances

class Musician:
    ''' class which inherited to any kind of musician'''
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

class Guitarist(Musician):
    ''' It is a sub class that creates a musician that can play guitar '''
    def __init__(self, name):
        self.name = name
        self.instrument = "guitar"

    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Drummer(Musician):
    ''' It is a sub class that creates a musician that can play drum '''
    def __init__(self, name):
        self.name = name
        self.instrument = "drums"

    def __str__(self):
        return f"My name is {self.name} and I play drums"
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    
    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


class Bassist(Musician):
    ''' It is a sub class that creates a musician that can play bass '''
    def __init__(self, name):
        self.name = name
        self.instrument = "bass"

    def __str__(self):
        return f"My name is {self.name} and I play bass"
    
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    
    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"