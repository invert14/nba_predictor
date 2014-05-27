function [ fit ] = testfun(x, y, param, testparam, klas)
%testfun funkcja sluzaca do testowania obliczonych w regresji liniowej
%wspolczynnikow
%   x - zbiór badany; y - wyniki do porównania; param - parametry obliczone
%   w regresji liniowej(wektor kolumnowy); testparam - wektor zawierajacy 0
%   lub 1 w zaleznosci czy dany parametr ma byc wykorzystany
    if size(testparam, 1) == 0
        testparam = ones(size(param, 1), 1);
    end
    
    fit = 0;
    for i = 1:size(x, 1)
        sim = 0;
        for j = 1:size(param, 1)
            if testparam(j) == 1
                sim = sim + param(j) * x(i, j);
            end
        end
        if(((sim > 1 && y(i) > 1) || (sim < 1 && y(i) < 1)) && (klas == 0))
            fit = fit + 1;
        else
            if(((sim > 0.5 && y(i) > 0.5) || (sim < 0.5 && y(i) < 0.5)) && (klas == 1))
                fit = fit + 1;
            end
        end
    end
    
    fit = fit / size(x, 1);
    %disp('Zgodnoœæ wyników:');
    %disp(fit);
end

