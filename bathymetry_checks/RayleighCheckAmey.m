load('ut_constants.mat','const');

CONST = {'H1';'M2'; 'H2'}
clear TA
for i = 1:length(CONST)
    for j = 1:length(CONST)

        if i == j
            T(i,j) = NaN;
            continue
        end
        % Convert back to angular frequency
        Oa1 = const.freq(strcmp(cellstr(const.name),CONST{i})) * 360;
        Oa2 = const.freq(strcmp(cellstr(const.name),CONST{j})) * 360;

        d_Omega = abs(Oa1-Oa2);

        % Compute required data record length       Rayleigh criterion
        T(i,j) = (360/d_Omega)/(24*365);                             % [year]

        disp(['To distinguish ' CONST{i} ' and ' CONST{j} ' the required record length is ' num2str(T(i,j)) ' years aka ' num2str(T(i,j)*365) ' days'])

    end
end
 
figure, 
h = imagesc(T)
axis image %// equal scale on both axes
% axis ij
colormap(flipud(hot))
colorbar
xticks([1:length(CONST)]); yticks([1:length(CONST)])
xticklabels(CONST)
yticklabels(CONST)