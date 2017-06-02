data_array = csvread('output_rch.csv', 2); 
[nrows, ncols] = size(data_array); 
for row = 1:nrows
    a = data_array(row, 1);
    b = data_array(row, 2); 
    % and so on... 
end 