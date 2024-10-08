# GAME ROBOT PYTHON
Executed and created in Python 3.9

Natanael I Manurung 19624283

1. Eksekusi kode di Python versi 3 keatas
Pastikan bahwa environment python yang dijalankan memiliki modul math dan random

2. Pilih robot yang ingin digunakan dan dilawan
Masukkan angka 1 sampai 3 untuk memilih robot yang ingin digunakan. Masukkan 4 untuk
melihat deskripsi dasar setiap robot dan pertolongan ketika bingung menjalankan gamenya

3. Pilih gerakan yang ingin dilakukan
Masukkan angka 1-4 untuk memilih aksi yang ingin dilakukan, setiap robot memiliki 4 aksi:
- Healing (Penambahan darah)
- Normal attack (Serangan biasa)
- Heavy attack (Serangan keras dengan akurasi yang rendah)
- +Attribute (Penambahan atribut khas setiap robot)

NOTE: Tekan enter setelah prompt untuk melanjutkan game

***
Penjelasan UI:

Tiger-Bot																	<- Status Player

||||||----------------------------------    16/100	

Elephant-Bot																<- Status lawan

|||||||||||||||||||||||||||||||||||||---    186/200

Elephant-Bot used SEISMIC BLAST towards Tiger-Bot and it dealt 18 HP!		<- Prompt selanjutnya

***
Penjelasan code:
1. Class robot
   
 	a. Memiliki atribut name, hp, attack, defense, evasion, moves, maxhp

	b. Metode move(opponent, index) menerima lawan dan input pilihan gerakan. Metode ini akan melakukan gerakan tersebut dengan merubah baik nilai lawan atau nilai user sesuai dengan move yang dilakukan.

3. Class battle
   
	a. Berfungsi untuk menginisiasi pertarungan antara 2 robot yang dimasukkan.

	b. Metode start_fight(player, opponent) menerima dua robot yang akan bertarung, satu robot yang dikontrol user dan satu lagi lawannya yang akan dikontrol kode. Memulai loop pertarungan, berhenti ketika HP salah satu robot mencapai 0. 
	
5. Class game
   
	a. Memiliki atribut is_ongoing, player, dan opponent.

	b. Metode add_robot(player, opponent) menerima robot yang dipertarungkan, yang nantinya akan diassign pada atribut game player dan opponent

	c. Metode start_game() menginiasi game dari awal, meminta robot yang ingin dipertarungkan, dan menjalankan start_fight(game.player, game.opponent). Menghentikan keseluruhan kode ketika user menolak untuk bermain lagi.
