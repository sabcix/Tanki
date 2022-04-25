import random
import pygame
pygame.init()
#galvenais speles riks
def spele_aplis():
    izeja = False #jo ir divi tanki
    spele_pabeigta = False
    atrums = 15
    a_veseliba = 100 #1 tanka veseliba
    b_veseliba = 100 #2 tanka veseliba
    b_platums = 50
    pareja_tanks_a = ekrana_platums * 0.89 #kur parvietojas tanks nr1
    tanka_parvietojums = 0
    ctp = 0
    pareja_tanks_b = ekrana_augstums * 0.89 #kur parvietojas tanks nr2
    lenka_maina = 0
    tanka_a_a = ekrana_platums * 0.2 #kur parvietojas tanks nr1
    tanku_speks = 59
    tanka_b_b = ekrana_augstums * 0.9#kur parvietojas tanks nr2
    izm = 0
    a_tanka_atr_v = (ekrana_platums / 2) + random.randint(-1 * ekrana_platums, 1 * ekrana_platums)
    bara_augstums = random.randrange(ekrana_augstums * 1, ekrana_augstums * 6)
    global saujamais, y_saujamais  # divu veidu saujamie

    while not izeja:#neiezejam no speles ja
        if not spele_pabeigta:#spele nav pabeigta
            pass
        else:
            zinas_ekrans("Spēle beigusies", deep_pink, -50, izmers="beigas")#izvadam, ka speles beigas.
            zinas_ekrans("  žēl  ", rozigs, 50)
            pygame.display.update()#update
            while spele_pabeigta: #kamēr spēle iet uz apli
                for notik in pygame.event.get():
                    if notik.type != pygame.QUIT: #nav izeja
                        pass
                    else: #savadak ir izeja
                        izeja = True
                        spele_pabeigta = False
                    if notik.type != pygame.KEYDOWN:
                        continue #ja nav speles beigas
                    if notik.key == pygame.K_c:
                        spele_aplis() #spele uz apli iet
                    elif notik.key == pygame.K_q:
                        izeja = True
                        spele_pabeigta = False

        for notik in pygame.event.get():
            if notik.type != pygame.QUIT:
                pass
            else: izeja = True #atkal izeeja no speles

            if notik.type == pygame.KEYDOWN: #izveidojam tanka lokacijas
                if notik.key == pygame.K_LEFT: #pa kreisi kustiba
                    tanka_parvietojums = -10

                elif notik.key == pygame.K_RIGHT:#pa labi kustiba
                    tanka_parvietojums = 10

                elif notik.key == pygame.K_UP: #uz augsu kustiba
                    lenka_maina = 2

                elif notik.key == pygame.K_DOWN: #uz leju kustiba
                    lenka_maina = -2

                elif notik.key == pygame.K_SPACE: #space bars poga

                    apsaude = speletaja_apsaude(saujamais, ctp, tanku_speks, a_tanka_atr_v, b_platums,
                                               bara_augstums, tanka_a_a) #pogu nospiezot mes saujam
                    b_veseliba -= apsaude
                    tanku_kustibas_b = ['a', 'b'] #kustibu divas puses pa labi
                    parvietosanas_puses = random.randrange(0, 2)#un pa kreisi

                    for a in range(random.randrange(0, 10)):

                        if ekrana_platums * 0.3 > tanka_a_a > ekrana_platums * 0.03: #cik daudz pa labi no ekrana lieluma
                            if tanku_kustibas_b[parvietosanas_puses] == "a":#variants a puse a
                                tanka_a_a += 5
                            elif tanku_kustibas_b[parvietosanas_puses] == "b":#variants b puse b
                                tanka_a_a -= 5

                            speles_iedalijums.fill(rozigs) #nosakam speles motivu
                            veseliba(a_veseliba, b_veseliba) #uzliekam veselibas kvadratus
                            saujamais = musu_tanks(pareja_tanks_a, pareja_tanks_b, ctp) #uzliekam abu tanku savejus
                            y_saujamais = datora_tanks(tanka_a_a, tanka_b_b, 8)
                            tanku_speks += izm #tanku speki noorganizeti

                            speles_iedalijums.fill(maize, rect=[0, ekrana_augstums - lielais_augstums, ekrana_platums, lielais_augstums])
                            pygame.display.update()#uztaisam speles iedalijuma krasas, platumu u.c.
                            clock.tick(atrums)

                    apsaude = datora_apsaude(y_saujamais, 8, a_tanka_atr_v, b_platums,bara_augstums, pareja_tanks_a)# aprakstam apsaudi
                    a_veseliba -= apsaude # no veselibas nonemam nost apsaudi.
                elif notik.key == pygame.K_a:
                    izm = -1 #nosakam v
                elif notik.key == pygame.K_d:
                    izm = 1#nosakam v

            elif notik.type == pygame.KEYUP: #nakosas varutibas
                if notik.key != pygame.K_LEFT and notik.key != pygame.K_RIGHT: #ja nav nospiests pa kreisi un pa labi
                    pass# tad passojam
                else:
                    tanka_parvietojums = 0 #savadak tanks neparvietojas
                if notik.key != pygame.K_UP and notik.key != pygame.K_DOWN:  #ja nav nospiests uz augsu vai uz leju
                    pass #passojam
                else:
                    lenka_maina = 0 #savadak lenka maina nenotiek
                if notik.key != pygame.K_a and notik.key != pygame.K_d: #ja nemainam stiprumu
                    continue #turpinam
                izm = 0 #izmainu nav tad

        pareja_tanks_a += tanka_parvietojums
        ctp += lenka_maina
        if ctp > 8: #ja lielaks par 8 parv
            ctp = 8
        elif ctp < 0:#ja mazaks par 0 parv
            ctp = 0

        if pareja_tanks_a - (tanka_platums / 2) < a_tanka_atr_v + b_platums:
            pareja_tanks_a += 5
        speles_iedalijums.fill(rozigs)# nosakam speles kerana krasu
        veseliba(a_veseliba, b_veseliba) #uzliekam veselibas kstites
        saujamais = musu_tanks(pareja_tanks_a, pareja_tanks_b, ctp) #a saujamais
        y_saujamais = datora_tanks(tanka_a_a, tanka_b_b, 8)# b saujamais
