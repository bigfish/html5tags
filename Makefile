#!/bin/bash
tags:	$(HTML5_HOME)/genHTMLtags $(HTML5_HOME)/genTags.pl $(HTML5_HOME)/index.html $(HTML5_HOME)/parseIDL $(HTML5_HOME)/parseIDL.pl $(HTML5_HOME)/stripComments.pl $(HTML5_HOME)/webgl/index.html
	$(HTML5_HOME)/genHTMLtags > $(HTML5_HOME)/tags
	$(HTML5_HOME)/genWebGLTags > $(HTML5_HOME)/webgl/tags
	cp $(HTML5_HOME)/tags $(VIM4JS_HOME)/tags/html/
	cp $(HTML5_HOME)/webgl/tags $(VIM4JS_HOME)/tags/webgl/

	
