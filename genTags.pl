#!/usr/bin/perl
#accept the IDL file as parameter
use File::Basename;
$file = shift;
$srcfile = $file;#use for jump location in tags

(my $filename, my $filepath, my $ext) = fileparse($file, qr{\..*});
#read file 
open(HANDLE, $file) || die ("could not open file $file");
my @lines = <HANDLE>;
close(HANDLE);

# STAGE 1 : create data structure from interface declarations in IDL
#we are going to construct a hash of interfaces hashes...
#my %interfaces = ();
#my %interface = ();

#each interface will have the following attributes
#my @attributes = ();
#my @methods = ();

#each attribute will be a hash with 3 attributes: name, type, is_readonly
#my %attribute = ();
my $attr_name = "";
my $attr_type = "";
my $is_readonly = "";

#each method has name, return_type, and params array
my $method_name = "";
my $return_type = "";
#my @params = [];
#my %param = ();

#each param has the following fields: param_name, param_type, is_optional
my $param_name = "";
my $param_type = "";
my $is_optional = 0;
#the special param name 'args' allows for multiple optional arguments
#the special type 'any' allows any type

my $interface_name = "";
my $inherit = "";
#my $is_empty = "";
my $signature = "";

my @tag_lines = [];
my $tag_line = "";

my $TAB = '	';
my $tag_line = "";
my $type_token = "";
my $sig;

foreach(@lines){

	chomp;

	my $line = $_;

	if ($line =~ /^interface\s+([A-Za-z]+)\s*(?::\s*([A-Za-z]+))?\s*{\s*(?:};)?/) {

		$typeToken = "c";
		$interface_name = $1;
		$inherit = $2;
		$tag_line = $interface_name.$TAB.$srcfile.$TAB.'/^'.$_.'$/;"'.$TAB.$typeToken.$TAB.'class:'.$interface_name;
		if ($inherit) {
			$tag_line = $tag_line.$TAB.'inherits:'.$inherit;
		}
		print $tag_line."\n";
		#$is_empty = $3;
		#print "found interface: $interface_name \n";
		#%interface = ();
		#if ($super_interface) {
			#$interface{ 'supertype' } = $super_interface;
		#}
	}


	if ($interface_name) {
		
		#attributes
		if ($line =~ /^\s*(readonly)?\s+attribute\s+([A-Za-z]*)\s+([A-Za-z_0-9]*);/) {
			$is_readonly = $1;
			$attr_type = $2;
			$attr_name = $3;
			$typeToken = "v";
			$tag_line = $attr_name.$TAB.$srcfile.$TAB.'/^'.$_.'$/;"'.$TAB.$typeToken.$TAB.'class:'.$interface_name;

			print $tag_line."\n";

			#push(@attributes, {
				#'attr_name'	=> $attr_name,
				#'attr_type' => $attr_type,
				#'is_readonly' => $is_readonly
			#});
		}
		#methods
		if ($line =~ /^\s*([A-Z-a-z]*)\s+([A-Za-z0-9_]+)\s*\(([^)]*)\);/ ) {
			#print "found method $1 $2 $3 \n";
			$typeToken = "m";
			$return_type = $1;
			$method_name = $2;
			$signature = $3;
			$sig = "(";
			my $isfirstparam = 1;

			if ($signature) {
				#parse params
				my @params_str = split(/,/, $signature);
				foreach(@params_str) {
					$param_str = $_;

					if ( $param_str =~ /\s*(?:in)?\s*([A-Za-z]+)[\.]*\s+([A-Za-z_]+)\s*/ ){
						$param_type = $1;
						$param_name = $2;
						if ($isfirstparam) {
							$sig .= '<+'.$param_name.":".$param_type.'+>' ;
							$isfirstparam = 0;
						} else {
							$sig .= ", " . '<+'.$param_name.":".$param_type.'+>' ;
							#$sig .=  ", " . $param_type . " " . $param_name;
						}

					}
				}
			}

			$sig .= ")";
			$tag_line = $attr_name.$TAB.$srcfile.$TAB.'/^'.$_.'$/;"'.$TAB.$typeToken.$TAB.'class:'.$interface_name.$TAB.'signature:'.$sig;
			print $tag_line."\n";
		}
	}

	#end of interface declaration -- cleanup
	if ($line =~ /.*};\s*$/) {

		#add interface with accumulated values
		$interfaces{$interface_name} = %interface;
		#debug
		#print keys $interfaces{ $interface_name }{'attributes'} . "\n";

		#reset vars
		#@attributes = [];
		#@methods = ();
		#%attribute = ();
		$attr_name = "";
		$attr_type = "";
		$is_readonly = "";
		$method_name = "";
		$return_type = "";
		#@params = [];
		#%param = ();
		$param_name = "";
		$param_type = "";
		$is_optional = 0;
		$interface_name = "";
		$super_interface = "";
		#$is_empty = "";
		$tag_line = "";
		$type_token = "";
	}

}
