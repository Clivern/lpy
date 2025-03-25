# 315. ABC register
#
# ABCMeta.register says an existing class implements the ABC without inheriting.
# isinstance then returns True. Useful for third-party types.
#
# Run: python 315_abc_abstract/main.py

from abc import ABC, abstractmethod
class Drawable(ABC):
    @abstractmethod
    def draw(self): ...
class ThirdParty:
    def draw(self):
        return "ok"
Drawable.register(ThirdParty)
print(isinstance(ThirdParty(), Drawable))
