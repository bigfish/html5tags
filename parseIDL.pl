#!/usr/bin/perl

use File::Basename;
#extract IDL tags from HTML 5 spec
my $file = shift;

sub stripTags
{
	my $str = shift;
	$str =~ s/<[^>]*>//g;
	return $str;
}

sub stripComments
{
	my $str = shift;
	$str =~ s/\/\/.*//g;
	return $str;
}
sub cleanUp
{
	my $str = shift;
	return stripComments(stripTags($str));
}

sub processLine
{
#get link
  my $str = shift;
  my $link = "";
  if ($str =~ /<a href="(#[^"]*)"/) {
    $link = $1;
  }
  $str = cleanUp($str);
  return $str.$link;
}

#STAGE ONE
#
#generate interfaces data structure from spec file
#by first extracting all IDL parts

(my $filename, my $filepath, my $ext) = fileparse($file, qr{\..*});
#read file 
open(HANDLE, $file) || die ("could not open file $file");
my @lines = <HANDLE>;
close(HANDLE);

my @idl_lines = [];
my $is_idl = 0;
my $link = "";

foreach(@lines){

	chomp;

	my $line = $_;
  
  #remove IDL metadata
	$line =~ s/\[[^\]*]*\]//g;
	
	if ($is_idl){

	 	if($line =~ /(.*)<\/pre>/) {

			$is_idl = 0;
           
			push(@idl_lines, processLine($1));

		} else {

			push(@idl_lines, processLine($line));
		}

	}

  if (!$is_idl && $line =~ /<pre\s+class\s*=\s*"idl"[^>]*>(.*)/) {
		$is_idl = 1;

		push(@idl_lines, processLine($1));
	}

}
foreach(@idl_lines){
  my $line = $_;
#working around a bug where an ARRAY reference is getting dumped into a line
  if ($line !~ "^ARRAY"){
    if ($line){
      print $line."\n";
    }
  }
}



