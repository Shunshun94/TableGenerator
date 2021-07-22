#!/usr/bin/perl

use Image::Magick;
use CGI;
$cgi = CGI::new();

$value = $cgi->url_param('value');
$xLength = $cgi->url_param('x') || 600;
$yLength = $cgi->url_param('y') || 450;
$image = Image::Magick->new(magick => "png");
$image->Set(size => $xLength . "x" . $yLength);
$image->ReadImage("canvas:white");

$image->Annotate(
    text=>$value,
    x=>4,
    y=>16,
    fill=>"#000000",
    strokewidth=>3,
    antialias=>true,
    font=>"./font.ttf",
    pointsize=>20
);

print ("Content-type: image/png\n\n");
binmode STDOUT;
$image->Write("png:-");

print "\n\n";
 
undef $image;
exit;
