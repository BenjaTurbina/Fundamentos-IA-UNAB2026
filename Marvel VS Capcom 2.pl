% ==============================================================================
% 							LISTA DE HECHOS DE PRIMER ORDEN
% ==============================================================================

% Identificador del título y nombre oficial
juego(mvc2, 'Marvel vs. Capcom 2: New Age of Heroes').

% Desarrollador y Editor
desarrollador(mvc2, capcom).
editor(mvc2, capcom).

% ---------------------------------------------------------
% LANZAMIENTOS Y PLATAFORMAS
% Estructura: lanzamiento(Juego, Plataforma, Año).
% ---------------------------------------------------------

% Lanzamiento original (Arcade y consolas de sexta generación)
lanzamiento(mvc2, arcade_naomi, 2000).
lanzamiento(mvc2, dreamcast, 2000).
lanzamiento(mvc2, playstation_2, 2002).
lanzamiento(mvc2, xbox, 2002).

% Relanzamientos en alta definición (Digitales)
lanzamiento(mvc2, playstation_3, 2009).
lanzamiento(mvc2, xbox_360, 2009).
lanzamiento(mvc2, ios, 2012).

% Relanzamiento moderno (Marvel vs. Capcom Fighting Collection)
lanzamiento(mvc2, nintendo_switch, 2024).
lanzamiento(mvc2, playstation_4, 2024).
lanzamiento(mvc2, pc_steam, 2024).


% ==============================================================================
% FRANQUICIA: MARVEL (28 personajes)
% ==============================================================================
% Declaración del personaje
personaje(blackheart).
personaje(cable).
personaje(captain_america).
personaje(colossus).
personaje(cyclops).
personaje(doctor_doom).
personaje(gambit).
personaje(hulk).
personaje(iceman).
personaje(iron_man).
personaje(juggernaut).
personaje(magneto).
personaje(marrow).
personaje(omega_red).
personaje(psylocke).
personaje(rogue).
personaje(sabretooth).
personaje(sentinel).
personaje(shuma_gorath).
personaje(silver_samurai).
personaje(spider_man).
personaje(spiral).
personaje(storm).
personaje(thanos).
personaje(venom).
personaje(war_machine).
personaje(wolverine).
personaje(bone_wolverine). % Wolverine con garras de hueso es un slot distinto en MvC2

% ==============================================================================
% FRANQUICIA: CAPCOM (28 personajes)
% ==============================================================================
% Declaración del personaje
personaje(akuma).
personaje(amingo).
personaje(anakaris).
personaje(bb_hood).
personaje(cammy).
personaje(captain_commando).
personaje(charlie).
personaje(chun_li).
personaje(dan).
personaje(dhalsim).
personaje(felicia).
personaje(guile).
personaje(hayato).
personaje(jill).
personaje(jin).
personaje(ken).
personaje(m_bison).
personaje(mega_man).
personaje(morrigan).
personaje(roll).
personaje(ruby_heart).
personaje(ryu).
personaje(sakura).
personaje(servbot).
personaje(sonson).
personaje(strider_hiryu).
personaje(tron_bonne).
personaje(zangief).

% Asignación a la franquicia marvel
franquicia(blackheart, marvel).
franquicia(cable, marvel).
franquicia(captain_america, marvel).
franquicia(colossus, marvel).
franquicia(cyclops, marvel).
franquicia(doctor_doom, marvel).
franquicia(gambit, marvel).
franquicia(hulk, marvel).
franquicia(iceman, marvel).
franquicia(iron_man, marvel).
franquicia(juggernaut, marvel).
franquicia(magneto, marvel).
franquicia(marrow, marvel).
franquicia(omega_red, marvel).
franquicia(psylocke, marvel).
franquicia(rogue, marvel).
franquicia(sabretooth, marvel).
franquicia(sentinel, marvel).
franquicia(shuma_gorath, marvel).
franquicia(silver_samurai, marvel).
franquicia(spider_man, marvel).
franquicia(spiral, marvel).
franquicia(storm, marvel).
franquicia(thanos, marvel).
franquicia(venom, marvel).
franquicia(war_machine, marvel).
franquicia(wolverine, marvel).
franquicia(bone_wolverine, marvel).

