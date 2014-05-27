function [ fit, param ] = nbalinreg(x_ucz, y_ucz, x_test, y_test, testparam, klas)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
    %jedynki = ones(size(x_ucz,1),1);
    %x_ucz = [x_ucz jedynki];
    %jedynki = ones(size(x_test,1),1);
    %x_test = [x_test jedynki];
    param = uczfun(x_ucz, y_ucz, testparam);
    fit = testfun(x_test, y_test, param, testparam, klas);
end

