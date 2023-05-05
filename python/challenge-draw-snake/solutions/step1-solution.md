# Solution

```python
def __init__(self):
    self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
    self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
    self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
    self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
    
    self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
    self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
    self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
    self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

    self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
    self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

    self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
    self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
    self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
    self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

    self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]

```