% Asignación a la franquicia de capcom
franquicia(akuma, capcom).
franquicia(amingo, capcom).
franquicia(anakaris, capcom).
franquicia(bb_hood, capcom).
franquicia(cammy, capcom).
franquicia(captain_commando, capcom).
franquicia(charlie, capcom).
franquicia(chun_li, capcom).
franquicia(dan, capcom).
franquicia(dhalsim, capcom).
franquicia(felicia, capcom).
franquicia(guile, capcom).
franquicia(hayato, capcom).
franquicia(jill, capcom).
franquicia(jin, capcom).
franquicia(ken, capcom).
franquicia(m_bison, capcom).
franquicia(mega_man, capcom).
franquicia(morrigan, capcom).
franquicia(roll, capcom).
franquicia(ruby_heart, capcom).
franquicia(ryu, capcom).
franquicia(sakura, capcom).
franquicia(servbot, capcom).
franquicia(sonson, capcom).
franquicia(strider_hiryu, capcom).
franquicia(tron_bonne, capcom).
franquicia(zangief, capcom).


% CAPCOM

% ---------------------------------------------------------
% STREET FIGHTER
% ---------------------------------------------------------
grupo(zangief, street_fighter).
grupo(cammy, street_fighter).
grupo(guile, street_fighter).
grupo(chun_li, street_fighter).
grupo(m_bison, street_fighter).
grupo(charlie, street_fighter).
grupo(dhalsim, street_fighter).
grupo(dan, street_fighter).
grupo(sakura, street_fighter).
grupo(ryu, street_fighter).
grupo(ken, street_fighter).
grupo(akuma, street_fighter).

% ---------------------------------------------------------
% DARKSTALKERS
% ---------------------------------------------------------
grupo(morrigan, darkstalkers).
grupo(felicia, darkstalkers).
grupo(anakaris, darkstalkers).
grupo(bb_hood, darkstalkers).

% ---------------------------------------------------------
% MEGA MAN
% ---------------------------------------------------------
grupo(mega_man, mega_man).
grupo(roll, mega_man).
grupo(tron_bonne, mega_man).
grupo(servbot, mega_man).

% ---------------------------------------------------------
% SEPARADOS
% ---------------------------------------------------------
grupo(strider_hiryu, strider).
grupo(hayato, star_gladiator).
grupo(jin, cyberbots).
grupo(jill, resident_evil).
grupo(captain_commando, captain_commando).
grupo(sonson, sonson).
grupo(amingo, original_characters).
grupo(ruby_heart, original_characters).

% GRUPO MARVEL

% ---------------------------------------------------------
% X-MEN
% ---------------------------------------------------------
grupo(juggernaut, x_men).
grupo(iceman, x_men).
grupo(magneto, x_men).
grupo(cable, x_men).
grupo(sentinel, x_men).
grupo(sabretooth, x_men).
grupo(marrow, x_men).
grupo(spiral, x_men).
grupo(cyclops, x_men).
grupo(colossus, x_men).
grupo(omega_red, x_men).
grupo(psylocke, x_men).
grupo(rogue, x_men).
grupo(gambit, x_men).
grupo(storm, x_men).
grupo(silver_samurai, x_men).
grupo(wolverine, x_men).
grupo(bone_wolverine, x_men).

% ---------------------------------------------------------
% VILLANO
% ---------------------------------------------------------
grupo(blackheart, villano).
grupo(shuma_gorath, villano).
grupo(doctor_doom, villano).
grupo(thanos, villaino).

% ---------------------------------------------------------
% SPIDER-MAN
% ---------------------------------------------------------
grupo(spider_man, spider_man).
grupo(venom, spider_man).

% ---------------------------------------------------------
% IRON MAN
% ---------------------------------------------------------
grupo(iron_man, iron_man).
grupo(war_machine, iron_man).

% ---------------------------------------------------------
% SEPARADOS
% ---------------------------------------------------------
grupo(hulk, the_hulk).
grupo(captain_america, captain_america).


% GÉNERO

