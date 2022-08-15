from abc import ABC, abstractmethod
class persona_info (ABC):
  @abstractmethod
  def persona_info_name(self):
    pass
  
class persona_name (persona_info):
  def persona_data(self, name):
     self.name = name
     print("", self.name)
    
akira = persona_name
akira.persona_data(akira, "Akira kurusu")
