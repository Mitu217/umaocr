from abc import ABCMeta, abstractmethod

from PIL import Image

from app.domain.skill import Skills, Skill


class SkillUsecase(metaclass=ABCMeta):
    @abstractmethod
    async def get_skills_from_character_modal_image(self, image: Image) -> Skills:
        raise NotImplementedError

    @abstractmethod
    async def get_skills_without_unique_from_image(self, image: Image) -> Skills:
        raise NotImplementedError

    @abstractmethod
    async def get_unique_skill_from_image(self, image: Image) -> Skill:
        raise NotImplementedError
