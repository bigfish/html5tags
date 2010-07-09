#!/usr/bin/perl -w

use strict;

my $file = shift;

# define the subclass
package IdentityParse;
use base "HTML::Parser";

sub text {
    my ($self, $text) = @_;
    # just print out the original text
    print $text;
}

sub comment {
    my ($self, $comment) = @_;
    # print out original text with comment marker
    print "";
}

sub start {
    my ($self, $tag, $attr, $attrseq, $origtext) = @_;
    # print out original text
    print $origtext;
}

sub end {
    my ($self, $tag, $origtext) = @_;
    # print out original text
    print $origtext;
}

my $p = new IdentityParse;

$p->parse_file($file);