% ---------------------------------------------------------
% MUJERES
% ---------------------------------------------------------
genero(cammy, mujer).
genero(chun_li, mujer).
genero(sakura, mujer).
genero(morrigan, mujer).
genero(felicia, mujer).
genero(bb_hood, mujer).
genero(roll, mujer).
genero(tron_bonne, mujer).
genero(jill, mujer).
genero(sonson, mujer).
genero(ruby_heart, mujer).
genero(marrow, mujer).
genero(spiral, mujer).
genero(psylocke, mujer).
genero(rogue, mujer).
genero(storm, mujer).

% ---------------------------------------------------------
% HOMBRES
% ---------------------------------------------------------
genero(zangief, hombre).
genero(guile, hombre).
genero(m_bison, hombre).
genero(charlie, hombre).
genero(dhalsim, hombre).
genero(dan, hombre).
genero(ryu, hombre).
genero(ken, hombre).
genero(akuma, hombre).
genero(anakaris, hombre).
genero(mega_man, hombre).
genero(strider_hiryu, hombre).
genero(hayato, hombre).
genero(jin, hombre).
genero(captain_commando, hombre).
genero(juggernaut, hombre).
genero(iceman, hombre).
genero(magneto, hombre).
genero(cable, hombre).
genero(sabretooth, hombre).
genero(cyclops, hombre).
genero(colossus, hombre).
genero(omega_red, hombre).
genero(gambit, hombre).
genero(silver_samurai, hombre).
genero(wolverine, hombre).
genero(bone_wolverine, hombre).
genero(blackheart, hombre).
genero(doctor_doom, hombre).
genero(thanos, hombre).
genero(spider_man, hombre).
genero(venom, hombre).
genero(iron_man, hombre).
genero(war_machine, hombre).
genero(hulk, hombre).
genero(captain_america, hombre).

% ---------------------------------------------------------
% OTROS (Robots, Plantas, Entes)
% ---------------------------------------------------------
genero(servbot, otro).
genero(amingo, otro).
genero(sentinel, otro).
genero(shuma_gorath, otro).

% ==============================================================================
% ESPECIE / NATURALEZA
% ==============================================================================
% Nota: Algunos personajes tienen múltiples entradas si son híbridos.

% ---------------------------------------------------------
% HUMANOS (Base)
% ---------------------------------------------------------
especie(zangief, humano).
especie(cammy, humano).
especie(guile, humano).
especie(chun_li, humano).
especie(m_bison, humano).
especie(charlie, humano).
especie(dhalsim, humano).
especie(dan, humano).
especie(sakura, humano).
especie(ryu, humano).
especie(ken, humano).
especie(akuma, humano).
especie(bb_hood, humano).
especie(tron_bonne, humano).
especie(strider_hiryu, humano).
especie(hayato, humano).
especie(jin, humano).
especie(jill, humano).
especie(captain_commando, humano).
especie(ruby_heart, humano).
especie(doctor_doom, humano).
especie(iron_man, humano).
especie(war_machine, humano).
especie(venom, humano). % Dependencia del huésped (Eddie Brock)

% ---------------------------------------------------------
% HUMANOS MUTADOS / ALTERADOS (Ciencia o magia, sin Gen X)
% ---------------------------------------------------------
especie(spider_man, humano_mutado).
especie(hulk, humano_mutado).
especie(captain_america, humano_mutado).
especie(juggernaut, humano_mutado). % Poder otorgado por la gema de Cyttorak

% ---------------------------------------------------------
% MUTANTES (Portadores del Gen X)
% ---------------------------------------------------------
especie(iceman, mutante).
especie(magneto, mutante).
especie(cable, mutante).
especie(sabretooth, mutante).
especie(marrow, mutante).
especie(cyclops, mutante).
especie(colossus, mutante).
especie(omega_red, mutante).
especie(psylocke, mutante).
especie(rogue, mutante).
especie(gambit, mutante).
especie(storm, mutante).
especie(silver_samurai, mutante).
especie(wolverine, mutante).
especie(bone_wolverine, mutante).

