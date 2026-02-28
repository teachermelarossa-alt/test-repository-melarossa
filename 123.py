from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
import random
import math

app = Ursina(borderless=False, fullscreen=False)
window.title = 'Roblox на Python - с NPC'
window.color = color.light_gray
window.fps_counter.enabled = True
window.exit_button.visible = False

# --- Переменные игры ---
block_pick = 1
blocks = []
npcs = []  # Список всех NPC
game_paused = False
coins = 100  # Начинаем с 100 монет для покупок

# --- СОЗДАНИЕ ТЕКСТУР для блоков ---
grass_texture = ProceduralTexture(width=16, height=16, mode='rgb')
for y in range(16):
    for x in range(16):
        if (x // 4 + y // 4) % 2 == 0:
            grass_texture.set_pixel(x, y, (80, 160, 80, 255))
        else:
            grass_texture.set_pixel(x, y, (100, 200, 100, 255))
grass_texture.apply()

stone_texture = ProceduralTexture(width=16, height=16, mode='rgb')
for y in range(16):
    for x in range(16):
        if random.random() > 0.7:
            color_val = 180
        else:
            color_val = 120
        stone_texture.set_pixel(x, y, (color_val, color_val, color_val, 255))
stone_texture.apply()

brick_texture = ProceduralTexture(width=16, height=16, mode='rgb')
for y in range(16):
    for x in range(16):
        if (y // 4) % 2 == 0:
            if x // 4 == 0 or x // 4 == 3:
                brick_texture.set_pixel(x, y, (100, 60, 60, 255))
            else:
                brick_texture.set_pixel(x, y, (200, 80, 80, 255))
        else:
            brick_texture.set_pixel(x, y, (160, 60, 60, 255))
brick_texture.apply()

block_textures = {
    1: grass_texture,
    2: stone_texture,
    3: brick_texture
}

# --- КЛАСС NPC (неигровой персонаж) ---
class NPC(Entity):
    def __init__(self, position=(0,0,0), color=color.blue, name="Торговец"):
        super().__init__(
            model='cube',  # Временно используем куб (можно заменить на модель человечка)
            color=color,
            position=position,
            scale=(0.8, 1.8, 0.8),  # Пропорции человека
            collider='box'
        )
        
        # Голова (отдельный куб сверху)
        self.head = Entity(
            model='cube',
            color=color.light_gray,
            position=(0, 1.2, 0),
            scale=(0.7, 0.7, 0.7),
            parent=self
        )
        
        # Глаза
        self.eye_left = Entity(
            model='sphere',
            color=color.black,
            position=(-0.2, 1.3, 0.35),
            scale=0.15,
            parent=self
        )
        self.eye_right = Entity(
            model='sphere',
            color=color.black,
            position=(0.2, 1.3, 0.35),
            scale=0.15,
            parent=self
        )
        
        # Имя над головой
        self.name_tag = Text(
            name,
            position=(0, 2.2, 0),
            scale=10,
            color=color.white,
            parent=self,
            billboard=True  # Текст всегда повернут к игроку
        )
        
        # Свойства NPC
        self.name = name
        self.speed = 2
        self.wander_timer = 0
        self.wander_direction = Vec3(random.uniform(-1,1), 0, random.uniform(-1,1)).normalized()
        self.dialog = [
            "Привет, путник!",
            "Хочешь купить блоки?",
            "У меня есть редкие материалы!",
            "Строй что угодно!",
            "Жми E, чтобы поговорить"
        ]
        self.dialog_index = 0
        self.shop_items = {
            'Трава': {'type': 1, 'price': 10, 'texture': grass_texture},
            'Камень': {'type': 2, 'price': 20, 'texture': stone_texture},
            'Кирпич': {'type': 3, 'price': 30, 'texture': brick_texture}
        }
        
        # Индикатор над головой (для магазина)
        self.shop_sign = Entity(
            model='cube',
            color=color.gold,
            position=(0, 2.0, 0),
            scale=(0.5, 0.2, 0.1),
            parent=self
        )
        
    def update(self):
        # Простая анимация ходьбы (покачивание головы)
        self.head.y = 1.2 + math.sin(time.time() * 5) * 0.05
        
        # Случайное блуждание
        self.wander_timer += time.dt
        if self.wander_timer > 3:  # Меняем направление каждые 3 секунды
            self.wander_direction = Vec3(random.uniform(-1,1), 0, random.uniform(-1,1)).normalized()
            self.wander_timer = 0
        
        # Движение
        new_position = self.position + self.wander_direction * self.speed * time.dt
        
        # Проверка коллизий с блоками
        hit = raycast(self.position, self.wander_direction, distance=self.speed * time.dt + 0.5, ignore=[self])
        if not hit.hit:
            self.position = new_position
        
        # Поворот в направлении движения (плавно)
        if self.wander_direction.length() > 0:
            target_rotation = Vec3(0, -math.degrees(math.atan2(self.wander_direction.x, self.wander_direction.z)), 0)
            self.rotation = self.rotation.lerp(target_rotation, time.dt * 5)
    
    def talk(self):
        # Показываем диалог
        dialog_text = self.dialog[self.dialog_index]
        self.dialog_index = (self.dialog_index + 1) % len(self.dialog)
        
        # Создаем облачко с текстом
        bubble = Entity(
            model='quad',
            color=color.white,
            scale=(len(dialog_text) * 0.1, 0.3),
            position=self.position + Vec3(0, 2.5, 0),
            billboard=True
        )
        Text(
            dialog_text,
            parent=bubble,
            scale=10,
            color=color.black,
            origin=(0,0)
        )
        # Удаляем через 3 секунды
        destroy(bubble, delay=3)
        
        return dialog_text
    
    def open_shop(self):
        # Открываем магазин (будет вызвано из GUI)
        return self.shop_items

# --- Функция создания NPC в мире ---
def create_npc(position, color=color.blue, name="Торговец"):
    npc = NPC(position=position, color=color, name=name)
    npcs.append(npc)
    return npc

# --- Создание мира ---
ground = Entity(
    model='cube',
    color=color.green.tint(-0.4),
    position=(0, -0.5, 0),
    scale=(100, 1, 100),
    collider='box',
)

# Добавим немного декораций
for i in range(10):
    Entity(
        model='cube',
        color=color.green,
        position=(random.uniform(-20,20), 0, random.uniform(-20,20)),
        scale=(0.5, random.uniform(1,3), 0.5),
        collider='box'
    )

Sky(color=color.azure)

# --- Функции для блоков ---
def create_block(position=(0,0,0), type=1):
    block = Entity(
        model='cube',
        texture=block_textures[type],
        position=position,
        collider='box'
    )
    blocks.append(block)
    return block

# Создаем торговую площадку с NPC
# Создаем платформу для NPC
market_platform = Entity(
    model='cube',
    color=color.brown,
    scale=(10, 0.5, 10),
    position=(15, 0, 15),
    collider='box'
)

# Создаем NPC
npc1 = create_npc(position=(15, 1, 15), color=color.blue, name="Строитель Боб")
npc2 = create_npc(position=(10, 1, 10), color=color.orange, name="Торговец Джек")
npc3 = create_npc(position=(20, 1, 20), color=color.magenta, name="Маг Стив")

# Несколько блоков для начала
for x in range(-5, 6, 2):
    for z in range(-5, 6, 2):
        if random.random() > 0.7:
            create_block(position=(x, 0.5, z), type=random.randint(1,3))

# --- Игрок ---
player = FirstPersonController(
    speed=8,
    jump_height=2,
    jump_duration=0.3,
    position=(0, 1, 0),
    mouse_sensitivity=Vec2(40, 40)
)

# --- GUI (Интерфейс) ---

# Полоска здоровья
health_bar = HealthBar(
    bar_color=color.lime,
    roundness=0.5,
    scale=(0.3, 0.03),
    position=(-0.65, 0.45)
)
health_bar.value = 100

# Текст с монетами
coin_text = Text(
    f'Монеты: {coins}',
    position=(-0.85, 0.35),
    scale=2,
    color=color.yellow,
    background=True
)

# Панель инвентаря
inventory_frame = Entity(
    model='quad',
    color=color.rgba(50, 50, 50, 200),
    scale=(0.6, 0.1),
    position=(0, -0.45),
    parent=camera.ui
)

slot_positions = [-0.2, 0, 0.2]
slot_frames = []

for i, x_pos in enumerate(slot_positions):
    frame = Entity(
        model='quad',
        color=color.dark_gray,
        scale=(0.15, 0.8),
        position=(x_pos, 0),
        parent=inventory_frame
    )
    slot_frames.append(frame)
    
    icon = Entity(
        model='quad',
        texture=block_textures[i+1],
        color=color.white,
        scale=(0.12, 0.6),
        position=(x_pos, 0.05),
        parent=inventory_frame
    )
    
    number_text = Text(
        str(i+1),
        position=(x_pos - 0.05, -0.1),
        scale=1.5,
        color=color.white,
        parent=inventory_frame,
        origin=(0,0)
    )

selector = Entity(
    model='quad',
    color=color.rgba(255, 255, 0, 100),
    scale=(0.16, 0.9),
    position=(slot_positions[0], 0),
    parent=inventory_frame
)

# Крестик в центре
crosshair = Entity(
    model='quad',
    color=color.white,
    scale=(0.02, 0.1),
    position=(0, 0),
    parent=camera.ui
)
crosshair2 = Entity(
    model='quad',
    color=color.white,
    scale=(0.1, 0.02),
    position=(0, 0),
    parent=camera.ui
)

# Магазин (появляется при разговоре с NPC)
shop_menu = Entity(
    parent=camera.ui,
    enabled=False,
    scale=(0.5, 0.6)
)

shop_bg = Entity(
    model='quad',
    color=color.rgba(0, 0, 0, 200),
    scale=(2, 2),
    parent=shop_menu
)

shop_frame = Entity(
    model='quad',
    color=color.dark_gray,
    scale=(0.8, 0.9),
    position=(0, 0),
    parent=shop_menu
)

shop_title = Text(
    'МАГАЗИН',
    position=(0, 0.35),
    scale=3,
    color=color.gold,
    parent=shop_menu,
    origin=(0,0)
)

# Кнопки товаров
shop_buttons = []
current_npc = None  # Текущий NPC, с которым говорим

def close_shop():
    shop_menu.enabled = False
    player.enabled = True
    mouse.visible = False

close_button = Button(
    text='Закрыть',
    color=color.red,
    scale=(0.2, 0.1),
    position=(0, -0.4),
    parent=shop_menu,
    on_click=close_shop
)

# Меню паузы
pause_menu = Entity(
    parent=camera.ui,
    enabled=False
)

pause_bg = Entity(
    model='quad',
    color=color.rgba(0, 0, 0, 150),
    scale=(2, 2),
    parent=pause_menu
)

pause_title = Text(
    'ПАУЗА',
    position=(0, 0.2),
    scale=5,
    color=color.white,
    parent=pause_menu,
    origin=(0,0)
)

resume_button = Button(
    text='Продолжить',
    color=color.azure,
    scale=(0.2, 0.1),
    position=(0, 0),
    parent=pause_menu
)

quit_button = Button(
    text='Выйти',
    color=color.red,
    scale=(0.2, 0.1),
    position=(0, -0.15),
    parent=pause_menu
)

# --- Функции ---
def update_slot_selector():
    global block_pick
    selector.position = (slot_positions[block_pick-1], 0)
    
    for i, frame in enumerate(slot_frames):
        if i == block_pick-1:
            frame.color = color.rgba(100, 100, 100, 255)
        else:
            frame.color = color.dark_gray

def resume_game():
    global game_paused
    game_paused = False
    pause_menu.enabled = False
    mouse.visible = False
    player.enabled = True
    application.paused = False

def quit_game():
    application.quit()

resume_button.on_click = resume_game
quit_button.on_click = quit_game

def is_player_on_ground():
    hit = raycast(
        origin=player.position + Vec3(0, 0.1, 0),
        direction=(0, -1, 0), 
        distance=1.2,
        ignore=[player]
    )
    return hit.hit

def buy_item(item_name, item_data):
    global coins
    if coins >= item_data['price']:
        coins -= item_data['price']
        coin_text.text = f'Монеты: {coins}'
        # Добавляем блок в инвентарь (в данном случае просто создаем в руке)
        print_on_screen(f'Куплен {item_name}!', position=(0,0.2), scale=2, duration=1, color=color.green)
        # Можно добавить блок в инвентарь игрока
    else:
        print_on_screen('Недостаточно монет!', position=(0,0.2), scale=2, duration=1, color=color.red)

# --- Обработка ввода ---
def input(key):
    global block_pick, game_paused, coins, current_npc, shop_menu
    
    if key == 'escape':
        if shop_menu.enabled:
            close_shop()
        else:
            game_paused = not game_paused
            pause_menu.enabled = game_paused
            mouse.visible = game_paused
            player.enabled = not game_paused
            application.paused = game_paused
        return
    
    if game_paused or shop_menu.enabled:
        return
    
    # Взаимодействие с NPC (кнопка E)
    if key == 'e':
        # Проверяем, есть ли NPC рядом
        for npc in npcs:
            distance = distance_xz(player.position, npc.position)
            if distance < 3:  # Если NPC в радиусе 3 блоков
                npc.talk()
                # Открываем магазин
                current_npc = npc
                open_shop_for_npc(npc)
                break
    
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=10, ignore=[player, ground] + npcs)
        if hit_info.hit and hit_info.entity in blocks:
            blocks.remove(hit_info.entity)
            destroy(hit_info.entity)
            coins += 10
            coin_text.text = f'Монеты: {coins}'
    
    if key == 'right mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=10, ignore=[player] + npcs)
        if hit_info.hit:
            position = hit_info.entity.position + hit_info.normal
            if not any(block.position == position for block in blocks) and position != ground.position:
                create_block(position=position, type=block_pick)
    
    if key == '1':
        block_pick = 1
        update_slot_selector()
        print_on_screen('Выбран блок: Трава', position=(0,0.1), scale=2, duration=1)
    if key == '2':
        block_pick = 2
        update_slot_selector()
        print_on_screen('Выбран блок: Камень', position=(0,0.1), scale=2, duration=1)
    if key == '3':
        block_pick = 3
        update_slot_selector()
        print_on_screen('Выбран блок: Кирпич', position=(0,0.1), scale=2, duration=1)

def open_shop_for_npc(npc):
    global shop_menu
    # Очищаем старые кнопки
    for btn in shop_buttons:
        destroy(btn)
    shop_buttons.clear()
    
    # Создаем кнопки для каждого товара
    items = npc.shop_items
    y_pos = 0.2
    for i, (item_name, item_data) in enumerate(items.items()):
        btn = Button(
            text=f'{item_name} - {item_data["price"]} монет',
            color=color.azure,
            scale=(0.6, 0.08),
            position=(0, y_pos - i * 0.1),
            parent=shop_menu
        )
        # Используем lambda с захватом значения
        btn.on_click = Func(buy_item, item_name, item_data)
        shop_buttons.append(btn)
    
    shop_menu.enabled = True
    player.enabled = False
    mouse.visible = True

# --- Обновление ---
def update():
    global coins, player_was_falling, fall_start_height
    
    if game_paused or shop_menu.enabled:
        return
    
    # Обновляем всех NPC
    for npc in npcs:
        npc.update()
    
    on_ground = is_player_on_ground()
    
    # Остальная логика (падение, здоровье и т.д.)
    # ... (оставляем как в предыдущих версиях)

# --- Инициализация ---
mouse.visible = False
update_slot_selector()

app.run()