#nosakam tanku spekus, cik tos var iznicinat
        tanku_speks += izm
        if tanku_speks > 100: #ja lielaks par 100
            tanku_speks = 100# tad tas nav iespejams jo lielaks par 100 nevar but
        elif tanku_speks < 1: #ja mazaks par 1
            tanku_speks = 1# tas nav iespejams
        speles_iedalijums.fill(maize, rect=[0, ekrana_augstums - lielais_augstums, ekrana_platums, lielais_augstums])
        pygame.display.update() #izveidojam speles iedalijumu

        if a_veseliba < 1: # ja veselibas kubins ir zem 1, tad mēs nomirtsma
            speles_3_att()# tiek izvadits 3 attels
        elif b_veseliba < 1: #ja speles kubins lielaks
            speletajs_uzvar()# par 1 tad mes vel spelejam
        clock.tick(atrums)
    pygame.quit()
    quit()
pedejais_dizains = pygame.font.SysFont("Arial", 70)
nv_dizains = pygame.font.SysFont("Arial", 20)
# izveidojam kopējos izskatus spēles sākumā, kā arī krāsas.
ekrana_augstums = 700
# krāsu nosaukumi un stili, bet dažas krāsas ir sajauktas.
rozigs = (196, 174, 173)
balts = (255, 255, 255)
ekrana_platums = 1000
coffee = (112, 66, 65)
deep_pink = (255, 20, 147)
pink = (255, 192, 203)
# viss saistits ar fontu utt
sakuma_dizains = pygame.font.SysFont("Arial", 20)
vidus_dizains = pygame.font.SysFont("Arial", 55)
yellow = (200, 200, 0)
speles_iedalijums = pygame.display.set_mode((ekrana_platums, ekrana_augstums))
#izvadam datus
pygame.display.set_caption('Tanku spēlīte')
silver_pink = (105, 105, 105)
light_yellow = (255, 255, 0)
maize = (251, 236, 93) # ta ir krasa
orchid = (218, 112, 214)
clock = pygame.time.Clock()