% ---------------------------------------------------------
% ROBOTS / CYBORGS / ANDROIDES
% ---------------------------------------------------------
especie(mega_man, robot).
especie(roll, robot).
especie(servbot, robot).
especie(sentinel, robot).
especie(cable, cyborg).     % Híbrido: Mutante y Cyborg
especie(omega_red, cyborg). % Híbrido: Mutante y Cyborg
especie(spiral, cyborg).    % Híbrido: Extraterrestre y Cyborg

% ---------------------------------------------------------
% EXTRATERRESTRES / ALIENÍGENAS
% ---------------------------------------------------------
especie(thanos, extraterrestre).
especie(spiral, extraterrestre). % Habitante del Mojoverso
especie(venom, extraterrestre).  % El Simbionte

% ---------------------------------------------------------
% DEMONIOS / MONSTRUOS / ENTIDADES MÁGICAS
% ---------------------------------------------------------
especie(morrigan, demonio).
especie(blackheart, demonio).
especie(felicia, monstruo). % Mujer gato
especie(anakaris, no_muerto).
especie(shuma_gorath, entidad_cosmica).
especie(sonson, bestia).

% ---------------------------------------------------------
% PLANTAS
% ---------------------------------------------------------
especie(amingo, planta).

% ==============================================================================
% NIVEL DE MUTANTE (Clasificación del Gen X según el canon de Marvel)
% ==============================================================================
% ---------------------------------------------------------
% NIVEL OMEGA 
% ---------------------------------------------------------
nivel_mutante(iceman, omega).
nivel_mutante(magneto, omega).
nivel_mutante(storm, omega).

% ---------------------------------------------------------
% NIVEL ALPHA 
% ---------------------------------------------------------
nivel_mutante(cyclops, alpha).
nivel_mutante(psylocke, alpha).
nivel_mutante(rogue, alpha).
nivel_mutante(gambit, alpha).
nivel_mutante(colossus, alpha).
nivel_mutante(omega_red, alpha).
nivel_mutante(silver_samurai, alpha).
nivel_mutante(cable, alpha). % Canon: Tiene potencial Omega, pero el virus T-O lo limita a Alpha.

% ---------------------------------------------------------
% NIVEL BETA
% ---------------------------------------------------------
nivel_mutante(wolverine, beta).     
nivel_mutante(bone_wolverine, beta). 
nivel_mutante(sabretooth, beta).    
nivel_mutante(marrow, beta).  

% ==============================================================================
% PRIMERA APARICIÓN (Historia y Lore)
% Estructura: primera_aparicion(Personaje, Año, 'Obra/Cómic/Juego').
% ==============================================================================

% ---------------------------------------------------------
%  MARVEL (Cómics)
% ---------------------------------------------------------
primera_aparicion(captain_america, 1941, 'Captain America Comics #1').
primera_aparicion(spider_man, 1962, 'Amazing Fantasy #15').
primera_aparicion(doctor_doom, 1962, 'The Fantastic Four #5').
primera_aparicion(hulk, 1962, 'The Incredible Hulk #1').
primera_aparicion(cyclops, 1963, 'The X-Men #1').
primera_aparicion(iceman, 1963, 'The X-Men #1').
primera_aparicion(magneto, 1963, 'The X-Men #1').
primera_aparicion(iron_man, 1963, 'Tales of Suspense #39').
primera_aparicion(juggernaut, 1965, 'The X-Men #12').
primera_aparicion(sentinel, 1965, 'The X-Men #14').
primera_aparicion(shuma_gorath, 1973, 'Marvel Premiere #5').
primera_aparicion(thanos, 1973, 'Iron Man #55').
primera_aparicion(silver_samurai, 1974, 'Daredevil #111').
primera_aparicion(wolverine, 1974, 'The Incredible Hulk #180').
primera_aparicion(colossus, 1975, 'Giant-Size X-Men #1').
primera_aparicion(storm, 1975, 'Giant-Size X-Men #1').
primera_aparicion(psylocke, 1976, 'Captain Britain #8').
primera_aparicion(sabretooth, 1977, 'Iron Fist #14').
primera_aparicion(rogue, 1981, 'Avengers Annual #10').
primera_aparicion(spiral, 1985, 'Longshot #1').
primera_aparicion(venom, 1988, 'The Amazing Spider-Man #299').
primera_aparicion(blackheart, 1989, 'Daredevil #270').
primera_aparicion(cable, 1990, 'New Mutants #87').
primera_aparicion(gambit, 1990, 'Uncanny X-Men #266').
primera_aparicion(omega_red, 1992, 'X-Men #4').
primera_aparicion(war_machine, 1992, 'Iron Man #281').
primera_aparicion(bone_wolverine, 1993, 'Wolverine #75'). % Año en que Magneto extrae su Adamantium
primera_aparicion(marrow, 1995, 'X-Men Prime #1').

