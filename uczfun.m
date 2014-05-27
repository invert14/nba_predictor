function [ wsp ] = uczfun(x, y, testparam)
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
    if size(testparam, 1) == 0
        testparam = ones(size(x, 2), 1);
    end
    psize = 0;
    for i = 1:size(testparam, 2)
        if testparam(i) == 1
            psize = psize + 1;
        end
    end
    
    xreg = zeros(size(y, 1), psize);
    j = 1;
    for i = 1:size(testparam, 2)
       if testparam(i) == 1
           xreg(:,j) = x(:,i);
           j = j + 1;
       end
    end
    
    %jedynki = ones(size(xreg,1),1);
    %xreg = [xreg jedynki];
    tmp = mvregress(xreg, y);
    wsp = zeros(size(testparam, 2), 1);
    j = 1;
    for i = 1:size(testparam, 2)
        if testparam(i) == 1
            wsp(i,1) = tmp(j,1);
            j = j + 1;
        end
    end
    
end