def speles_1_att():
    sakuma_iest = True
    while sakuma_iest:#parbaudam no sakuma
        for notikums in pygame.event.get():# sakuma iestatijumus
            if notikums.type == pygame.QUIT:
                pygame.quit()
                quit()
#ka ari parejos iestatijumus
            if notikums.type != pygame.KEYDOWN:#turpinam
                continue
            if notikums.key == pygame.K_c: # ja == tad izvadam nepareizs
                sakuma_iest = False #c ita gadijuma izejam
            elif notikums.key == pygame.K_q:
                pygame.quit()
                quit()
#pievienojam speles ieksejas krasas
        speles_iedalijums.fill(rozigs)
        zinas_ekrans("Tanku spēlīte", balts, -90, izmers="beigas") #proti beigu izmers, lai uzraditu datus
        zinas_ekrans("Tavs galvenais uzdevums ir pēc iespējas ātrāk sašaut datora tanku. ", silver_pink, 15)
        zinas_ekrans("Lai veicas!", silver_pink, 59)#redigejam izmerus visiem tekstiem
        poga("Spēlēt", 450, 490, 90, 40, silver_pink, orchid, notikums="play")#updeito attelus
        pygame.display.update()
        clock.tick(20)

def speles_3_att(): #pedeja attela izvade
    spele_beigusies_dators_uzvar = True #izvada ja dators uzvar
#ja jau dators uzvar tad
    while spele_beigusies_dators_uzvar:
        for event in pygame.event.get():#izejam no speles
            if event.type == pygame.QUIT:#piedavajam jaunu speli
                pygame.quit()
                quit()

        speles_iedalijums.fill(rozigs)#protams seit spele beidzas
        zinas_ekrans("Spēle beigusies!", balts, -109, izmers="beigas")#ja tanks uzvar
        zinas_ekrans("Tevi nošāva", silver_pink, -39)#ka ari izvada rezultatus
        poga("Spēlēt atkal", 440, 490, 140, 49, silver_pink, orchid, notikums="play")
        pygame.display.update()#iespejams ari spelet atkal
        clock.tick(15)

def teksta_izveidotais(txt, color, izmers="sakums"):
    global teksta_pamatne #ja izmers nav vienads ar sakuma
    if izmers != "sakums":
        pass
    else: teksta_pamatne = sakuma_dizains.render(txt, True, color)
    if izmers != "videjais":#ja izmers nav vienads ar videjais
        pass
    else: teksta_pamatne = vidus_dizains.render(txt, True, color)
    if izmers != "beigas":#ja izmers nav vienads ar beigas
        pass
    else: teksta_pamatne = pedejais_dizains.render(txt, True, color)
    if izmers != "v_sakums":#ja izmers nav vienads ar vsakuma
        pass
    else: teksta_pamatne = nv_dizains.render(txt, True, color)
    # ja izmers nav vienads ar tad atgriezam
    return teksta_pamatne, teksta_pamatne.get_rect()

def teksta_poga(zina, krasa, poga_a, poga_b, pogas_plat, pogas_augst, izmers="v_sakums"):#protams ka pogas koordinacija
    teksta_pamatne, teksta_repamat = teksta_izveidotais(zina, krasa, izmers)#pogai nepieciesamas krasas utt
    teksta_repamat.center = ((poga_a + (pogas_plat / 2)), poga_b + (pogas_augst / 2))#pogas izmers
    speles_iedalijums.blit(teksta_pamatne, teksta_repamat)

def datora_apsaude(ab, AtrasanasA, Aatrasanas, platums, augstums, tanksA):
    problemas = 0#no skauma visu aprakstam
    speks = 1
    spradziens_atr = False #ja nepatiess
