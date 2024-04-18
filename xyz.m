A = [1 2; 3 4]
B = [2 3; 4 5]

A+B
A*B

clc
clear

% x_val = 0:0.001:1;
x_val = linspace(0, 1)

f = @(x) x.^2
g = @(x) x.^4
g = @(x, y) [x + y; x .* y];

figure(1)
plot(x_val, f(x_val), 'r-', 'linewidth', 2)
hold on
plot(x_val, g(x_val), 'b-', 'linewidth', 2)
title('Schöne Funktion')
xlabel('x')
ylabel('y')
hold off

figure(2)
loglog(x_val, f(x_val), 'r-', 'linewidth', 2)
hold on
loglog(x_val, g(x_val), 'b-', 'linewidth', 2)
title('Schöne Funktion mit log-Achse')
xlabel('x')
ylabel('y')
hold off