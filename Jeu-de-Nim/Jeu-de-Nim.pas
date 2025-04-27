//Programme réalisé par Matthieu Meunier

program Alumettes;
uses crt;

{ -initialisation des variables globales- }

var
  prenomja: string;  //ja = j1
  prenomjb: string;  //jb = j2
  joueur: integer;  //donne quel joueur est en train de jouer
  
{ -sous programmes- }

procedure prenom();  //demande le prénom de chaque joueur et le récupère sous forme d'un string
begin
	writeln('Entrez votre prénom joueur 1 :');
  readln(prenomja);
  writeln('Entrez votre prénom joueur 2 :');
  readln(prenomjb);
end;

function c_a_ki(o: integer): string;  //revoie le nom du joueur qui est en train de jouer
begin
  if o = 1 then
  begin
    c_a_ki := prenomja;
  end
  else
  begin
    c_a_ki := prenomjb;
  end
end;

{ procédure principal permettant de faire tourner le jeu }
procedure jeuAllumettes(n: integer);
  procedure allumettes();  //procedure qui affiche le bon nb d'allumettes
  var
    i: integer;  //compteur
  begin
    for i := 1 to n do  //boucle affichant n allumettes
    begin
      write(' | ');
    end;
  end;

var
  m: integer;  //nombre d'allumettes à enlever

begin
  joueur := 1;  //le joueur 1 commence
  m := 1;
  writeln(#10'Il y a ',n,' allumettes pour cette partie :'#10);  //donne le nb d'allumettes au début de la partie

  while n>0 do
  begin
    writeln(#10'Combien d allumettes voulez-vous retirer entre 1 et 3 ',c_a_ki(joueur),' ?',#10);
    allumettes();  //affiche le bon nb allumettes
    write(#10);
    readln(m);
    if (m>0) and (m<4) then
    begin
      joueur := joueur mod 2 +1;  //passe au joueur suivant
      n := n-m;
    end
    else
    begin
      write('Vous ne pouvez enlever que 1, 2 ou 3 allumettes',#10)
    end;
  end;
  writeln(#10,c_a_ki(joueur mod 2 +1),' a gagné !!!',#10);
end;

{ -programme principal- }

begin
  prenom();
  jeuAllumettes(12)
end.