#kamer vel nav atrasts spradziens tikmer
    while not spradziens_atr:
        speks += 1
        if speks > 100:#ja speks lielaks par 100
            spradziens_atr = True #tad spradziens atrasts
        uguni = True #saujam
        sakt_saut = list(ab) #sakt saut uz kuru pusi

        while uguni: #kamer saujam
            for notikums in pygame.event.get():#tikmer viss notiek
                if notikums.type == pygame.QUIT:
                    pygame.quit()#kad beidzam tad iziet ara
                    quit()

            sakt_saut[0] += (11 - AtrasanasA) * 2 #atrasanas lokaciju mainas
            sakt_saut[1] += int( # 0, 1 divas puses
                (((sakt_saut[0] - ab[0]) * 0.015 / (speks / 50)) ** 2) - (AtrasanasA + AtrasanasA / (11 - AtrasanasA)))

            if sakt_saut[1] > ekrana_augstums - lielais_augstums: #nodefinejam cik talu
                hit_x = int((sakt_saut[0] * ekrana_augstums - lielais_augstums) / sakt_saut[1]) #cik augstu var saut
                if tanksA + 15 > hit_x > tanksA - 15:
                    spradziens_atr = True #ja atrod spradzienu
                uguni = False #nofalso saujamo
#parbaudam saujamo adresi
            check_x_1 = sakt_saut[0] <= Aatrasanas + platums
            check_x_2 = sakt_saut[0] >= Aatrasanas #parbaudam saujamo adresi
            check_y_1 = sakt_saut[1] <= ekrana_augstums #parbaudam saujamo adresi
            check_y_2 = sakt_saut[1] >= ekrana_augstums - augstums#parbaudam saujamo adresi
            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                int((sakt_saut[0]))# parbaudam to visu caur arr
                int(sakt_saut[1])
                uguni = False #nofalso

    uguni = True
    sakt_saut = list(ab) #isti

    while uguni: #kamer saujam
        for notikums in pygame.event.get(): #tikmer process notiek
            if notikums.type == pygame.QUIT:
                pygame.quit()#kad beidzam izejam
                quit()
#pec formas izveidojam procesus
        pygame.draw.circle(speles_iedalijums, deep_pink, (sakt_saut[0], sakt_saut[1]), 15)#saujamie procesi, to parveide
        sakt_saut[0] += (11 - AtrasanasA) * 2#saujamie procesi, to parveide
        gun_power = random.randrange(int(speks * 0.91), int(speks * 1.11))#saujamie procesi, to parveide
        sakt_saut[1] += int( #saujamie procesi, to parveide
            (((sakt_saut[0] - ab[0]) * 0.014 / (gun_power / 50)) ** 2) - (AtrasanasA + AtrasanasA / (11 - AtrasanasA)))
        # saujamie procesi, to parveide
        if sakt_saut[1] > ekrana_augstums - lielais_augstums:#ekrana diferencesana
            hit_x = int((sakt_saut[0] * ekrana_augstums - lielais_augstums) / sakt_saut[1])#ekrana diferencesana
            hit_y = int(ekrana_augstums - lielais_augstums)
#parbaude uz to, cik liels sitiens
            if tanksA + 10 > hit_x > tanksA - 10:
                problemas = 25 #sitiens max
            elif tanksA + 35 > hit_x > tanksA - 35:
                problemas = 5 #sitiens min

            uguni = False
        check_x_1 = sakt_saut[0] <= Aatrasanas + platums #parbaude
        check_x_2 = sakt_saut[0] >= Aatrasanas #parbaude
        check_y_1 = sakt_saut[1] <= ekrana_augstums #parbaude
        check_y_2 = sakt_saut[1] >= ekrana_augstums - augstums #parbaude

        if check_x_1 and check_x_2 and check_y_1 and check_y_2: #parbaude
            hit_x = int((sakt_saut[0])) # ja viss ok sakam saut
            hit_y = int(sakt_saut[1])# ja viss ok sakam saut
            uguni = False
        pygame.display.update() #updeito ekranu
        clock.tick(80)#atrums
    return problemas

def speletajs_uzvar():# ja nu mes uzvaram
    spele_beigusies_tu_uzvari = True # ja ta ir patiesiba, ka uzvaram
    while spele_beigusies_tu_uzvari:
        for notikums in pygame.event.get():#so jau paskaidroju
            if notikums.type == pygame.QUIT:
                pygame.quit()#izejam
                quit()
