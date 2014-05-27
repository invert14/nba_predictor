y = y_sezon06;
yk = zeros(size(y,1),1);

for i=1:size(y,1)
    if(y(i)<1)
        yk(i) = 0;
    else
        yk(i) = 1;
    end
end

y_sezon06k = yk;