% ---------------------------------------------------------
% CAPCOM (Videojuegos)
% ---------------------------------------------------------
primera_aparicion(ryu, 1987, 'Street Fighter').
primera_aparicion(ken, 1987, 'Street Fighter').
primera_aparicion(mega_man, 1987, 'Mega Man').
primera_aparicion(roll, 1987, 'Mega Man').
primera_aparicion(strider_hiryu, 1989, 'Strider').
primera_aparicion(chun_li, 1991, 'Street Fighter II').
primera_aparicion(guile, 1991, 'Street Fighter II').
primera_aparicion(zangief, 1991, 'Street Fighter II').
primera_aparicion(dhalsim, 1991, 'Street Fighter II').
primera_aparicion(m_bison, 1991, 'Street Fighter II').
primera_aparicion(captain_commando, 1991, 'Captain Commando').
primera_aparicion(cammy, 1993, 'Super Street Fighter II').
primera_aparicion(akuma, 1994, 'Super Street Fighter II Turbo').
primera_aparicion(morrigan, 1994, 'Darkstalkers: The Night Warriors').
primera_aparicion(felicia, 1994, 'Darkstalkers: The Night Warriors').
primera_aparicion(anakaris, 1994, 'Darkstalkers: The Night Warriors').
primera_aparicion(charlie, 1995, 'Street Fighter Alpha').
primera_aparicion(dan, 1995, 'Street Fighter Alpha').
primera_aparicion(jin, 1995, 'Cyberbots: Fullmetal Madness').
primera_aparicion(sakura, 1996, 'Street Fighter Alpha 2').
primera_aparicion(hayato, 1996, 'Star Gladiator').
primera_aparicion(jill, 1996, 'Resident Evil').
primera_aparicion(bb_hood, 1997, 'Vampire Savior').
primera_aparicion(tron_bonne, 1997, 'Mega Man Legends').
primera_aparicion(servbot, 1997, 'Mega Man Legends').
primera_aparicion(amingo, 2000, 'Marvel vs. Capcom 2').
primera_aparicion(ruby_heart, 2000, 'Marvel vs. Capcom 2').
primera_aparicion(sonson, 2000, 'Marvel vs. Capcom 2'). % Es SonSon III, nieta del personaje arcade de 1984

% ==============================================================================
% PERSONAJE PRINCIPAL / REPRESENTANTE DEL GRUPO
% Estructura: personaje_principal(Grupo, Personaje).
% ==============================================================================

% ---------------------------------------------------------
% LADO CAPCOM
% ---------------------------------------------------------
personaje_principal(street_fighter, ryu).
personaje_principal(darkstalkers, morrigan).
personaje_principal(mega_man, mega_man).
personaje_principal(strider, strider_hiryu).
personaje_principal(star_gladiator, hayato).
personaje_principal(cyberbots, jin).
personaje_principal(resident_evil, jill).
personaje_principal(captain_commando, captain_commando).
personaje_principal(sonson, sonson).
personaje_principal(marvelVScapcomII, ruby_heart). 

% ---------------------------------------------------------
% LADO MARVEL
% ---------------------------------------------------------
personaje_principal(x_men, cyclops).
personaje_principal(villano, doctor_doom).
personaje_principal(spider_man, spider_man).
personaje_principal(iron_man, iron_man).
personaje_principal(the_hulk, hulk).
personaje_principal(captain_america, captain_america).


% ==============================================================================
% ORIGEN / NACIONALIDAD
% Estructura: origen(Personaje, Pais_o_Lugar).
% ==============================================================================