#displeja nokrasas
        speles_iedalijums.fill(rozigs)
        zinas_ekrans("Tu esi uzvarējis!", balts, -90, izmers="beigas")#izvadam uzvaru
        zinas_ekrans("Apsveicam!", silver_pink, -29) #krasas, apsveicam
        poga("Spēlēt atkal", 449, 499, 149, 49, silver_pink, orchid, notikums="play")# spelet poga
        pygame.display.update()
        clock.tick(15) #atrums
def speletaja_apsaude(ab, AtrasanasA, ieroca_speks, Aatrasanas, platums, augstums, tanksA): #mes apsaudam datoru
    uzsakts_saut = list(ab)
    saut = True #uzsakts saut izvelamies true
    problemas = 0
    while saut: # kamer saujams
        for notikums in pygame.event.get():
            if notikums.type != pygame.QUIT:# ja notikums nav vienads
                continue #turpinam
            pygame.quit()# savadak izejam
            quit()

        pygame.draw.circle(speles_iedalijums, deep_pink, (uzsakts_saut[0], uzsakts_saut[1]), 15)#atkal zimejam apli prieks tanka
        uzsakts_saut[0] -= (11 - AtrasanasA) * 2#lokacija
        uzsakts_saut[1] += int((((uzsakts_saut[0] - ab[0]) * 0.015 / (ieroca_speks / 50)) ** 2) - (AtrasanasA + AtrasanasA / (11 - AtrasanasA)))
#lokacijas izveide, atrasanas
        if uzsakts_saut[1] > ekrana_augstums - lielais_augstums: #ekrana atrasanas vietas noteiksanas
            hit_x = int((uzsakts_saut[0] * ekrana_augstums - lielais_augstums) / uzsakts_saut[1])#ekrana atrasanas vietas noteiksanas
            hit_y = int(ekrana_augstums - lielais_augstums)#ekrana atrasanas vietas noteiksanas
            if tanksA + 10 > hit_x > tanksA - 10:
                problemas = 25 #probelmas max
            elif tanksA + 35 > hit_x > tanksA - 35:
                problemas = 5 #problemas min
            saut = False

        check_x_1 = uzsakts_saut[0] <= Aatrasanas + platums #atrasasnas v noteiksana
        check_x_2 = uzsakts_saut[0] >= Aatrasanas #atrasasnas v noteiksana
        check_y_1 = uzsakts_saut[1] <= ekrana_augstums #atrasasnas v noteiksana
        check_y_2 = uzsakts_saut[1] >= ekrana_augstums - augstums #atrasasnas v noteiksana

        if check_x_1 and check_x_2 and check_y_1 and check_y_2: #veicam parbaudes
            hit_x = int((uzsakts_saut[0]))#pirmais parbaude
            hit_y = int(uzsakts_saut[1])#otrais parbaude
            saut = False

        pygame.display.update()
        clock.tick(120) #ātrums kada sauj
    return problemas

def veseliba(a_tanks, b_tanks):# seit noteiksmi cik loti
    if a_tanks <= 50:#sabombardets ir tanks
        a_tanks_v = deep_pink
    else: a_tanks_v = maize # ir divas krasas:
    if b_tanks <= 50:# roza un dzeltena
        b_tanks_v = deep_pink# ja ir roza tad tansk ievainots smagi
    else: b_tanks_v = maize# ja dzeltena tad ne tik smagi

    pygame.draw.rect(speles_iedalijums, a_tanks_v, (880, 70, a_tanks, 45))# atrasanas vietas veselibas kastitem
    pygame.draw.rect(speles_iedalijums, b_tanks_v, (20, 70, b_tanks, 45))# atrasanas vietas veselibas kastitem

    #ekrans kurs izvada vairakas zinas
def zinas_ekrans(zina, krasa, b_atraanas_vieta=0, izmers="sakums"):
    teksta_pamatne, teksta_repamat = teksta_izveidotais(zina, krasa, izmers) #ja nebutu sis ekrans tad zinas nebutu
    teksta_repamat.center = (int(ekrana_platums / 2), int(ekrana_augstums / 2) + b_atraanas_vieta)#iespejams izvadit
    speles_iedalijums.blit(teksta_pamatne, teksta_repamat)

