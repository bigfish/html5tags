#!/usr/bin/perl

use File::Basename;

$file = shift;
$html_spec = shift;
$doc_url = shift;

(my $filename, my $filepath, my $ext) = fileparse($file, qr{\..*});
#read file 
open(HANDLE, $file) || die ("could not open file $file");
my @lines = <HANDLE>;
close(HANDLE);

my $attr_name = "";
my $attr_type = "";
my $is_readonly = "";

my $method_name = "";
my $return_type = "";

my $param_name = "";
my $param_type = "";
my $is_optional = 0;
#the special param name 'args' allows for multiple optional arguments
#the special type 'any' allows any type

my $interface_name = "";
my $inherit = "";
my $signature = "";

my @tag_lines = [];
my $tag_line = "";

my $TAB = '	';
my $tag_line = "";
my $type_token = "";
my $sig;
my $cmd;

foreach(@lines){

	chomp;

	my $line = $_;

	if ($line =~ /^interface\s+([A-Za-z0-9]+)\s*(?::\s*([A-Za-z0-9]+))?\s*{\s*(?:};)?(#.*)?/i) {

		$typeToken = "c";
		$interface_name = $1;
		$inherit = $2;
		$link = $3;
		#set cmd to the url of the definition
		$tag_line = $interface_name.$TAB.$html_spec.$TAB.'/^'.$_.'$/;"'.$TAB.$typeToken.$TAB.'class:'.$interface_name.$TAB.'type:constructor';
		if ($inherit) {
			$tag_line = $tag_line.$TAB.'inherits:'.$inherit;
		}
		if ($link){
			$tag_line = $tag_line.$TAB.'link:'.$link;
		}
		if ($interface_name){
			push(@tag_lines, $tag_line);
		}
	}


	if ($interface_name) {
		
		#attributes
		if ($line =~ /^\s*(readonly)?\s+attribute\s+([A-Za-z0-9]*)\s+([A-Za-z_0-9]*);(#.*)?/i) {

			$is_readonly = $1;
			$attr_type = $2;
			$attr_name = $3;
			$link = $4;
			$typeToken = "v";
			$tag_line = $attr_name.$TAB.$html_spec.$TAB.'/^'.$_.'$/;"'.$TAB.$typeToken.$TAB.'class:'.$interface_name.$TAB.'type:'.$attr_type;
			if ($link){
				$tag_line = $tag_line.$TAB.'link:'.$link;
			}
			push(@tag_lines, $tag_line);
		}

		#methods
		if ($line =~ /^\s*([A-Za-z]+)\s*(?:<[^>]*>\s*)?([A-Za-z0-9_]+)\s*(?:\s*<[^>]*>)?\s*\(([^)]*)\);(#.*)?/i ) {
			$typeToken = "m";
			$return_type = $1;
			$method_name = $2;
			$signature = $3;
			$link = $4;
			$sig = "(";

			my $isfirstparam = 1;

			if ($signature) {
				#parse params
				my @params_str = split(/,/, $signature);
				foreach(@params_str) {
					$param_str = $_;

					if ( $param_str =~ /\s*(?:in)?\s*([A-Za-z0-9]+)[\.]*\s+([A-Za-z_0-9]+)\s*/i ){
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
			$tag_line = $method_name.$TAB.$html_spec.$TAB.'/^'.$_.'$/;"'.$TAB.$typeToken.$TAB.'class:'.$interface_name.$TAB.'signature:'.$sig.$TAB.'type:'.$return_type;
			if ($link){
				$tag_line = $tag_line.$TAB.'link:'.$link;
			}
			push(@tag_lines, $tag_line);
		}
	}

	#end of interface declaration -- cleanup
	if ($line =~ /.*};\s*$/) {

		$attr_name = "";
		$attr_type = "";
		$is_readonly = "";
		$method_name = "";
		$return_type = "";
		$param_name = "";
		$param_type = "";
		$is_optional = 0;
		$interface_name = "";
		$inherit = "";
		$signature = "";
		$tag_line = "";
		$tag_line = "";
		$type_token = "";
		$sig = "";
	}

}
#part II -- HTML elements
#: re-parse HTML spec file and create tags based on interfaces implemented by elements
$file = $html_spec;

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
# the vast majority implement a single interface (which may in turn implement others..)
my $TAB = '	';
my $element_name = "";
my $element_interface = "";
#my $doc_url = "http://html5/";
my $got_interface = 1;
my $link = "";

foreach(@lines){

	chomp;

	my $line = $_;
	
	#start of element declaration ... get name
	if ($line =~ /The\s<dfn>\s*<code>([^<]*)<\/code>\s*<\/dfn>\s*element/i ){
		$element_name = $1;
		if ($element_name !~ /^\s*$/ ){
			$link = "";
			$got_interface = 0;
		}
	}
	
	if (!$got_interface) {

		if ($line =~ /<dd>\s*Uses\s*<code>\s*<a[^>]*>([^<]*)<\/a>/i ) {
			#print "$element_name implements interface: $1 \n";
			$element_interface = $1;
			$tag_line = $element_name.$TAB.$html_spec.$TAB.'/^'.$_.'$/;"'.$TAB.$typeToken.$TAB.'class:'.$element_name.$TAB.'type:'.$element_name.$TAB.'inherits:'.$element_interface;
			#push(@tag_lines, $tag_line);
			#$got_interface = 1;
		}

		if ($line =~ /<pre\s+class="idl">interface\s<dfn[^>]+>([A-Za-z]+)<\/dfn>/gi ) {
			#print "$element_name implements interface: $1 \n";
			$element_interface = $1;
			$tag_line = $element_name.$TAB.$html_spec.$TAB.'/^'.$_.'$/;"'.$TAB.$typeToken.$TAB.'class:'.$element_name.$TAB.'type:'.$element_name.$TAB.'inherits:'.$element_interface;
			#push(@tag_lines, $tag_line);
			#$got_interface = 1;
		}
		#grab the link to the definition in the spec
		#note this is only for the elements themselves not properties
		if ($line =~ /<a\s*href="(#[^"]*)"\s*>\s*([A-Za-z_0-9]*)\s*<\/a>/i ){
			$link = $1;
			if ($2 =~ /$element_name/i ) {
				#print "el name: $element_name  link: $link \n";
				$tag_line = $tag_line.$TAB."link:".$link;
				push(@tag_lines, $tag_line);
				$got_interface = 1;
			}
		}
	}
	
} 

#finally sort and spit out tags
my @html5tags = sort(@tag_lines);
foreach(@html5tags) {
	my $line = $_;
	if($line !~ /^ARRAY/ ){
		print $line."\n";
	}
}
