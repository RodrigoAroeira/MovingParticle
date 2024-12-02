import pygame

from particle import Particle

ROOT = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Moving")
WHITE = (255, 255, 255)
ROOT.fill(WHITE)


def loop():

    dS = 5
    running = True
    particle = Particle(40, (0, 0, 0), pygame.Vector2(400, 400))
    clock = pygame.time.Clock()

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False

                case pygame.MOUSEWHEEL:
                    dS += event.y
                    print(f"{dS=}")

        velocity = pygame.Vector2(0, 0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            velocity.x -= dS

        if keys[pygame.K_d]:
            velocity.x += dS

        if keys[pygame.K_w]:
            velocity.y -= dS

        if keys[pygame.K_s]:
            velocity.y += dS

        if keys[pygame.K_q]:
            particle.radius -= dS / 3
        if keys[pygame.K_e]:
            particle.radius += dS / 3
        particle.move(velocity)

        # Check if the mouse button is pressed
        if pygame.mouse.get_pressed()[0]:  # 0 means left button
            x, y = map(int, pygame.mouse.get_pos())
            particle.pos = pygame.Vector2(x, y)

        ROOT.fill(WHITE)
        particle.draw(ROOT)
        pygame.display.update()


if __name__ == "__main__":
    loop()
