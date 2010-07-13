#!/usr/bin/perl

use File::Basename;

$file = "html5.idl";
$html_spec = "index.html";
$doc_url = "http://html5/";

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

	if ($line =~ /^interface\s+([A-Za-z]+)\s*(?::\s*([A-Za-z]+))?\s*{\s*(?:};)?/) {

		$typeToken = "c";
		$interface_name = $1;
		$inherit = $2;
		#set cmd to the url of the definition
		$tag_line = $interface_name.$TAB.$srcfile.$TAB.'/^'.$_.'$/;"'.$TAB.$typeToken.$TAB.'class:'.$interface_name;
		if ($inherit) {
			$tag_line = $tag_line.$TAB.'inherits:'.$inherit;
		}
		push(@tag_lines, $tag_line);
	}


	if ($interface_name) {
		
		#attributes
		if ($line =~ /^\s*(readonly)?\s+attribute\s+([A-Za-z]*)\s+([A-Za-z_0-9]*);/) {

			$is_readonly = $1;
			$attr_type = $2;
			$attr_name = $3;
			$typeToken = "v";
			$tag_line = $attr_name.$TAB.$srcfile.$TAB.'/^'.$_.'$/;"'.$TAB.$typeToken.$TAB.'class:'.$interface_name;

			push(@tag_lines, $tag_line);
		}

		#methods
		if ($line =~ /^\s*([A-Z-a-z]*)\s+([A-Za-z0-9_]+)\s*\(([^)]*)\);/ ) {

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
my $doc_url = "http://html5/";
my $got_interface = 1;

foreach(@lines){

	chomp;

	my $line = $_;
	
	#start of element declaration ... get name
	if ($line =~ /The\s<dfn>\s*<code>(\S*)<\/code>\s*<\/dfn>\s*element/ ){
		$element_name = $1;
		$got_interface = 0;
	}
	
	if (!$got_interface) {

		if ($line =~ /<dd>\s*Uses\s*<code>\s*<a[^>]*>([^<]*)<\/a>/ ) {
			#print "$element_name implements interface: $1 \n";
			$element_interface = $1;
			$cmd = $doc_url."#".$element_name;
			$tag_line = $element_name.$TAB.$srcfile.$TAB.'/^'.$cmd.'$/;"'.$TAB.$typeToken.$TAB.'class:'.$element_name.$TAB.'inherits:'.$element_interface;
			push(@tag_lines, $tag_line);
			$got_interface = 1;
		}

		if ($line =~ /<pre\s+class="idl">interface\s<dfn[^>]+>([A-Za-z]+)<\/dfn>/g ) {
			#print "$element_name implements interface: $1 \n";
			$element_interface = $1;
			$cmd = $doc_url."#".$element_name;
			$tag_line = $element_name.$TAB.$srcfile.$TAB.'/^'.$cmd.'$/;"'.$TAB.$typeToken.$TAB.'class:'.$element_name.$TAB.'inherits:'.$element_interface;
			push(@tag_lines, $tag_line);
			$got_interface = 1;
		}
		
	}
	
} 

#finally sort and spit out tags
my @html5tags = sort(@tag_lines);
foreach(@html5tags) {
	print $_."\n";
}