% ---------------------------------------------------------
% LADO MARVEL
% ---------------------------------------------------------
origen(captain_america, estados_unidos).
origen(spider_man, estados_unidos).
origen(iron_man, estados_unidos).
origen(hulk, estados_unidos).
origen(war_machine, estados_unidos).
origen(venom, estados_unidos).
origen(cyclops, estados_unidos).
origen(iceman, estados_unidos).
origen(gambit, estados_unidos).
origen(rogue, estados_unidos).
origen(juggernaut, estados_unidos).
origen(cable, estados_unidos).
origen(sentinel, estados_unidos).
origen(marrow, estados_unidos).
origen(wolverine, canada).
origen(bone_wolverine, canada).
origen(sabretooth, canada).
origen(colossus, rusia).
origen(omega_red, rusia).
origen(psylocke, reino_unido).
origen(magneto, alemania).
origen(silver_samurai, japon).
origen(storm, kenia).
origen(doctor_doom, latveria).
origen(thanos, titan). 
origen(shuma_gorath, dimension_del_caos).
origen(blackheart, inframundo).
origen(spiral, mojoverso).


% ---------------------------------------------------------
% LADO CAPCOM
% ---------------------------------------------------------
origen(ryu, japon).
origen(sakura, japon).
origen(akuma, japon).
origen(mega_man, japon).
origen(roll, japon).
origen(strider_hiryu, japon).
origen(hayato, japon).
origen(jin, japon).
origen(ken, estados_unidos).
origen(guile, estados_unidos).
origen(charlie, estados_unidos).
origen(felicia, estados_unidos).
origen(jill, estados_unidos).
origen(captain_commando, estados_unidos).
origen(chun_li, china).
origen(sonson, china).
origen(zangief, rusia).
origen(dhalsim, india).
origen(cammy, reino_unido).
origen(dan, hong_kong).
origen(morrigan, escocia).
origen(anakaris, egipto).
origen(bb_hood, europa_del_norte).
origen(tron_bonne, isla_kattelox).
origen(servbot, isla_kattelox).
origen(m_bison, desconocido). % Origen exacto encubierto por Shadaloo
origen(amingo, desconocido).
origen(ruby_heart, desconocido).

es_lugar_real(estados_unidos).
es_lugar_real(canada).
es_lugar_real(rusia).
es_lugar_real(reino_unido).
es_lugar_real(alemania).
es_lugar_real(japon).
es_lugar_real(kenia).
es_lugar_real(china).
es_lugar_real(india).
es_lugar_real(hong_kong).
es_lugar_real(escocia).
es_lugar_real(egipto).
es_lugar_real(europa_del_norte).



% ==============================================================================
% 				LISTA DE REGLAS 
% ==============================================================================


equipo_crossover_lore(LiderCapcom, MutanteElite, VillanoAntiguo) :-
    % 1. Condición del líder: Rostro principal de un grupo y perteneciente a Capcom
    personaje_principal(_, LiderCapcom),
    franquicia(LiderCapcom, capcom),
    
    % 2. Condición del mutante: Especie mutante y nivel omega o alpha
    especie(MutanteElite, mutante),
    (nivel_mutante(MutanteElite, omega) ; nivel_mutante(MutanteElite, alpha)),
    
    % 3. Condición del villano: Demonio o del grupo de villanos, debut anterior a 1990
    (especie(VillanoAntiguo, demonio) ; grupo(VillanoAntiguo, villains)),
    primera_aparicion(VillanoAntiguo, Anio, _),
    Anio < 1990,
    
    % 4. Validación: Evitar que el mismo personaje ocupe dos puestos
    LiderCapcom \= MutanteElite,
    LiderCapcom \= VillanoAntiguo,
    MutanteElite \= VillanoAntiguo.

lider_veterano_no_humano(Personaje, Año, Obra) :-
    personaje_principal(_, Personaje),
    primera_aparicion(Personaje, Año, Obra),
    Año < 1990,
    \+ especie(Personaje, humano). % Excluye estrictamente a los humanos

origen_ficticio(Personaje, Lugar) :-
    origen(Personaje, Lugar),
    \+ es_lugar_real(Lugar),
    Lugar \= desconocido.