def poga(teksts, a, b, platums, augstums, krasa0, krasa1, notikums=None):
    bumbina = pygame.mouse.get_pos() #viss par un ap nospiesanas pogu
    spiedums = pygame.mouse.get_pressed() #par to, ka uztaisam nospiedumu
    if a + platums > bumbina[0] > a and b + augstums > bumbina[1] > b:
        pygame.draw.rect(speles_iedalijums, krasa1, (a, b, platums, augstums)) #pogas jutiguma location
        if spiedums[0] != 1:
            return #ja nav  spiedums
        if notikums is not None: #spiedums
            if notikums == "play":# play ka spelejam speli
                spele_aplis() #spele uz rinki kamer viss ok
    else:
        pygame.draw.rect(speles_iedalijums, krasa0, (a, b, platums, augstums))

    teksta_poga(teksts, rozigs, a, b, platums, augstums)
# tanka izmēri
t_platums = 10
t_augstums = 30
tanka_platums = 50
tanka_augstums = 30
lielais_augstums = 35
#noteicam izmerus tagad darbosimies ar tanku
def musu_tanks(a, b, atdalijuma_kalns):
    a = int(a)
    b = int(b)
    # pievienojam visus datus ar lokaciju, mainigajiem
    kalns_atdalijuma: list[tuple[int, int]] = [(a - 26, b - 1), (a - 25, b - 4), (a - 24, b - 7),#pievienojam visus datus
                                               (a - 22, b - 11), (a - 19, b - 13), (a - 17, b - 14), (a - 14, b - 16),#pievienojam visus datus
                                               (a - 12, b - 18), (a - 10, b - 20)]#pievienojam visus datus
    # pievienojam visus datus ar lokaciju, mainigajiem
    pygame.draw.circle(speles_iedalijums, coffee, (a, b), int(tanka_augstums / 2))#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a - 9, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a - 9, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a - 14, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a - 9, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a - 4, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a + 4, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a + 9, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a + 14, b + 19), t_augstums)#lokacijas
    pygame.draw.rect(speles_iedalijums, coffee, (a - tanka_augstums, b, tanka_platums, tanka_augstums))#lokacijas
    pygame.draw.line(speles_iedalijums, coffee, (a, b), kalns_atdalijuma[atdalijuma_kalns], t_platums)#lokacijas
    return kalns_atdalijuma[atdalijuma_kalns]#vieta, kur tanki vairs nevar saut

def datora_tanks(a, b, atdalijuma_kalns): #viss prieks datora tanka
    a = int(a)
    b = int(b)
    # pievienojam visus datus ar lokaciju, mainigajiem
    kalna_atdalijums: list[tuple[int, int]] = [(a - 26, b - 1), (a - 25, b - 4), (a - 24, b - 7),    # pievienojam visus datus ar lokaciju, mainigajiem
                                               (a - 22, b - 11), (a - 19, b - 13), (a - 17, b - 14), (a - 14, b - 16),# pievienojam visus datus
                                               (a - 12, b - 18), (a - 10, b - 20)]# pievienojam visus datus
    # pievienojam visus datus ar lokaciju, mainigajiem
    pygame.draw.circle(speles_iedalijums, coffee, (a, b), int(tanka_augstums / 2))#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a - 9, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a - 9, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a - 14, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a - 9, b + 19), t_augstums)#lokacijas#lokacijas#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a - 4, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a, b + 19), t_augstums)#lokacijas#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a + 4, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a + 9, b + 19), t_augstums)#lokacijas
    pygame.draw.circle(speles_iedalijums, coffee, (a + 14, b + 19), t_augstums)#lokacijas
    pygame.draw.rect(speles_iedalijums, coffee, (a - tanka_augstums, b, tanka_platums, tanka_augstums))#lokacijas
    pygame.draw.line(speles_iedalijums, coffee, (a, b), kalna_atdalijums[atdalijuma_kalns], t_platums)#lokacijas
    return kalna_atdalijums[atdalijuma_kalns]#vieta, kur tanki vairs nevar saut

speles_1_att()
spele_aplis()
