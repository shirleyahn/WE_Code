version='1ball_1step_beta_20_r_0.4';
file1=load(strcat('flux_total_',version,'_1.txt'));
file2=load(strcat('flux_total_',version,'_2.txt'));
file3=load(strcat('flux_total_',version,'_3.txt'));

endpt=16769;
flux_avg=(file1(1:endpt,:)+file2(1:endpt,:)+file3(1:endpt,:))/3;
flux1=[file1(1:endpt,2).';file2(1:endpt,2).';file3(1:endpt,2).'];
flux2=[file1(1:endpt,3).';file2(1:endpt,3).';file3(1:endpt,3).'];

%flux_avg=(file1(1:endpt,:)+file2(1:endpt,:))/2;
%flux1=[file1(1:endpt,2).';file2(1:endpt,2).'];
%flux2=[file1(1:endpt,3).';file2(1:endpt,3).'];

flux1_std=std(flux1);
flux2_std=std(flux2);
flux_std=[(1:1:endpt);flux1_std;flux2_std].';

fid = fopen(strcat('flux_avg_',version,'.txt'), 'wt');
fprintf(fid, [repmat('%g\t', 1, size(flux_avg,2)-1) '%g\n'], flux_avg.');
fclose(fid);

fid = fopen(strcat('flux_std_',version,'.txt'), 'wt');
fprintf(fid, [repmat('%g\t', 1, size(flux_std,2)-1) '%g\n'], flux_std.');
fclose(fid);


%%
version='CAS_1ball_10steps_r_0.1';
file1=load(strcat(version,'_1/total_weight.txt'));
file2=load(strcat(version,'_2/total_weight.txt'));
file3=load(strcat(version,'_3/total_weight.txt'));

%flux_avg=(file1+file2+file3+file4)/4;
%flux1=[file1(:,2).';file2(:,2).';file3(:,2).';file4(:,2).'];
%flux2=[file1(:,3).';file2(:,3).';file3(:,3).';file4(:,3).'];

total_weight_avg=(file1+file2+file3)/3;

fid = fopen(strcat('total_weight_avg_',version,'.txt'), 'wt');
fprintf(fid, [repmat('%g\t', 1, size(total_weight_avg,2)-1) '%g\n'], total_weight_avg.');
fclose(fid);


%%
version='1ball_1step_beta_20_r_0.4';
file1=load(strcat('total_time_',version,'_1.txt'));
file2=load(strcat('total_time_',version,'_2.txt'));
file3=load(strcat('total_time_',version,'_3.txt'));

endpt=16769;
total_time_avg=(file1(1:endpt,:)+file2(1:endpt,:)+file3(1:endpt,:))/3;
%total_time_avg=(file1(1:endpt,:)+file2(1:endpt,:))/2;

fid = fopen(strcat('total_time_avg_',version,'.txt'), 'wt');
fprintf(fid, [repmat('%g\t', 1, size(total_time_avg,2)-1) '%g\n'], total_time_avg.');
fclose(fid);
