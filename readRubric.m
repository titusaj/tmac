% readRubric function 
% Titus John
% 9/21/2019

% Input 
% A jpg image with the highlighted spots


% Output
%  Out the map of this image space 
% This map is like a heat map 



function [] = readRubric() 

%%  Read in image into an array.
[rgbImage storedColorMap] = imread('testRubric.jpg');

%%  convert the HSV space
HSV = rgb2hsv(im);

%%  

%% Bound around pixel space of intrest based on the saturation


%% Take the bounding box do character recogonition

%% 


end