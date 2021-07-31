#!/usr/bin/perl

use Image::Magick;
use CGI;
$cgi = CGI::new();

$xLength = $cgi->url_param('x') || 600;
$yLength = $cgi->url_param('y') || 450;
$fontSize = $cgi->url_param('fontSize') || 20;
$image = Image::Magick->new(magick => "png");
$image->Set(size => $xLength . "x" . $yLength);
$image->ReadImage("canvas:white");

$v2 = $cgi->url_param('v2');
$v1 = $cgi->url_param('value');
if ($v1) {
    $image->Annotate(
        text=>$v1,
        x=>4,
        y=>$fontSize,
        fill=>"#000000",
        strokewidth=>3,
        antialias=>true,
        font=>"./font.ttf",
        pointsize=>$fontSize
    );
} elsif(v2) {
    @columnsLength = split(/,/, $cgi->url_param('cols'));
    @lines = split(/\n/, $v2);
    $header = "┌" . join ("┬",  map { "─" x $_ } @columnsLength ) . "┐\n";
    $border = "├" . join ("┼",  map { "─" x $_ } @columnsLength ) . "┤\n";
    $footer = "└" . join ("┴", map { "─" x $_ } @columnsLength ) . "┘";
    $result = $header . join($border, (map { "│" . $_ . "│\n" } @lines)) . $footer;
    $image->Annotate(
        text=>$result,
        x=>4,
        y=>$fontSize,
        fill=>"#000000",
        strokewidth=>3,
        antialias=>true,
        font=>"./font.ttf",
        pointsize=>$fontSize
    );
} 

print ("Content-type: image/png\n\n");
binmode STDOUT;
$image->Write("png:-");

print "\n\n";
 
undef $image;
exit;
