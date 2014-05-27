
k = 10;
x = xs;
y = ys;
wyniki3 = zeros(1,40);
%for q=1:33
%ktore = zbyszek([1:17 33]);
ktore = zbyszek ([1 7 9 13 15 16 17 20 22 23 24 26 27 28 30 31 32]);
neurony = 8;
%%for n=1:40
rozmiar = floor(((k-1)/k) * size(x, 1));
r_czesci = floor((1/k) * size(x, 1));
wyn = 0;
for i=1:k
    x_uczace = zeros(rozmiar, size(x, 2));
    licz = 0;
    for j=1:k
        if(i ~= j)
            x_uczace(((licz*r_czesci)+1):((licz+1)*r_czesci),:) = x((((j-1)*r_czesci)+1):(j*r_czesci),:);
            y_uczace(((licz*r_czesci)+1):((licz+1)*r_czesci),:) = y((((j-1)*r_czesci)+1):(j*r_czesci),:);
            licz = licz + 1;
        else
            x_test = x((((j-1)*r_czesci)+1):(j*r_czesci),:);
            y_test = y((((j-1)*r_czesci)+1):(j*r_czesci),:);
        end
    end 
    %wyn = wyn + nbalinreg(x_uczace, y_uczace, x_test, y_test, ktore, 1);
    wyn = wyn + nbaneurony(x_uczace, y_uczace, x_test, y_test, ktore, neurony);
end
wyn = wyn / k;
%wyniki3(n) = wyn;
disp(wyn);
%end
%wyniki(q) = wyn;
%end