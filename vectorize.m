function [ y ] = vectorize( x )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
    y = zeros(1,33);
    for i=1:size(x,2)
        y(x(i)) = 1;
    end
end

