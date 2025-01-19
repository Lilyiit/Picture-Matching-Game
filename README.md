# ResimEslestirme
 Bu proje, Captain's Deck adlı bir hafıza oyunu olup, kart eşleştirme mekaniği üzerine kuruludur. 
Aşağıda, kodun temel işleyişi adım adım açıklanmıştır:

1. Kütüphanelerin ve Ayarların Yüklenmesi:
pygame kütüphanesi oyun arayüzü ve sesler için kullanılır.
random kütüphanesi kartların karıştırılması ve rastgele müzik seçimi için kullanılır.
Ekran boyutu, cihazın çözünürlüğüne uygun şekilde otomatik olarak ayarlanır.
Bu sayede oyun farklı cihazlarda doğru şekilde görüntülenir.

2. Müziklerin Yüklenmesi:
Oyunun başlangıcında rastgele bir müzik seçilir ve sürekli döngüde çalınır.
play_random_music fonksiyonu, sounds/ klasöründen müzik dosyalarını yükler ve ses seviyesini ayarlar.
Eğer bir müzik dosyası eksikse hata mesajı görüntülenir.
3. Kart Görsellerinin ve Arka Yüz Tasarımının Yüklenmesi
Tüm kart görselleri ve arka yüz tasarımı, images/ klasöründen yüklenir.
Kart görselleri, tanımlı boyutlara ölçeklenir (CARD_SIZE)

4. Oyuncu Adı Alma:
Oyuncunun adı konsoldan alınır. Bu ad, skor dosyasına kaydedilecek oyuncu bilgisi için gereklidir.

5. Kartların Tanımlanması ve Oluşturulması
Card sınıfı, her bir kartın özelliklerini ve davranışlarını tanımlar:

Rect: Kartın ekrandaki yeri (x, y koordinatları).
İmage: Kartın ön yüzündeki görsel.
Revealed: Kartın açık mı yoksa kapalı mı olduğunu takip eder.
ID: Kartların eşleştirilmesini sağlamak için kullanılan benzersiz bir değer.
create_cards fonksiyonu, 12 farklı görselden iki adet kart oluşturur (toplam 24 kart)
ve bu kartları rastgele karıştırır. Daha sonra kartları ekrandaki sıralı bir ızgaraya yerleştirir.

6. Oyun Döngüsü:
game_loop fonksiyonu, oyunun ana döngüsüdür ve şu işlevleri içerir:
Oyun başlangıcı: Saat başlatılır ve kartlar ekrana yerleştirilir.
Fare etkileşimleri: Oyuncunun fare tıklamalarını algılar. 
Eğer tıklanan kart kapalıysa, kart açılır ve seçilen kartlar listesine eklenir.
Kart eşleştirme kontrolü:
İki kart seçildiğinde, bu kartların kimlikleri karşılaştırılır.
Eşleşme varsa, kartlar açık kalır. Eşleşme yoksa, kartlar tekrar kapatılır.
Oyun bitişi: Tüm kartlar açıldığında oyun sona erer. Geçen süre hesaplanır ve ekrana yazdırılır.
Ayrıca bu süre oyuncunun adıyla birlikte scores.txt dosyasına kaydedilir.


7. Grafikler ve Çizim:
Kartlar ve arka plan, her döngüde yeniden çizilir.
Arka plan rengi korsan temalı bir atmosfer oluşturacak şekilde koyu mavi olarak ayarlanmıştır.
Kartlar açıkken ilgili görseli, kapalıyken arka yüz desenini gösterir.


8. Skor Kaydı:
Oyunun sonunda, oyuncunun adı ve oyunu tamamlama süresi scores.txt dosyasına şu formatta kaydedilir:
OyuncuAdı: XX saniye

9. Oyun Akışı:
Program başlatıldığında ekran oluşturulur ve müzik çalınır.
Kartlar rastgele karıştırılır ve ekrana yerleştirilir.
Oyuncu kartları açarak çiftleri eşleştirmeye çalışır.
Tüm kartlar eşleştiğinde oyun sona erer ve oyuncunun skor bilgisi kaydedilir.

10. Kapatma ve FPS Ayarı:
pygame.QUIT olayı algılandığında oyun güvenli bir şekilde kapanır.
Oyun, clock.tick(30) ile saniyede 30 karelik bir hızda çalışır. Bu, oyunun akıcı bir şekilde çalışmasını sağlar.
Bu yapı sayesinde oyun hem kullanıcı dostu hem de geliştirilebilir bir yapıya sahiptir.
