#!/bin/bash
tags:	genHTMLtags genTags.pl index.html parseIDL parseIDL.pl stripComments.pl webgl/index.html
	./genHTMLtags > tags
	./genWebGLtags > webgl/tags
