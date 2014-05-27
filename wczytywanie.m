function [x y yk] = wczytywanie(nazwa_x, nazwa_y)

x_plik = load (nazwa_x);
y_plik = load (nazwa_y);

rozmiar_x = size(x_plik, 1);
rozmiar_y = size(y_plik, 1);
x = zeros(rozmiar_x/2,size(x_plik, 2));
y = zeros(rozmiar_y,1);
yk = zeros(rozmiar_y,1);

for i=1:(rozmiar_x/2)
    x(i,:) = x_plik(2*(i-1)+1,:)-x_plik(2*(i-1)+2,:);
end

for i=1:rozmiar_y
    
    y(i) = y_plik(i,1)-y_plik(i,2);
    if(y(i)<0)
        yk(i) = 0;
    else
        yk(i) = 1;
    end

end