from dataclasses import dataclass
import pygame


@dataclass
class Particle:
    """"""

    radius: int
    color: tuple[int, int, int]
    pos: pygame.Vector2

    def draw(self, win: pygame.Surface) -> None:
        pygame.draw.circle(
            surface=win, color=self.color, center=self.pos, radius=self.radius
        )

    def move(self, velocity: pygame.Vector2) -> None:
        self.pos += velocity
