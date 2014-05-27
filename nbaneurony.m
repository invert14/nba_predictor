function [ fit ] = nbaneurony( x_ucz, y_ucz, x_test, y_test, testparam, neurony)
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here

    if size(testparam, 1) == 0
        testparam = ones(size(x_ucz, 2), 1);
    end
    
    psize = 0;
    for i = 1:size(testparam, 2)
        if testparam(i) == 1
            psize = psize + 1;
        end
    end
    
    xn_ucz = zeros(size(y_ucz, 1), psize);
    xn_test = zeros(size(y_test, 1), psize);
    j = 1;
    for i = 1:size(testparam, 2)
       if testparam(i) == 1
           xn_ucz(:,j) = x_ucz(:,i);
           xn_test(:,j) = x_test(:,i);
           j = j + 1;
       end
    end
    
    %for i = 1:size(testparam, 1)
    %    if testparam(i) == 0
    %        x_ucz(:, i) = zeros(size(x_ucz, 1), 1);
    %        x_test(:, i) = zeros(size(x_test, 1), 1);
    %    end
    %end
    wejscia = [zeros(psize,1) 5*ones(psize,1)];
    
    net = newff(wejscia, [8 4 1], {'tansig', 'tansig', 'purelin'});
    net.trainParam.epochs = 20;
    net.trainParam.goal = 0.01;
    
    xn_ucz = xn_ucz';
    y_ucz = y_ucz';

    net = train(net, xn_ucz, y_ucz);

    xn_test = xn_test';
    y_net = sim(net, xn_test);

    fit = 0;
    for i = 1:size(y_net, 2)
        if((y_net(i) > 1 && y_test(i) > 1) || (y_net(i) < 1 && y_test(i) < 1))
                fit = fit + 1;
        end
    end
    fit = fit / size(y_net, 2);
    disp('Zgodnoœæ wyników:')
    disp(fit);

end

