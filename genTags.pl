#!/usr/bin/perl
#accept the IDL file as parameter
use File::Basename;
$file = shift;

(my $filename, my $filepath, my $ext) = fileparse($file, qr{\..*});
#read file 
open(HANDLE, $file) || die ("could not open file $file");
my @lines = <HANDLE>;
close(HANDLE);

# STAGE 1 : create data structure from interface declarations in IDL
#we are going to construct a hash of interfaces hashes...
my %interfaces = ();
my %interface = ();

#each interface will have the following attributes
my @attributes = ();
my @methods = ();

#each attribute will be a hash with 3 attributes: name, type, is_readonly
my %attribute = ();
my $attr_name = "";
my $attr_type = "";
my $is_readonly = "";

#each method has name, return_type, and params array
my $method_name = "";
my $return_type = "";
my @params = [];
my %param = ();

#each param has the following fields: param_name, param_type, is_optional
my $param_name = "";
my $param_type = "";
my $is_optional = 0;
#the special param name 'args' allows for multiple optional arguments
#the special type 'any' allows any type

my $interface_name = "";
my $super_interface = "";
my $is_empty = "";
my $signature = "";
foreach(@lines){

	chomp;

	my $line = $_;

	if ($line =~ /^interface\s+([A-Za-z]+)\s*(?::\s*([A-Za-z]+))?\s*{\s*(};)?/) {
		$interface_name = $1;
		$super_interface = $2;
		$is_empty = $3;
		#print "found interface: $interface_name \n";
		%interface = ();
		if ($super_interface) {
			$interface{ 'supertype' } = $super_interface;
		}
	}

	if ($is_empty || $line =~ /^\s*};\s*$/) {

		#end of interface declaration
		#add interface with accumulated values
		$interfaces{$interface_name} = %interface;
		#debug
		#print keys $interfaces{ $interface_name }{'attributes'} . "\n";

		#reset vars
		@attributes = [];
		@methods = ();
		%attribute = ();
		$attr_name = "";
		$attr_type = "";
		$is_readonly = "";
		$method_name = "";
		$return_type = "";
		@params = [];
		%param = ();
		$param_name = "";
		$param_type = "";
		$is_optional = 0;
		$interface_name = "";
		$super_interface = "";
		$is_empty = "";
	}
	if ($interface_name) {
		
		#attributes
		if ($line =~ /^\s*(readonly)?\s+attribute\s+([A-Za-z]*)\s+([A-Za-z_0-9]*);/) {
			$is_readonly = $1;
			$attr_type = $2;
			$attr_name = $3;
			push(@attributes, {
				'attr_name'	=> $attr_name,
				'attr_type' => $attr_type,
				'is_readonly' => $is_readonly
			});
		}
		#methods
		if ($line =~ /^\s*([A-Z-a-z]*)\s+([A-Za-z0-9_]+)\s*\(([^)]*)\);/ ) {
			#print "found method $1 $2 $3 \n";
			$return_type = $1;
			$method_name = $2;
			$signature = $3;
			if ($signature) {
				#parse params
				my @params_str = split(/,/, $signature);
				foreach(@params_str) {
					$param_str = $_;
					if ( $param_str =~ /\s*(?:in)?\s*([A-Za-z]+)[\.]*\s+([A-Za-z_]+)\s*/ ){
						push(@params, {
							'param_name' => $2,
							'param_type' => $1
						});
					}
				}
			}
		}
		#TODO: deal with the X implements Y statements
	}

}

#STAGE 2 : re-parse HTML spec file and create tags based on interfaces implemented by elements
$file = "index.html";

(my $filename, my $filepath, my $ext) = fileparse($file, qr{\..*});
#read file 
open(HANDLE, $file) || die ("could not open file $file");
my @lines = <HANDLE>;
close(HANDLE);

#example element definition
#</div><h4 id="the-noscript-element"><span class="secno">4.3.2 </span>The <dfn><code>noscript</code></dfn> element</h4><p class="XXX annotation"><b>Status: </b><i>Last call for comments</i></p><dl class="element"><dt>Categories</dt>
# this is followed soon after by a 'Uses' section
#<dd>Uses <code><a href="http://www.w3.org/TR/html5/Overview.html#htmlelement">HTMLElement</a></code>.</dd>
# for each value of 'uses' make tags for that interface and any ancestor interfaces
my $element_name = "";
my @element_interfaces = [];

foreach(@lines){

	chomp;

	my $line = $_;
	
	if ($line =~ /The\s<dfn>\s*<code>(\S*)<\/code>\s*<\/dfn>\s*element/ ){
		#finish off old element
		print "$element_name implements @element_interfaces \n";
		$element_name = $1;
		@element_interfaces = ();
	}

	if ($line =~ /<dd>\s*Uses\s*<code>\s*<a[^>]*>([^<]*)<\/a>/ ) {
		#print "$element_name implements interface: $1 \n";
		push(@element_interfaces, $1);
	}
	if ($line =~ /<pre\s*class="idl"\s*>\s*interface\s+<dfn[^>]+>([^<]*)<\/dfn>\s*\:\s*<a[^>]*>([^<]*)<\/a>/ ) {
		push(@element_interfaces, $1);
		if ($2) {
			push(@element_interfaces, $2);
		}
	}




	
} 
