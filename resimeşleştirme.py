import pygame
import random
import sys
import time


pygame.init() # Pygame başlatma
pygame.mixer.init()  # Ses modülünü başlat

# Oyun Ayarları
GRID_ROWS = 6
GRID_COLS = 4
CARD_SIZE = 110
GAP = 15

# Ekran boyutunun kartlara göre ayarlarlanması
info = pygame.display.Info()
SCREEN_WIDTH = min(info.current_w, (CARD_SIZE + GAP) * GRID_COLS + GAP)
SCREEN_HEIGHT = min(info.current_h, (CARD_SIZE + GAP) * GRID_ROWS + GAP)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Ekran oluşturma
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Captain's Deck")

# Müzik yükleme ve rastgele oynatma
def play_random_music():
    try:
        music_files = [
            'sounds/Drunken_Sailor.mp3',
            'sounds/BosunBill.mp3',
            'sounds/JollyRogers.mp3',
            'sounds/PiratesCarabian.mp3'
        ]
        selected_music = random.choice(music_files) # Rastgele bir şarkı seçer
        pygame.mixer.music.load(selected_music)
        pygame.mixer.music.play(-1)  # Seçilen şarkıyı sonsuz döngüde çalar
        pygame.mixer.music.set_volume(0.2)  # Ses seviyesi (0.0 - 1.0 arası)
        print(f"Çalan şarkı: {selected_music}")
    except pygame.error as e:
        print(f"Müzik yüklenemedi: {e}")

play_random_music()

# Resimleri yükleme
rum_img = pygame.image.load('images/rum.png')
map_img = pygame.image.load('images/map.png')
compass_img = pygame.image.load('images/compass.png')
coin_img = pygame.image.load('images/coin.png')
hook_img = pygame.image.load('images/hook.png')
sword_img = pygame.image.load('images/sword.png')
ring_img = pygame.image.load('images/ring.png')
parrot_img = pygame.image.load('images/parrot.png')
octopus_img = pygame.image.load('images/octopus.png')
spyglass_img = pygame.image.load('images/spyglass.png')
mermaid_img = pygame.image.load('images/mermaid.png')
wheel_img = pygame.image.load('images/wheel.png')

# Kart arka yüz deseni yükleme
desen_img = pygame.image.load('images/desen.png')
desen_img = pygame.transform.scale(desen_img, (CARD_SIZE, CARD_SIZE))

# Oyuncu adı alma
player_name = input("Oyuncu adınızı girin: ")

# Kart sınıfı
class Card:
    def __init__(self, x, y, image, identifier):
        self.rect = pygame.Rect(x, y, CARD_SIZE, CARD_SIZE) # Kartın pozisyon ve boyut bilgileri)
        self.image = pygame.transform.scale(image, (CARD_SIZE, CARD_SIZE)) # Kartın resmini, tanımlı boyutlara ölçekler
        self.revealed = False #Kartın açık olup olmadığını kontrol eder
        self.id = identifier

    def draw(self, surface):
        if self.revealed:
            surface.blit(self.image, self.rect.topleft)
        else:
            surface.blit(desen_img, self.rect.topleft)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)

    def reveal(self):
        self.revealed = True

    def hide(self):
        self.revealed = False

    def __eq__(self, other): 
        return self.id == other.id

# Kartları oluşturma
def create_cards():
    images = [rum_img, map_img, compass_img, coin_img, hook_img, sword_img, ring_img, parrot_img, octopus_img, spyglass_img, mermaid_img, wheel_img] #kart resimleri
    cards = [] #kartlar listesi
    
    # Her resimden 2 tane oluştur
    for i, img in enumerate(images):    
        for _ in range(2): #her görselden 2 tane oluşturur
            x = 0
            y = 0
            cards.append(Card(x, y, img, i))

    random.shuffle(cards)

    # Kartları ekrana yerleştir
    for idx, card in enumerate(cards):
        row = idx // GRID_COLS #kartların sıralanacağı satır ve sütun
        col = idx % GRID_COLS
        card.rect.topleft = (col * (CARD_SIZE + GAP) + GAP, row * (CARD_SIZE + GAP) + GAP) #kartların konumları

    print(f"{len(cards)} kart oluşturuldu.")
    return cards

# Oyun döngüsü
def game_loop():
    clock = pygame.time.Clock() # Oyun saatini başlat
    cards = create_cards()  # Kartları oluştur
    selected_cards = [] # Seçilen kartlar

    start_time = time.time() # Oyun başlangıç zamanı

    running = True  
    while running: 
        screen.fill((45, 45, 80))  #(oyun alanı arkaplanı)
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # Çıkış yapılırsa oyunu kapat
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN: # Fare tıklaması algıla
                for card in cards:
                    if card.rect.collidepoint(event.pos) and not card.revealed: # Kartın üzerine tıklanırsa, kartı aç ,seçilen kartları listeye ekle
                        card.reveal() 
                        selected_cards.append(card)    
                        
                        if len(selected_cards) == 2: # Seçilen 2 kartı kontrol et,Kartları çiz,Ekranı güncelle
                            for card in cards:
                                card.draw(screen) 
                            pygame.display.flip() 
                            pygame.time.wait(500) # 0.5 saniye bekle
                            if selected_cards[0] == selected_cards[1]: 
                                print("Eşleşme bulundu!")
                            else:
                                selected_cards[0].hide() # Eşleşme yoksa kartları kapatır
                                selected_cards[1].hide()
                            selected_cards.clear()
        
        if all(card.revealed for card in cards): # Tüm kartlar açıldıysa oyunu bitirir
            end_time = time.time() # Oyun bitiş zamanı
            total_time = round(end_time - start_time, 2) # Oyun süresi
            pygame.mixer.music.stop()  # Oyun bitince müziği durdurur
            screen.fill((210, 180, 140))  # Oyun bitince arkaplan kum rengi yapar
            print(f"Tebrikler {player_name}! Tüm kartları {total_time} saniyede eşleştirdiniz.") 
            with open("scores.txt", "a") as file: # Skorları dosyaya yazar
                file.write(f"{player_name}: {total_time} saniye\n")     
            pygame.display.flip() # Ekranı günceller
            pygame.time.wait(3000) # 3 saniye bekler
            running = False # Oyunu bitirir

        for card in cards:
            card.draw(screen) # Kartları çizer

        pygame.display.flip()
        clock.tick(30) # FPS (30 kare/saniye) ayarlar

if __name__ == "__main__": # Programın başlangıç noktası
    game_loop() # Oyun döngüsünü başlatır