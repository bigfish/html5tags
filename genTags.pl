#!/usr/bin/perl
#accept the IDL file as parameter
use File::Basename;
$file = shift;

(my $filename, my $filepath, my $ext) = fileparse($file, qr{\..*});
#read file 
open(HANDLE, $file) || die ("could not open file $file");
my @lines = <HANDLE>;
close(HANDLE);

#we are going to construct a hash of interfaces hashes...
my %interfaces = ();
my %interface = ();

#each interface will have the following attributes
my %attributes = ();
my %methods = ();

#each attribute will be a hash with 3 attributes: name, type, is_readonly
my %attribute = ();
my $attr_name = "";
my $attr_type = "";

#each method has name, return_type, and params array
my $method_name = "";
my $return_type = "";
my @params = [];
my %param = ();

#each param has the following fields: param_name, param_type, is_optional
my $param_name = "";
my $param_type = "";
my $is_optional = 0;
#the special param name 'rest_args' allows for multiple optional arguments
#the special type 'any' allows any type

my $interface_name = "";
my $super_interface = "";
foreach(@lines){

	chomp;

	my $line = $_;

	if ($line =~ /^interface\s+([A-Za-z]+)\s*:?\s*([A-Za-z]+)\s*{\s*(?:})?/) {
		$interface_name = $1;
		$super_interface = $2;
		print "found interface: $interface_name \n";
	}
	

}
  
